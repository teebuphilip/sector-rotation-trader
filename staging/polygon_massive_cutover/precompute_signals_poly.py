"""
precompute_signals_poly.py — Drop-in replacement for precompute_signals.py using Polygon.io.

The only yfinance dependency in precompute_signals.py is get_sector_etf(), which calls
yf.Ticker(ticker).info to get the "sector" string. This file replaces that lookup with
Polygon's /v3/reference/tickers/{ticker} endpoint (sic_code → ETF mapping).

Everything else is identical to precompute_signals.py.

Swap instructions (Week 3):
  1. Set POLYGON_API_KEY in GitHub Actions secrets
  2. In daily_run.yml: replace `python precompute_signals.py` with
     `python precompute_signals_poly.py`
  3. Delete precompute_signals.py (or keep as fallback)

SIC code ranges used for ETF mapping are broad-brush approximations.
The sector cache (cache/ticker_sectors.json) persists across runs so each
ticker is only looked up once — the mapping only needs to be correct, not fast.
"""

import argparse
import json
import os
import sys
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Optional

import pandas as pd

_POLYGON_BASE = "https://api.polygon.io"

# ── Paths ──────────────────────────────────────────────────────────────────────
ROOT_DIR        = Path(__file__).parent
SIGNALS_DIR     = ROOT_DIR / "docs" / "signals"
CRAZY_STATE_DIR = ROOT_DIR / "data" / "crazy" / "state"
NORMAL_STATE_DIR = ROOT_DIR / "data" / "normal" / "state"
BLOCKED_ALGOS_FILE = ROOT_DIR / "data" / "blocked" / "algos.jsonl"
DISCLAIMER = (
    "This is an experimental signal lab. Not financial advice. "
    "Signals are research outputs, not recommendations to buy, sell, or hold any asset. "
    "Signals can and will fail. Past performance does not guarantee future results. "
    "Results are simulated/model outputs and may not reflect slippage, fees, liquidity, execution delays, or market impact. "
    "Third-party data may be incomplete, delayed, inaccurate, or revised. "
    "Do your own research and consult a qualified professional before making investment decisions. "
    "Paper-traded only — no real money at risk."
)

# ── Sector ETF map ─────────────────────────────────────────────────────────────
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


def _sic_to_etf(sic_str):
    """
    Map a 4-digit SIC code to the nearest SPDR sector ETF.
    Broad-brush — precise enough for S&P 500 constituents.
    """
    try:
        code = int(sic_str)
    except (TypeError, ValueError):
        return None

    # Agriculture, Forestry, Fishing
    if 100 <= code <= 999:
        return "XLB"
    # Oil & Gas Extraction / Mining
    if 1000 <= code <= 1499:
        return "XLE" if 1300 <= code <= 1399 else "XLB"
    # Construction
    if 1500 <= code <= 1799:
        return "XLI"
    # Food & Tobacco (Consumer Defensive)
    if 2000 <= code <= 2199:
        return "XLP"
    # Pharma / Biotech
    if 2830 <= code <= 2836:
        return "XLV"
    # Chemicals (Basic Materials)
    if 2800 <= code <= 2999:
        return "XLB"
    # Industrial Manufacturing
    if 2000 <= code <= 3499:
        return "XLI"
    # Semiconductors & Electronic Components
    if 3559 <= code <= 3679:
        return "XLK"
    # Medical devices / instruments
    if 3841 <= code <= 3845:
        return "XLV"
    # General manufacturing
    if 3000 <= code <= 3999:
        return "XLI"
    # Rail / Trucking / Air transport
    if 4000 <= code <= 4799:
        return "XLI"
    # Telecom
    if 4800 <= code <= 4899:
        return "XLC"
    # Utilities
    if 4900 <= code <= 4999:
        return "XLU"
    # Wholesale trade
    if 5000 <= code <= 5199:
        return "XLI"
    # Food & Drug retail (Consumer Defensive)
    if 5400 <= code <= 5499:
        return "XLP"
    # Retail trade (Consumer Discretionary)
    if 5200 <= code <= 5999:
        return "XLY"
    # Banks / Credit
    if 6000 <= code <= 6199:
        return "XLF"
    # Insurance
    if 6300 <= code <= 6499:
        return "XLF"
    # Real Estate
    if 6500 <= code <= 6599:
        return "XLRE"
    # Investment firms / Asset mgmt
    if 6200 <= code <= 6726:
        return "XLF"
    # Hotels / Amusement / Entertainment
    if 7000 <= code <= 7299:
        return "XLY"
    # Computer Programming / Software / Data Processing
    if 7370 <= code <= 7379:
        return "XLK"
    # Motion pictures / Broadcasting
    if 7800 <= code <= 7999:
        return "XLC"
    # Health Services
    if 8000 <= code <= 8099:
        return "XLV"
    # Engineering / Research
    if 8700 <= code <= 8999:
        return "XLK"

    return None


