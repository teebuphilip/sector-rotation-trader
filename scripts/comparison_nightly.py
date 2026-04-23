"""
Nightly comparator suite.

Runs all baseline comparators against all 11 sector ETFs and writes
docs/comparison/today.json and docs/comparison/history.json.

Each comparator produces a direction (UP/DOWN/NEUTRAL) per ETF.
Algo grading reads whichever comparators exist and scores against all.

Current comparators:
  momentum_5d   — 5-day close-to-close return (free, always-on)
  momentum_20d  — 20-day close-to-close return (free, always-on)

Future comparator candidates:
  kronos        — NeoQuasar/Kronos-mini (requires post-launch server)

Adding a new comparator: implement _run_<name>(ticker, as_of) -> dict
and add it to COMPARATORS below.

Usage:
    python scripts/comparison_nightly.py
    python scripts/comparison_nightly.py --date 2026-04-20
    python scripts/comparison_nightly.py --dry-run
"""

import argparse
import json
from datetime import date, datetime, timedelta
from pathlib import Path

import pandas as pd
import yfinance as yf

ETFS = ["XLK", "XLF", "XLY", "XLP", "XLU", "XLV", "XLI", "XLB", "XLRE", "XLC", "XLE"]
OUT_DIR = Path("docs/comparison")

_LOOKBACK_DAYS = 20   # download window


def _fetch_closes(ticker: str, as_of: date) -> list:
    end = as_of + timedelta(days=1)
    start = as_of - timedelta(days=_LOOKBACK_DAYS * 2)
    try:
        df = yf.download(ticker, start=start.isoformat(), end=end.isoformat(),
                         progress=False, auto_adjust=True)
        if df.empty:
            return []
        closes = df["Close"]
        if isinstance(closes, pd.DataFrame):
            if ticker in closes.columns:
                closes = closes[ticker]
            elif len(closes.columns) == 1:
                closes = closes.iloc[:, 0]
            else:
                return []
        closes = closes.dropna()
        closes = closes[closes.index.normalize() <= str(as_of)]
        return [float(v) for v in closes.values]
    except Exception as exc:
        print(f"[comparison] {ticker}: failed to fetch closes: {exc}")
        return []


def _momentum(closes: list, n: int) -> dict:
    if len(closes) < n + 1:
        return {"direction": "NEUTRAL", "return_pct": None, "confidence": 0.0, "error": "insufficient_data"}
    recent, prior = closes[-1], closes[-(n + 1)]
    if prior == 0:
        return {"direction": "NEUTRAL", "return_pct": None, "confidence": 0.0, "error": "zero_price"}
    ret = (recent - prior) / prior
    direction = "UP" if ret > 0 else ("DOWN" if ret < 0 else "NEUTRAL")
    return {
        "direction": direction,
        "return_pct": round(ret * 100, 3),
        "confidence": round(min(abs(ret) / 0.05, 1.0), 3),
    }


def _run_momentum_5d(ticker: str, as_of: date) -> dict:
    closes = _fetch_closes(ticker, as_of)
    return _momentum(closes, 5)


def _run_momentum_20d(ticker: str, as_of: date) -> dict:
    closes = _fetch_closes(ticker, as_of)
    return _momentum(closes, 20)


# Kronos: placeholder — implement when $6.99/mo server is provisioned
# def _run_kronos(ticker: str, as_of: date) -> dict:
#     raise NotImplementedError("Kronos requires server")


COMPARATORS = {
    "momentum_5d": _run_momentum_5d,
    "momentum_20d": _run_momentum_20d,
    # "kronos": _run_kronos,   # uncomment when server is ready
}


def run(as_of: date, dry_run: bool = False) -> dict:
    results = {}
    for name, fn in COMPARATORS.items():
        etf_signals = {}
        for etf in ETFS:
            etf_signals[etf] = fn(etf, as_of)
        results[name] = etf_signals
        print(f"[comparison] {name} done")

    payload = {
        "date": as_of.isoformat(),
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "comparators": results,
    }

    if dry_run:
        print(json.dumps(payload, indent=2))
        return payload

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    today_path = OUT_DIR / "today.json"
    today_path.write_text(json.dumps(payload, indent=2))

    history_path = OUT_DIR / "history.json"
    if history_path.exists():
        try:
            history = json.loads(history_path.read_text())
        except Exception:
            history = []
    else:
        history = []

    history = [e for e in history if e.get("date") != as_of.isoformat()]
    history.append(payload)
    history.sort(key=lambda e: e.get("date", ""))
    history_path.write_text(json.dumps(history, indent=2))

    print(f"[comparison] {as_of} — wrote {today_path} ({len(COMPARATORS)} comparators, {len(ETFS)} ETFs)")
    return payload


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", default=None, help="YYYY-MM-DD (default: today)")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    as_of = date.fromisoformat(args.date) if args.date else date.today()
    run(as_of, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
