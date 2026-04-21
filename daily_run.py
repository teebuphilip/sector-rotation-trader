"""
daily_run.py — Runs once per day via GitHub Actions.
  1. Load state
  2. Accrue margin interest
  3. Check exits on open positions
  4. Sector scan → find leading sector
  5. Filter stock leaders
  6. Check entry signals → open positions (cash first, margin if needed)
  7. Snapshot portfolio
  8. Regenerate HTML dashboard
  9. Save state + trade log
"""
import sys
import argparse
import pandas as pd
from datetime import date

parser = argparse.ArgumentParser()
parser.add_argument("--dry-run", action="store_true", help="Run without saving state or dashboard")
args = parser.parse_args()
DRY_RUN = args.dry_run

from config import (
    MAX_POSITION_SIZE, SECTOR_ETFS,
    STOP_LOSS_PCT, MAX_DRAWDOWN_PCT, MAX_POSITIONS_PER_SECTOR
)
from scanner import SECTOR_STOCKS, find_leading_sector, filter_sector_leaders, safe_download
from signals import check_entry, check_exit, get_entry_price
from portfolio import (
    load_state, save_state, open_position, close_position,
    accrue_interest, snapshot, available_cash, can_borrow,
    save_trade_log, total_equity, compute_analytics
)
from dashboard import generate_dashboard

print("=" * 60)
print(f"SECTOR ROTATION TRADER — Daily Run {date.today()}" + (" [DRY RUN]" if DRY_RUN else ""))
print("=" * 60)

# ── Load state ─────────────────────────────────────────────────
state = load_state()
print(f"\nLoaded state | Cash: ${state['cash']:,.0f} | "
      f"Borrowed: ${state['borrowed']:,.0f} | "
      f"Open positions: {len(state['positions'])}")

# ── Download data ──────────────────────────────────────────────
print("\n[1/6] Downloading market data...")
sector_raw = safe_download(SECTOR_ETFS, period="1y")
if sector_raw.empty:
    print("  ✖ Failed to download sector ETF data — aborting run.")
    sys.exit(0)
sector_data = sector_raw['Close']

# Build ticker list: all sector stocks + currently held tickers
held_tickers = list(state["positions"].keys())
scan_sector_raw, _, _ = find_leading_sector(sector_data)
candidate_universe = list(set(
    SECTOR_STOCKS.get(scan_sector_raw, []) + held_tickers
)) if scan_sector_raw else held_tickers

all_needed = list(set(candidate_universe + held_tickers))

if all_needed:
    raw = safe_download(all_needed, period="1y")
    if raw.empty:
        if state["positions"]:
            print("  ✖ Failed to download stock data with open positions — aborting run.")
            sys.exit(1)
        print("  ⚠ Failed to download stock data — no open positions, skipping entries.")
        prices_all  = pd.DataFrame()
        volumes_all = pd.DataFrame()
    elif isinstance(raw.columns, pd.MultiIndex):
        prices_all  = raw['Close']
        volumes_all = raw['Volume']
    else:
        prices_all  = raw[['Close']]
        volumes_all = raw[['Volume']]
else:
    prices_all  = pd.DataFrame()
    volumes_all = pd.DataFrame()

# Current price dict
current_px = {}
for ticker in (prices_all.columns if not prices_all.empty else []):
    s = prices_all[ticker].dropna()
    if len(s):
        current_px[ticker] = float(s.iloc[-1])

# ── Step 1: Accrue margin interest ────────────────────────────
print(f"\n[2/6] Accruing margin interest on ${state['borrowed']:,.0f} borrowed...")
accrue_interest(state)

# ── Step 2: Check exits ────────────────────────────────────────
print(f"\n[3/6] Checking exit signals on {len(state['positions'])} positions...")
exits_today = []
for ticker in list(state["positions"].keys()):
    if ticker not in prices_all.columns:
        print(f"  ⚠ {ticker}: no price data, skipping exit check")
        continue
    px_t   = prices_all[ticker].dropna()
    pos    = state["positions"][ticker]
    cur_px = current_px.get(ticker, pos["entry_price"])

    # Hard stop-loss check
    loss_pct = (cur_px - pos["entry_price"]) / pos["entry_price"]
    if loss_pct <= -STOP_LOSS_PCT:
        close_position(state, ticker, cur_px, reason="stop_loss")
        exits_today.append(ticker)
        print(f"  ✖ STOP-LOSS {ticker} @ ${cur_px:.2f} ({loss_pct:.1%})")
        continue

    consec = pos.get("consec_below_ma", 0)
    should_exit, new_consec = check_exit(px_t, consec)
    state["positions"][ticker]["consec_below_ma"] = new_consec
    if should_exit:
        close_position(state, ticker, cur_px, reason="20MA_exit")
        exits_today.append(ticker)
        print(f"  ✖ EXITED {ticker} @ ${cur_px:.2f}")
    else:
        unr = (current_px.get(ticker, state["positions"][ticker]["entry_price"])
               - state["positions"][ticker]["entry_price"]) * state["positions"][ticker]["shares"]
        print(f"  ✓ HOLD   {ticker} | consec_below_MA={new_consec} | unrealized P&L: ${unr:+,.0f}")

# ── Step 3: Sector scan ────────────────────────────────────────
print(f"\n[4/6] Running sector scan...")
top_etf, spread, sector_df = find_leading_sector(sector_data)

