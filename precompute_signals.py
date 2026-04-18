"""
precompute_signals.py
---------------------
Nightly job: for every S&P 500 ticker, map it to its SPDR sector ETF,
run the full proven signal stack against that sector, and write a
pre-computed verdict JSON to docs/signals/<TICKER>.json.

Also writes:
  docs/signals/index.json   — meta + public preview leaderboard
  docs/signals/_sectors.json — per-sector composite (for ETF lookups)

Called from GitHub Actions after crazy_run.py completes.

Usage:
  python precompute_signals.py
  python precompute_signals.py --min-days 60   # lower threshold for early launch
  python precompute_signals.py --dry-run       # compute but don't write files
"""

import argparse
import json
import os
import sys
from datetime import date, datetime, timedelta
from pathlib import Path

import pandas as pd
import yfinance as yf

# ── Paths ──────────────────────────────────────────────────────────────────────
ROOT_DIR       = Path(__file__).parent
SIGNALS_DIR    = ROOT_DIR / "docs" / "signals"
CRAZY_STATE_DIR = ROOT_DIR / "data" / "crazy" / "state"
NORMAL_STATE_DIR = ROOT_DIR / "data" / "normal" / "state"
BLOCKED_ALGOS_FILE = ROOT_DIR / "data" / "blocked" / "algos.jsonl"
DISCLAIMER     = (
    "This is an experimental signal lab. Not financial advice. "
    "Signals are research outputs, not recommendations to buy, sell, or hold any asset. "
    "Signals can and will fail. Past performance does not guarantee future results. "
    "Results are simulated/model outputs and may not reflect slippage, fees, liquidity, execution delays, or market impact. "
    "Third-party data may be incomplete, delayed, inaccurate, or revised. "
    "Do your own research and consult a qualified professional before making investment decisions. "
    "Paper-traded only — no real money at risk."
)

# ── Sector ETF map ─────────────────────────────────────────────────────────────
# yfinance sector string → SPDR ETF
SECTOR_TO_ETF = {
    "Technology":             "XLK",
    "Healthcare":             "XLV",
    "Financial Services":     "XLF",
    "Consumer Cyclical":      "XLY",
    "Industrials":            "XLI",
    "Communication Services": "XLC",
    "Consumer Defensive":     "XLP",
    "Energy":                 "XLE",
    "Basic Materials":        "XLB",
    "Real Estate":            "XLRE",
    "Utilities":              "XLU",
}

ETF_TO_SECTOR = {v: k for k, v in SECTOR_TO_ETF.items()}

ALL_ETFS = list(SECTOR_TO_ETF.values())

# ── S&P 500 ticker list ────────────────────────────────────────────────────────
def get_sp500_tickers(use_wiki: bool = True) -> list[str]:
    """
    Pull S&P 500 constituents from Wikipedia.
    Falls back to a hardcoded top-100 list if network fails.
    """
    if not use_wiki:
        print("  Using fallback S&P 500 list (no-wiki)")
        return _SP500_FALLBACK
    try:
        tables = pd.read_html(
            "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies",
            attrs={"id": "constituents"},
        )
        tickers = tables[0]["Symbol"].tolist()
        # Wikipedia uses dots (BRK.B) — yfinance uses dashes (BRK-B)
        tickers = [t.replace(".", "-") for t in tickers]
        print(f"  Loaded {len(tickers)} S&P 500 tickers from Wikipedia")
        return tickers
    except Exception as e:
        print(f"  Wikipedia fetch failed ({e}), using fallback list")
        return _SP500_FALLBACK


