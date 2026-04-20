#!/usr/bin/env python3
"""Rebuild aggregate crazy outputs from existing per-algo state files.

This script does not call any adapters, does not rebalance, and does not mutate
per-algo state. It is safe to run after a narrow experiment-only crazy run so
public aggregate pages can see newly seeded algos without rerunning the whole
crazy universe.
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from portfolio import compute_analytics, load_state_from
from crazy.algos import get_crazy_algos
from crazy.combined_dashboard import generate_combined_dashboard
from crazy.config import CRAZY_STATE_DIR
from crazy.ledger import write_crazy_ledger


def _summary_for_algo(algo) -> dict:
    state_path = os.path.join(CRAZY_STATE_DIR, f"{algo.algo_id}.json")
    state = load_state_from(state_path)
    analytics = compute_analytics(state)
    snapshots = state.get("daily_snapshots", [])
    equity = snapshots[-1]["equity"] if snapshots else state.get("cash", 100_000)
    meta = state.get("meta", {})

    return {
        "algo_id": algo.algo_id,
        "name": algo.name,
        "equity": float(equity),
        "net_pnl": float(equity) - 100_000,
        "sharpe": analytics.get("sharpe", 0.0),
        "max_drawdown_pct": analytics.get("max_drawdown_pct", 0.0),
        "last_signal": meta.get("signal_label") or meta.get("last_signal") or "HOLD",
        "num_trades": len(state.get("trade_log", [])),
        "sim_start": state.get("sim_start") or (snapshots[0]["date"] if snapshots else None),
    }


def main() -> int:
    summaries = [_summary_for_algo(algo) for algo in get_crazy_algos()]
    generate_combined_dashboard(summaries)
    write_crazy_ledger()
    print(f"Rebuilt crazy combined dashboard and ledger for {len(summaries)} algos")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
