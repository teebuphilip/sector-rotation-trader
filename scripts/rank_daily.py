#!/usr/bin/env python3
"""
rank_daily.py
-------------
Unified daily force-rank of all algos (crazy + normal) by two criteria:
  1. Total return (ytd_pct)
  2. Alpha vs SPY (ytd_pct - spy_pct)

Appends one row per algo per day to data/rank_history.csv.
Designed to run after validate_nightly.py in the daily workflow.

Usage:
  python scripts/rank_daily.py
"""
from __future__ import annotations

import csv
import json
import os
import sys
from datetime import date
from pathlib import Path
from typing import Optional

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

CRAZY_STATE_DIR = ROOT / "data" / "crazy" / "state"
NORMAL_STATE_DIR = ROOT / "data" / "normal" / "state"
CSV_PATH = ROOT / "data" / "rank_history.csv"

COLUMNS = [
    "date",
    "rank_return",
    "rank_alpha",
    "algo_id",
    "algo_type",
    "name",
    "ytd_pct",
    "spy_pct",
    "alpha_pct",
    "equity",
    "beat_spy",
    "days_running",
]


def get_spy_ytd() -> float:
    """Fetch SPY YTD return percentage."""
    try:
        import yfinance as yf
        spy = yf.download("SPY", start="2026-01-01", progress=False)
        if spy.empty:
            return 0.0
        first = spy["Close"].iloc[0]
        last = spy["Close"].iloc[-1]
        # Handle Series vs scalar
        if hasattr(first, "iloc"):
            first = first.iloc[0]
        if hasattr(last, "iloc"):
            last = last.iloc[0]
        return ((float(last) / float(first)) - 1) * 100
    except Exception:
        return 0.0


def load_algo_entries() -> list:
    spy_pct = get_spy_ytd()
    print("  SPY YTD: {:+.2f}%".format(spy_pct))

    entries = []
    for state_dir, algo_type in [
        (CRAZY_STATE_DIR, "crazy"),
        (NORMAL_STATE_DIR, "normal"),
    ]:
        if not state_dir.exists():
            continue
        for f in sorted(state_dir.glob("*.json")):
            try:
                data = json.loads(f.read_text())
            except Exception:
                continue

            snaps = data.get("daily_snapshots", [])
            if len(snaps) < 2:
                continue

            algo_id = f.stem
            s0, s1 = snaps[0], snaps[-1]

            eq0 = s0.get("equity", 100_000)
            eq1 = s1.get("equity", 100_000)

            ytd = ((eq1 - eq0) / eq0 * 100) if eq0 else 0.0
            alpha = ytd - spy_pct

            # Best-effort name from meta
            meta = data.get("meta", {})
            name = algo_id
            for key, val in meta.items():
                if isinstance(val, dict) and val.get("name"):
                    name = val["name"]
                    break

            entries.append({
                "algo_id": algo_id,
                "algo_type": algo_type,
                "name": name,
                "ytd_pct": round(ytd, 2),
                "spy_pct": round(spy_pct, 2),
                "alpha_pct": round(alpha, 2),
                "equity": round(eq1, 2),
                "beat_spy": ytd > spy_pct,
                "days_running": len(snaps),
            })

    return entries


def assign_ranks(entries: list) -> list:
    # Rank by total return (descending)
    by_return = sorted(entries, key=lambda e: e["ytd_pct"], reverse=True)
    for i, e in enumerate(by_return, 1):
        e["rank_return"] = i

    # Rank by alpha vs SPY (descending)
    by_alpha = sorted(entries, key=lambda e: e["alpha_pct"], reverse=True)
    for i, e in enumerate(by_alpha, 1):
        e["rank_alpha"] = i

    return by_return


def write_csv(entries: list, as_of: date):
    """Write today's rows, replacing any existing rows for today."""
    today_str = as_of.isoformat()

    # Read existing rows, drop today's
    prior_rows = []
    if CSV_PATH.exists() and CSV_PATH.stat().st_size > 0:
        with open(CSV_PATH) as f:
            reader = csv.DictReader(f)
            prior_rows = [r for r in reader if r.get("date") != today_str]

    # Write all rows back + today's fresh entries
    with open(CSV_PATH, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=COLUMNS)
        writer.writeheader()
        writer.writerows(prior_rows)
        for e in entries:
            row = {"date": today_str}
            for col in COLUMNS:
                if col == "date":
                    continue
                row[col] = e.get(col, "")
            writer.writerow(row)


def main():
    today = date.today()
    print("=== rank_daily.py — {} ===".format(today))

    entries = load_algo_entries()
    if not entries:
        print("  No algo states found. Exiting.")
        return

    ranked = assign_ranks(entries)
    write_csv(ranked, today)

    # Print summary
    beating = sum(1 for e in ranked if e["beat_spy"])
    print("  Algos ranked: {}".format(len(ranked)))
    print("  Beating SPY:  {}/{}".format(beating, len(ranked)))
    print()
    print("  Top 5 by Return:")
    for e in ranked[:5]:
        print("    #{:2d}  {:40s}  {:+7.2f}%".format(
            e["rank_return"], e["name"], e["ytd_pct"]))
    print()
    print("  Top 5 by Alpha vs SPY:")
    by_alpha = sorted(ranked, key=lambda e: e["rank_alpha"])
    for e in by_alpha[:5]:
        print("    #{:2d}  {:40s}  {:+7.2f}%".format(
            e["rank_alpha"], e["name"], e["alpha_pct"]))

    print()
    print("  Appended {} rows to {}".format(len(ranked), CSV_PATH.relative_to(ROOT)))
    print("=== Done ===")


if __name__ == "__main__":
    main()