# Hardcoded top-100 as fallback (covers most common lookups)
_SP500_FALLBACK = [
    "AAPL","MSFT","NVDA","AMZN","META","GOOGL","GOOG","BRK-B","TSLA","LLY",
    "AVGO","JPM","V","UNH","XOM","MA","COST","HD","PG","JNJ","ABBV","BAC",
    "MRK","CRM","CVX","ORCL","NFLX","WMT","KO","PEP","AMD","TMO","ACN","MCD",
    "CSCO","ABT","LIN","DHR","TXN","PM","CAT","AMGN","GE","INTU","MS","ISRG",
    "RTX","SPGI","GS","BLK","AMAT","AXP","NEE","T","VRTX","SYK","BSX","REGN",
    "ETN","MDT","CI","PLD","ADI","GILD","ZTS","MMC","CB","SCHW","DE","HCA",
    "SO","MO","NOC","DUK","USB","CME","WM","EMR","AON","PNC","TGT","MCO",
    "ELV","CL","ITW","FDX","SHW","FCX","GD","APH","NSC","EOG","MPC","PSX",
    "HUM","NEM","F","GM","DAL","UAL","MAR","HLT","DIS","CMCSA","VZ","INTC",
]


# ── Sector cache ───────────────────────────────────────────────────────────────
_sector_cache: dict[str, str] = {}   # ticker → ETF
_sector_cache_file = ROOT_DIR / "cache" / "ticker_sectors.json"

def load_sector_cache():
    if _sector_cache_file.exists():
        try:
            data = json.loads(_sector_cache_file.read_text())
            _sector_cache.update(data)
        except Exception:
            pass

def save_sector_cache():
    _sector_cache_file.parent.mkdir(parents=True, exist_ok=True)
    _sector_cache_file.write_text(json.dumps(_sector_cache, indent=2))

from typing import Optional


def get_sector_etf(ticker: str) -> Optional[str]:
    """Map a ticker to its SPDR sector ETF. Cached."""
    if ticker in _sector_cache:
        return _sector_cache[ticker]

    # Direct ETF lookup
    if ticker in ALL_ETFS:
        _sector_cache[ticker] = ticker
        return ticker

    try:
        info = yf.Ticker(ticker).info
        sector = info.get("sector", "")
        etf = SECTOR_TO_ETF.get(sector)
        if etf:
            _sector_cache[ticker] = etf
            return etf
    except Exception:
        pass

    _sector_cache[ticker] = None
    return None


# ── Signal state loader ────────────────────────────────────────────────────────
def load_algo_states() -> list[dict]:
    """
    Load all algo state files and return metadata for proven algos.
    An algo is "proven" (Tier 1) if it has >= MIN_DAYS of daily snapshots.
    """
    states = []

    for state_dir, algo_type in [
        (CRAZY_STATE_DIR, "crazy"),
        (NORMAL_STATE_DIR, "normal"),
    ]:
        if not state_dir.exists():
            continue
        for f in state_dir.glob("*.json"):
            try:
                data = json.loads(f.read_text())
                snapshots = data.get("daily_snapshots", [])
                trade_log = data.get("trade_log", [])
                algo_id   = f.stem

                states.append({
                    "algo_id":    algo_id,
                    "algo_type":  algo_type,
                    "state_path": str(f),
                    "snapshots":  snapshots,
                    "trade_log":  trade_log,
                    "days":       len(snapshots),
                    "data":       data,
                })
            except Exception:
                continue

    return states


def get_lab_start(states: list[dict]) -> str:
    """Earliest state start date across all loaded algos."""
    starts = []
    for state in states:
        data = state.get("data", {})
        sim_start = data.get("sim_start")
        if sim_start:
            starts.append(str(sim_start))
            continue
        snapshots = state.get("snapshots", [])
        if snapshots and snapshots[0].get("date"):
            starts.append(str(snapshots[0]["date"]))
    return sorted(starts)[0] if starts else "unknown"


def load_blocked_algos() -> list[dict]:
    """Return latest blocked-key record for each algo."""
    if not BLOCKED_ALGOS_FILE.exists():
        return []
    latest = {}
    for line in BLOCKED_ALGOS_FILE.read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if not s:
            continue
        try:
            obj = json.loads(s)
        except Exception:
            continue
        algo_id = obj.get("algo_id")
        if algo_id:
            latest[algo_id] = {
                "timestamp": obj.get("timestamp", ""),
                "algo_id": algo_id,
                "name": obj.get("name", algo_id),
                "keys": obj.get("keys", []),
                "reason": obj.get("reason", ""),
            }
    return sorted(latest.values(), key=lambda x: x["algo_id"])