def _polygon_api_key():
    key = os.getenv("POLYGON_API_KEY", "")
    if not key:
        raise EnvironmentError("POLYGON_API_KEY not set")
    return key


def _fetch_ticker_details(ticker, api_key):
    """Call Polygon /v3/reference/tickers/{ticker}, return results dict or {}."""
    import requests
    poly_ticker = ticker.replace("-", ".")
    url = f"{_POLYGON_BASE}/v3/reference/tickers/{poly_ticker}?apiKey={api_key}"
    try:
        resp = requests.get(url, timeout=10)
        if resp.status_code == 200:
            return resp.json().get("results", {})
    except Exception:
        pass
    return {}


# ── Sector cache ───────────────────────────────────────────────────────────────
_sector_cache = {}
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


def get_sector_etf(ticker):
    """Map a ticker to its SPDR sector ETF using Polygon reference data. Cached."""
    cached = _sector_cache.get(ticker)
    if cached:
        return cached

    if ticker in ALL_ETFS:
        _sector_cache[ticker] = ticker
        return ticker

    try:
        api_key = _polygon_api_key()
        details = _fetch_ticker_details(ticker, api_key)
        sic_code = details.get("sic_code")
        if sic_code:
            etf = _sic_to_etf(sic_code)
            if etf:
                _sector_cache[ticker] = etf
                return etf
    except EnvironmentError:
        pass
    except Exception:
        pass

    return None


# ── S&P 500 ticker list (unchanged from precompute_signals.py) ─────────────────
def get_sp500_tickers(use_wiki=True):
    if not use_wiki:
        return _SP500_FALLBACK
    try:
        tables = pd.read_html(
            "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies",
            attrs={"id": "constituents"},
        )
        tickers = tables[0]["Symbol"].tolist()
        tickers = [t.replace(".", "-") for t in tickers]
        print(f"  Loaded {len(tickers)} S&P 500 tickers from Wikipedia")
        return tickers
    except Exception as e:
        print(f"  Wikipedia fetch failed ({e}), using fallback list")
        return _SP500_FALLBACK


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


# ── Everything below is identical to precompute_signals.py ────────────────────

def load_algo_states():
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


def get_lab_start(states):
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


def load_blocked_algos():
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
                "algo_id":   algo_id,
                "name":      obj.get("name", algo_id),
                "keys":      obj.get("keys", []),
                "reason":    obj.get("reason", ""),
            }
    return sorted(latest.values(), key=lambda x: x["algo_id"])


def get_current_positions(state_data):
    return set(state_data.get("positions", {}).keys())


def get_recent_signal_direction(state_data, etf):
    positions = state_data.get("positions", {})
    if etf in positions:
        return "BULLISH"
    trade_log = state_data.get("trade_log", [])
    recent = sorted(trade_log, key=lambda t: t.get("date", ""), reverse=True)[:20]
    for trade in recent:
        if trade.get("ticker") == etf:
            action = trade.get("action", "")
            if action == "SELL":
                return "BEARISH"
            if action == "BUY":
                return "BULLISH"
    if not positions:
        return "NEUTRAL"
    return "BEARISH"


def get_algo_display_name(algo_id, state_data):
    meta = state_data.get("meta", {})
    for key, val in meta.items():
        if isinstance(val, dict) and val.get("name"):
            return val["name"]
    return algo_id.replace("_", " ").replace("-", " ").title()


