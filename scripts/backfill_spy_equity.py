#!/usr/bin/env python3
"""
Backfill spy_equity in daily snapshots for crazy/normal state files.
"""
from __future__ import annotations

import json
import sys
from datetime import datetime
from typing import Optional
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scanner_polygon import safe_download


def _load_states(base: Path) -> list[Path]:
    if not base.exists():
        return []
    return sorted(base.glob("*.json"))


def _parse_date(s: str) -> Optional[pd.Timestamp]:
    try:
        return pd.to_datetime(s)
    except Exception:
        return None


def _backfill_state(path: Path, spy_series: pd.Series) -> bool:
    data = json.loads(path.read_text(encoding="utf-8"))
    snaps = data.get("daily_snapshots", [])
    if not snaps:
        return False

    first_date = _parse_date(snaps[0].get("date", ""))
    if first_date is None:
        return False

    if first_date not in spy_series.index:
        # Use last available before first_date
        spy_start = spy_series.loc[spy_series.index <= first_date].iloc[-1]
    else:
        spy_start = spy_series.loc[first_date]

    start_equity = snaps[0].get("equity", 100_000) or 100_000

    changed = False
    for snap in snaps:
        d = _parse_date(snap.get("date", ""))
        if d is None:
            continue
        if d not in spy_series.index:
            series = spy_series.loc[spy_series.index <= d]
            if series.empty:
                continue
            spy_price = series.iloc[-1]
        else:
            spy_price = spy_series.loc[d]

        spy_equity = float(start_equity) * (float(spy_price) / float(spy_start))
        if snap.get("spy_equity") != spy_equity:
            snap["spy_equity"] = spy_equity
            changed = True

    if changed:
        path.write_text(json.dumps(data, indent=2, default=str), encoding="utf-8")
    return changed


def main() -> int:
    crazy_dir = Path("data/crazy/state")
    normal_dir = Path("data/normal/state")

    paths = _load_states(crazy_dir) + _load_states(normal_dir)
    if not paths:
        print("No state files found.")
        return 0

    # Determine overall date range
    all_dates = []
    for p in paths:
        data = json.loads(p.read_text(encoding="utf-8"))
        for snap in data.get("daily_snapshots", []):
            d = _parse_date(snap.get("date", ""))
            if d is not None:
                all_dates.append(d)

    if not all_dates:
        print("No snapshot dates found.")
        return 0

    start = min(all_dates)
    end = max(all_dates)

    # Download SPY prices
    period_days = max((end - start).days + 30, 60)
    period = f"{period_days}d"
    raw = safe_download(["SPY"], period=period)
    if raw.empty:
        print("Failed to download SPY prices.")
        return 1

    prices = raw["Close"] if "Close" in raw.columns else raw
    spy_series = prices["SPY"].dropna()
    if spy_series.empty:
        print("No SPY prices available.")
        return 1

    changed = 0
    for p in paths:
        if _backfill_state(p, spy_series):
            changed += 1

    print(f"Backfilled spy_equity for {changed} state files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