def get_current_positions(state_data: dict) -> set[str]:
    """Return set of ETFs currently held by this algo."""
    return set(state_data.get("positions", {}).keys())


def get_recent_signal_direction(state_data: dict, etf: str) -> str:
    """
    Infer current signal direction for an ETF from algo state.

    Logic:
    - If ETF is currently held → BULLISH
    - If ETF was recently sold (last 5 trade days) → BEARISH
    - If cash/no position → NEUTRAL
    """
    positions = state_data.get("positions", {})
    if etf in positions:
        return "BULLISH"

    # Check recent trade log for this ETF
    trade_log = state_data.get("trade_log", [])
    recent = sorted(trade_log, key=lambda t: t.get("date", ""), reverse=True)[:20]

    for trade in recent:
        if trade.get("ticker") == etf:
            action = trade.get("action", "")
            if action == "SELL":
                return "BEARISH"
            if action == "BUY":
                return "BULLISH"

    # No positions, no recent trades for this ETF = neutral
    if not positions:
        return "NEUTRAL"

    # Holding something else = implicitly bearish on this ETF
    return "BEARISH"


def get_algo_display_name(algo_id: str, state_data: dict) -> str:
    """Best-effort human name for an algo."""
    # Some algos store name in meta
    meta = state_data.get("meta", {})
    for key, val in meta.items():
        if isinstance(val, dict) and val.get("name"):
            return val["name"]

    # Title-case the algo_id
    return algo_id.replace("_", " ").replace("-", " ").title()


# ── Performance stats ──────────────────────────────────────────────────────────
def compute_algo_performance(snapshots: list[dict]) -> dict:
    """Compute YTD return, Sharpe proxy, and SPY beat flag from snapshots."""
    if len(snapshots) < 2:
        return {"ytd_pct": 0.0, "beat_spy": False, "days_running": 0}

    start_equity = snapshots[0].get("equity", 100_000)
    end_equity   = snapshots[-1].get("equity", 100_000)

    ytd_pct = ((end_equity - start_equity) / start_equity * 100) if start_equity else 0.0

    # SPY return over same window
    spy_start = snapshots[0].get("spy_equity", start_equity)
    spy_end   = snapshots[-1].get("spy_equity", end_equity)
    spy_pct   = ((spy_end - spy_start) / spy_start * 100) if spy_start else 0.0

    return {
        "ytd_pct":     round(ytd_pct, 2),
        "spy_pct":     round(spy_pct, 2),
        "beat_spy":    ytd_pct > spy_pct,
        "days_running": len(snapshots),
        "equity":      round(end_equity, 2),
    }


# ── Core: compute sector verdict ──────────────────────────────────────────────
def compute_sector_verdict(
    etf: str,
    proven_states: list[dict],
) -> dict:
    """
    Run all proven algo states against one sector ETF.
    Returns bullish/bearish/neutral counts and per-algo breakdown.
    """
    breakdown = []
    bullish = bearish = neutral = 0

    for s in proven_states:
        direction = get_recent_signal_direction(s["data"], etf)
        perf      = compute_algo_performance(s["snapshots"])

        entry = {
            "algo_id":     s["algo_id"],
            "name":        get_algo_display_name(s["algo_id"], s["data"]),
            "algo_type":   s["algo_type"],
            "direction":   direction,
            "days_running": s["days"],
            "ytd_pct":     perf["ytd_pct"],
            "beat_spy":    perf["beat_spy"],
        }
        breakdown.append(entry)

        if direction == "BULLISH":
            bullish += 1
        elif direction == "BEARISH":
            bearish += 1
        else:
            neutral += 1

    total_active = bullish + bearish  # exclude neutral from pct calc
    pct = round(bullish / total_active * 100) if total_active else 50

    if pct >= 65:
        composite_label = "BULLISH"
        composite_color = "green"
    elif pct <= 35:
        composite_label = "BEARISH"
        composite_color = "red"
    else:
        composite_label = "MIXED"
        composite_color = "yellow"

    return {
        "etf":             etf,
        "sector":          ETF_TO_SECTOR.get(etf, etf),
        "bullish":         bullish,
        "bearish":         bearish,
        "neutral":         neutral,
        "total_signals":   len(proven_states),
        "total_active":    total_active,
        "bullish_pct":     pct,
        "composite":       f"{bullish} of {total_active}",
        "composite_label": composite_label,
        "composite_color": composite_color,
        "breakdown":       breakdown,
    }