def compute_algo_performance(snapshots):
    if len(snapshots) < 2:
        return {"ytd_pct": 0.0, "beat_spy": False, "days_running": 0}
    start_equity = snapshots[0].get("equity", 100_000)
    end_equity   = snapshots[-1].get("equity", 100_000)
    ytd_pct = ((end_equity - start_equity) / start_equity * 100) if start_equity else 0.0
    spy_start = snapshots[0].get("spy_equity", start_equity)
    spy_end   = snapshots[-1].get("spy_equity", end_equity)
    spy_pct   = ((spy_end - spy_start) / spy_start * 100) if spy_start else 0.0
    return {
        "ytd_pct":      round(ytd_pct, 2),
        "spy_pct":      round(spy_pct, 2),
        "beat_spy":     ytd_pct > spy_pct,
        "days_running": len(snapshots),
        "equity":       round(end_equity, 2),
    }


def compute_sector_verdict(etf, proven_states):
    breakdown = []
    bullish = bearish = neutral = 0
    for s in proven_states:
        direction = get_recent_signal_direction(s["data"], etf)
        perf      = compute_algo_performance(s["snapshots"])
        entry = {
            "algo_id":      s["algo_id"],
            "name":         get_algo_display_name(s["algo_id"], s["data"]),
            "algo_type":    s["algo_type"],
            "direction":    direction,
            "days_running": s["days"],
            "ytd_pct":      perf["ytd_pct"],
            "beat_spy":     perf["beat_spy"],
        }
        breakdown.append(entry)
        if direction == "BULLISH":
            bullish += 1
        elif direction == "BEARISH":
            bearish += 1
        else:
            neutral += 1

    total_active = bullish + bearish
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


def write_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, default=str))


def main(min_days=30, dry_run=False, use_wiki=True):
    today = date.today()
    print(f"\n=== precompute_signals_poly.py — {today} ===")
    print(f"  min_days={min_days}  dry_run={dry_run}")

    load_sector_cache()

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

    print("\n[2/5] Computing sector verdicts...")
    sector_verdicts = {}
    for etf in ALL_ETFS:
        verdict = compute_sector_verdict(etf, proven)
        sector_verdicts[etf] = verdict
        print(f"  {etf:5s}  {verdict['composite']:12s}  {verdict['composite_label']}")

    print("\n[3/5] Writing sector JSONs...")
    sectors_output = {}
    for etf, verdict in sector_verdicts.items():
        payload = {
            **verdict,
            "generated":   today.isoformat(),
            "lab_started": lab_start,
            "disclaimer":  DISCLAIMER,
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

    if not dry_run:
        save_sector_cache()

    print(f"  Written: {written}  Skipped: {skipped}  Errors: {errors}")

    print("\n[5/5] Writing index.json...")
    leaderboard = []
    for s in proven:
        perf = compute_algo_performance(s["snapshots"])
        leaderboard.append({
            "algo_id":      s["algo_id"],
            "name":         get_algo_display_name(s["algo_id"], s["data"]),
            "algo_type":    s["algo_type"],
            "ytd_pct":      perf["ytd_pct"],
            "spy_pct":      perf["spy_pct"],
            "beat_spy":     perf["beat_spy"],
            "days_running": s["days"],
            "equity":       perf["equity"],
        })

    leaderboard.sort(key=lambda x: x["ytd_pct"], reverse=True)

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
        "leaderboard":      leaderboard[:20],
        "ticker_index":     ticker_index,
        "idle_algos":       sum(1 for s in all_states if len(s.get("trade_log", [])) == 0),
        "blocked_algos":    blocked_algos,
        "disclaimer":       DISCLAIMER,
    }

    if not dry_run:
        write_json(SIGNALS_DIR / "index.json", index)
        print(f"  Wrote index.json  ({len(leaderboard)} algos in leaderboard)")

    print(f"\n=== Done ===")
    print(f"  Proven algos:    {len(proven)}")
    print(f"  Tickers written: {written}")
    print(f"  Top BULLISH:     {', '.join(top_bullish)}")
    print(f"  Top BEARISH:     {', '.join(top_bearish)}")

    beats = sum(1 for s in proven if compute_algo_performance(s["snapshots"])["beat_spy"])
    print(f"  Algos beating SPY: {beats} of {len(proven)}")

    if dry_run:
        print("\n  DRY RUN — no files written")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Pre-compute signal verdicts (Polygon.io)")
    parser.add_argument("--min-days", type=int, default=30)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--no-wiki", action="store_true")
    args = parser.parse_args()
    main(min_days=args.min_days, dry_run=args.dry_run, use_wiki=not args.no_wiki)