if top_etf:
    print(f"  Leading sector: {top_etf} (spread: {spread:.2%})")
    print(f"  Accelerating sectors:")
    for etf, row in sector_df[sector_df["3M"] > sector_df["6M"]].iterrows():
        marker = " ◄ LEADER" if etf == top_etf else ""
        print(f"    {etf:5s}  3M={row['3M']:.1%}  6M={row['6M']:.1%}{marker}")
else:
    print("  No accelerating sector found today.")

# ── Step 4: Filter stock leaders ──────────────────────────────
candidates = []
if top_etf and not prices_all.empty:
    print(f"\n[5/6] Filtering stock leaders in {top_etf}...")
    sector_stocks_avail = [t for t in SECTOR_STOCKS.get(top_etf, []) if t in prices_all.columns]
    candidates = filter_sector_leaders(
        top_etf,
        sector_data[top_etf],
        prices_all[sector_stocks_avail]
    )
    print(f"  Candidates outperforming ETF: {candidates}")
else:
    print("\n[5/6] Skipping stock filter — no leading sector.")

# ── Step 5: Entry signals ──────────────────────────────────────
print(f"\n[6/6] Checking entry signals...")
entries_today = []

# Drawdown circuit breaker
peak_equity = max(
    (s["equity"] for s in state["daily_snapshots"]),
    default=100_000
)
cur_equity = total_equity(state, current_px)
drawdown = (cur_equity - peak_equity) / peak_equity if peak_equity > 0 else 0
drawdown_blocked = drawdown <= -MAX_DRAWDOWN_PCT
if drawdown_blocked:
    print(f"  ⚠ DRAWDOWN BREAKER: {drawdown:.1%} from peak — no new entries")

# Count positions per sector for concentration limit
def sector_for_ticker(t):
    for etf, tickers in SECTOR_STOCKS.items():
        if t in tickers:
            return etf
    return None

sector_counts = {}
for t in state["positions"]:
    sec = sector_for_ticker(t)
    if sec:
        sector_counts[sec] = sector_counts.get(sec, 0) + 1

for ticker in candidates:
    if drawdown_blocked:
        break
    if ticker in state["positions"]:
        print(f"  ~ {ticker}: already held, skip")
        continue
    if ticker not in prices_all.columns or ticker not in volumes_all.columns:
        continue

    # Sector concentration check
    t_sector = sector_for_ticker(ticker)
    if t_sector and sector_counts.get(t_sector, 0) >= MAX_POSITIONS_PER_SECTOR:
        print(f"  ~ {ticker}: sector {t_sector} at max {MAX_POSITIONS_PER_SECTOR} positions, skip")
        continue

    px_t  = prices_all[ticker].dropna()
    vol_t = volumes_all[ticker].dropna()

    if not check_entry(px_t, vol_t):
        print(f"  . {ticker}: no entry signal")
        continue

    entry_price = get_entry_price(px_t)
    cash_avail  = available_cash(state)

    if cash_avail >= MAX_POSITION_SIZE:
        open_position(state, ticker, entry_price, MAX_POSITION_SIZE, using_margin=False)
        entries_today.append(ticker)
        if t_sector:
            sector_counts[t_sector] = sector_counts.get(t_sector, 0) + 1
        print(f"  ✚ ENTERED {ticker} @ ${entry_price:.2f} (cash)")
    elif can_borrow(state, MAX_POSITION_SIZE):
        open_position(state, ticker, entry_price, MAX_POSITION_SIZE, using_margin=True)
        entries_today.append(ticker)
        if t_sector:
            sector_counts[t_sector] = sector_counts.get(t_sector, 0) + 1
        print(f"  ✚ ENTERED {ticker} @ ${entry_price:.2f} (MARGIN)")
    else:
        print(f"  ✗ {ticker}: signal fired but insufficient cash + margin")

# ── Snapshot + save ────────────────────────────────────────────
snapshot(state, current_px, top_etf or "none")
if not DRY_RUN:
    save_state(state)
    save_trade_log(state)
else:
    print("\n  [DRY RUN] Skipping state save.")

# ── SPY benchmark ─────────────────────────────────────────────
spy_raw = safe_download(["SPY"], period="1y")
spy_prices = None
if not spy_raw.empty:
    spy_prices = spy_raw['Close'] if 'Close' in spy_raw.columns else spy_raw[['Close']]

# ── Dashboard ──────────────────────────────────────────────────
analytics = compute_analytics(state)
if not DRY_RUN:
    generate_dashboard(state, current_px, top_etf, analytics=analytics, spy_prices=spy_prices)
else:
    print("  [DRY RUN] Skipping dashboard generation.")

# ── Summary ────────────────────────────────────────────────────
equity = total_equity(state, current_px)
realized = sum(t.get("pnl", 0) for t in state["trade_log"] if t["action"] == "SELL")

print("\n" + "=" * 60)
print("DAILY SUMMARY")
print(f"  Date:           {date.today()}")
print(f"  Leading sector: {top_etf or 'none'}")
print(f"  Entries today:  {entries_today or 'none'}")
print(f"  Exits today:    {exits_today or 'none'}")
print(f"  Open positions: {len(state['positions'])}")
print(f"  Cash:           ${state['cash']:,.2f}")
print(f"  Borrowed:       ${state['borrowed']:,.2f}")
print(f"  Total equity:   ${equity:,.2f}")
print(f"  Realized P&L:   ${realized:,.2f}")
print(f"  Net P&L:        ${equity - 100_000:,.2f}")
print("=" * 60)