# ── Write helpers ──────────────────────────────────────────────────────────────
def write_json(path: Path, data: dict):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, default=str))


# ── Main ───────────────────────────────────────────────────────────────────────
def main(min_days: int = 30, dry_run: bool = False, use_wiki: bool = True):
    today = date.today()
    print(f"\n=== precompute_signals.py — {today} ===")
    print(f"  min_days={min_days}  dry_run={dry_run}")

    # 1. Load sector cache
    load_sector_cache()

    # 2. Load all algo states
    print("\n[1/5] Loading algo states...")
    all_states = load_algo_states()
    proven     = [s for s in all_states if s["days"] >= min_days]
    lab_start  = get_lab_start(all_states)
    blocked_algos = load_blocked_algos()
    print(f"  Total algos: {len(all_states)}")
    print(f"  Proven (>= {min_days} days): {len(proven)}")
    print(f"  Lab started: {lab_start}")
    print(f"  Blocked algos: {len(blocked_algos)}")

    if not proven:
        print("  No proven algos yet — exiting. Run with --min-days 1 to include all.")
        sys.exit(0)

    # 3. Pre-compute verdict for every sector ETF
    print("\n[2/5] Computing sector verdicts...")
    sector_verdicts: dict[str, dict] = {}

    for etf in ALL_ETFS:
        verdict = compute_sector_verdict(etf, proven)
        sector_verdicts[etf] = verdict
        label = verdict["composite_label"]
        comp  = verdict["composite"]
        print(f"  {etf:5s}  {comp:12s}  {label}")

    # 4. Write per-sector JSON
    print("\n[3/5] Writing sector JSONs...")
    sectors_output = {}
    for etf, verdict in sector_verdicts.items():
        payload = {
            **verdict,
            "generated":    today.isoformat(),
            "lab_started":  lab_start,
            "disclaimer":   DISCLAIMER,
        }
        if not dry_run:
            write_json(SIGNALS_DIR / "_sectors" / f"{etf}.json", payload)
        sectors_output[etf] = {
            "etf":             etf,
            "sector":          verdict["sector"],
            "composite":       verdict["composite"],
            "composite_label": verdict["composite_label"],
            "composite_color": verdict["composite_color"],
            "bullish_pct":     verdict["bullish_pct"],
        }

    if not dry_run:
        write_json(SIGNALS_DIR / "_sectors.json", {
            "generated":   today.isoformat(),
            "lab_started": lab_start,
            "sectors":     sectors_output,
        })
        print(f"  Wrote _sectors.json")

    # 5. Get S&P 500 tickers and write per-ticker JSON
    print("\n[4/5] Writing per-ticker JSONs...")
    tickers = get_sp500_tickers(use_wiki=use_wiki)

    written = skipped = errors = 0
    ticker_index = {}

    for ticker in tickers:
        try:
            etf = get_sector_etf(ticker)
            if etf is None:
                skipped += 1
                continue

            verdict = sector_verdicts.get(etf)
            if verdict is None:
                skipped += 1
                continue

            payload = {
                "ticker":          ticker,
                "sector":          verdict["sector"],
                "sector_etf":      etf,
                "composite":       verdict["composite"],
                "composite_label": verdict["composite_label"],
                "composite_color": verdict["composite_color"],
                "bullish":         verdict["bullish"],
                "bearish":         verdict["bearish"],
                "neutral":         verdict["neutral"],
                "total_signals":   verdict["total_signals"],
                "total_active":    verdict["total_active"],
                "bullish_pct":     verdict["bullish_pct"],
                "breakdown":       verdict["breakdown"],
                "generated":       today.isoformat(),
                "lab_started":     lab_start,
                "disclaimer":      DISCLAIMER,
            }

            if not dry_run:
                write_json(SIGNALS_DIR / f"{ticker}.json", payload)

            ticker_index[ticker] = {
                "sector_etf":      etf,
                "composite_label": verdict["composite_label"],
                "bullish_pct":     verdict["bullish_pct"],
            }
            written += 1

        except Exception as e:
            print(f"  ERROR {ticker}: {e}")
            errors += 1

    # Save sector cache (avoids re-fetching next run)
    if not dry_run:
        save_sector_cache()

    print(f"  Written: {written}  Skipped: {skipped}  Errors: {errors}")

    # 6. Write index.json (public preview data + leaderboard)
    print("\n[5/5] Writing index.json...")

    # Build leaderboard from proven algos
    leaderboard = []
    for s in proven:
        perf = compute_algo_performance(s["snapshots"])
        leaderboard.append({
            "algo_id":     s["algo_id"],
            "name":        get_algo_display_name(s["algo_id"], s["data"]),
            "algo_type":   s["algo_type"],
            "ytd_pct":     perf["ytd_pct"],
            "spy_pct":     perf["spy_pct"],
            "beat_spy":    perf["beat_spy"],
            "days_running": s["days"],
            "equity":      perf["equity"],
        })

    leaderboard.sort(key=lambda x: x["ytd_pct"], reverse=True)

    # Top bullish / bearish sectors
    sorted_sectors = sorted(
        sector_verdicts.values(),
        key=lambda v: v["bullish_pct"],
        reverse=True,
    )
    top_bullish = [v["etf"] for v in sorted_sectors[:3]]
    top_bearish = [v["etf"] for v in sorted_sectors[-3:]]

    index = {
        "generated":        today.isoformat(),
        "lab_started":      lab_start,
        "signal_count":     len(proven),
        "total_algos":      len(all_states),
        "ticker_count":     written,
        "top_bullish_etfs": top_bullish,
        "top_bearish_etfs": top_bearish,
        "sector_summary":   sectors_output,
        "leaderboard":      leaderboard[:20],   # top 20 for public preview
        "ticker_index":     ticker_index,        # used by free ticker search
        "idle_algos":       sum(1 for s in all_states if len(s.get("trade_log", [])) == 0),
        "blocked_algos":    blocked_algos,
        "disclaimer":       DISCLAIMER,
    }

    if not dry_run:
        write_json(SIGNALS_DIR / "index.json", index)
        print(f"  Wrote index.json  ({len(leaderboard)} algos in leaderboard)")

    # ── Summary ───────────────────────────────────────────────────────────────
    print(f"\n=== Done ===")
    print(f"  Proven algos:   {len(proven)}")
    print(f"  Tickers written: {written}")
    print(f"  Sectors computed: {len(sector_verdicts)}")
    print(f"  Top BULLISH:    {', '.join(top_bullish)}")
    print(f"  Top BEARISH:    {', '.join(top_bearish)}")

    beats = sum(1 for s in proven if compute_algo_performance(s["snapshots"])["beat_spy"])
    print(f"  Algos beating SPY: {beats} of {len(proven)}")

    if dry_run:
        print("\n  DRY RUN — no files written")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Pre-compute signal verdicts")
    parser.add_argument(
        "--min-days",
        type=int,
        default=30,
        help="Minimum days of history for an algo to be included (default: 30)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Compute but do not write any files",
    )
    parser.add_argument(
        "--no-wiki",
        action="store_true",
        help="Skip Wikipedia and use fallback S&P 500 list",
    )
    args = parser.parse_args()
    main(min_days=args.min_days, dry_run=args.dry_run, use_wiki=not args.no_wiki)
