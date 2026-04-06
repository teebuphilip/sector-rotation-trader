"""
seed.py — Bootstrap 90 days of historical simulation state.
Run ONCE manually before the first daily_run.py execution.

Usage:
    python seed.py

This walks day-by-day through the seed window applying the full
entry/exit logic so the portfolio starts in a realistic state.
"""
import pandas as pd
import numpy as np
from datetime import date, timedelta
import yfinance as yf
import json

from config import SEED_DAYS, MAX_POSITION_SIZE, STATE_FILE
from scanner import SECTOR_STOCKS, SECTOR_ETFS, find_leading_sector, filter_sector_leaders
from signals import check_entry, check_exit, get_entry_price
from portfolio import (
    _default_state, save_state, open_position, close_position,
    accrue_interest, snapshot, available_cash, can_borrow,
    save_trade_log, total_equity
)

print("=" * 60)
print("SECTOR ROTATION TRADER — SEED (90-day historical bootstrap)")
print("=" * 60)

# ── Download all data upfront ──────────────────────────────────
print("\n[1/4] Downloading sector ETF data...")
sector_raw = yf.download(SECTOR_ETFS, period="2y", auto_adjust=True, progress=False)['Close']

all_tickers = list(set(t for tl in SECTOR_STOCKS.values() for t in tl))
print(f"[2/4] Downloading {len(all_tickers)} stock tickers...")
stock_raw = yf.download(all_tickers, period="2y", auto_adjust=True, progress=False)
prices_all  = stock_raw['Close']  if isinstance(stock_raw.columns, pd.MultiIndex) else stock_raw[['Close']]
volumes_all = stock_raw['Volume'] if isinstance(stock_raw.columns, pd.MultiIndex) else stock_raw[['Volume']]

# ── Determine seed window ──────────────────────────────────────
end_date   = date.today() - timedelta(days=1)   # yesterday = sim "present"
start_date = end_date - timedelta(days=SEED_DAYS)

trading_days = [
    d for d in pd.bdate_range(start=start_date, end=end_date)
]

print(f"[3/4] Simulating {len(trading_days)} trading days ({start_date} → {end_date})...")

state = _default_state()
state["sim_start"] = start_date.isoformat()

# ── Day-by-day simulation ──────────────────────────────────────
for i, dt in enumerate(trading_days):
    dt_str = dt.strftime("%Y-%m-%d")

    # Slice data up to this day
    sec_slice  = sector_raw[sector_raw.index <= dt]
    px_slice   = prices_all[prices_all.index <= dt]
    vol_slice  = volumes_all[volumes_all.index <= dt]

    if len(sec_slice) < 130:   # not enough history for 6M calc
        continue

    # --- Current prices dict for P&L
    current_px = {}
    for ticker in list(state["positions"].keys()) + list(prices_all.columns):
        if ticker in px_slice.columns and not px_slice[ticker].empty:
            v = px_slice[ticker].dropna()
            if len(v):
                current_px[ticker] = float(v.iloc[-1])

    # --- 1. Accrue margin interest
    accrue_interest(state)

    # --- 2. Check exits on open positions
    for ticker in list(state["positions"].keys()):
        if ticker not in px_slice.columns:
            continue
        px_t = px_slice[ticker].dropna()
        if len(px_t) < 22:
            continue
        consec = state["positions"][ticker]["consec_below_ma"]
        should_exit, new_consec = check_exit(px_t, consec)
        state["positions"][ticker]["consec_below_ma"] = new_consec
        if should_exit:
            close_price = float(px_t.iloc[-1])
            close_position(state, ticker, close_price, reason="20MA_exit")

    # --- 3. Sector scan
    top_etf, spread, _ = find_leading_sector(sec_slice)
    if top_etf is None:
        snapshot(state, current_px, "none")
        continue

    candidates = filter_sector_leaders(
        top_etf,
        sec_slice[top_etf],
        px_slice[[t for t in SECTOR_STOCKS.get(top_etf, []) if t in px_slice.columns]]
    )

    # --- 4. Entry signals on candidates not already held
    for ticker in candidates:
        if ticker in state["positions"]:
            continue
        if ticker not in px_slice.columns or ticker not in vol_slice.columns:
            continue

        px_t  = px_slice[ticker].dropna()
        vol_t = vol_slice[ticker].dropna()

        if not check_entry(px_t, vol_t):
            continue

        entry_price = get_entry_price(px_t)
        if entry_price <= 0:
            continue

        cash_avail = available_cash(state)

        if cash_avail >= MAX_POSITION_SIZE:
            open_position(state, ticker, entry_price, MAX_POSITION_SIZE, using_margin=False)
        elif can_borrow(state, MAX_POSITION_SIZE):
            open_position(state, ticker, entry_price, MAX_POSITION_SIZE, using_margin=True)

    # --- 5. Snapshot
    snapshot(state, current_px, top_etf or "none")

    if i % 10 == 0:
        eq = total_equity(state, current_px)
        print(f"  Day {i+1:3d}/{len(trading_days)} | {dt_str} | "
              f"Sector: {top_etf or '—':5s} | "
              f"Positions: {len(state['positions']):2d} | "
              f"Equity: ${eq:,.0f}")

# ── Save ───────────────────────────────────────────────────────
save_state(state)
save_trade_log(state)

final_px = {}
for ticker in prices_all.columns:
    v = prices_all[ticker].dropna()
    if len(v):
        final_px[ticker] = float(v.iloc[-1])

final_equity = total_equity(state, final_px)
trades_made  = len([t for t in state["trade_log"] if t["action"] == "BUY"])
pnl_closed   = sum(t.get("pnl", 0) for t in state["trade_log"] if t["action"] == "SELL")

print("\n[4/4] Seed complete.")
print(f"  Final equity:    ${final_equity:,.2f}")
print(f"  Cash:            ${state['cash']:,.2f}")
print(f"  Borrowed:        ${state['borrowed']:,.2f}")
print(f"  Open positions:  {len(state['positions'])}")
print(f"  Trades executed: {trades_made}")
print(f"  Realized P&L:    ${pnl_closed:,.2f}")
print(f"\n  State saved → {STATE_FILE}")
print("  Ready for daily_run.py")
