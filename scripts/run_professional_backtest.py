#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from backtest.engine import run_backtest
from backtest.report import write_master, write_result
from crazy.algos import get_crazy_algos
from normal.algos import get_normal_algos


def _norm(value: str) -> str:
    return value.strip().lower().replace("_", "-")


def _filter(algos, wanted):
    if not wanted:
        return list(algos)
    keys = {_norm(v) for v in wanted}
    out = []
    for algo in algos:
        aliases = {_norm(algo.algo_id), _norm(algo.name), _norm(algo.__class__.__name__)}
        if aliases & keys:
            out.append(algo)
    return out


def _load_algos(args):
    pairs = []
    if args.family in ("normal", "all"):
        pairs.extend(("normal", a) for a in get_normal_algos())
    if args.family in ("crazy", "all"):
        pairs.extend(("crazy", a) for a in get_crazy_algos())
    if args.algo_id:
        wanted = {_norm(v) for v in args.algo_id}
        pairs = [
            (family, algo) for family, algo in pairs
            if {_norm(algo.algo_id), _norm(algo.name), _norm(algo.__class__.__name__)} & wanted
        ]
    return pairs


def main() -> int:
    parser = argparse.ArgumentParser(description="Professional backtest V1: no-lookahead sector ETF price backtests.")
    parser.add_argument("--family", choices=["normal", "crazy", "all"], default="all")
    parser.add_argument("--algo-id", action="append", help="Run one algo id/name/class. Repeatable.")
    parser.add_argument("--start", default="2021-01-01")
    parser.add_argument("--end", default=date.today().isoformat())
    parser.add_argument("--slippage-bps", type=float, default=5.0)
    parser.add_argument("--output-root", default="reports/backtests")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    pairs = _load_algos(args)
    if args.limit:
        pairs = pairs[: args.limit]
    if not pairs:
        print("No matching algos found", file=sys.stderr)
        return 2

    run_date = date.today().isoformat()
    root = Path(args.output_root)
    written = []
    print(f"[run] algos={len(pairs)} family={args.family} start={args.start} end={args.end} slippage_bps={args.slippage_bps}")

    for idx, (family, algo) in enumerate(pairs, 1):
        print(f"[{idx}/{len(pairs)}] {family}:{algo.algo_id} {algo.name}")
        if args.dry_run:
            continue
        result = run_backtest(algo, family, args.start, args.end, args.slippage_bps)
        payload = write_result(result, root / "algos", run_date)
        written.append(payload)
        m = payload.get("metrics") or {}
        print(
            f"  -> {payload['status']} alpha={m.get('alpha_vs_spy_pct', '')} "
            f"trades={m.get('trade_count', '')} reason={payload['reason']}"
        )

    if not args.dry_run:
        write_master(written, root, run_date, args.start, args.end, args.slippage_bps)
        counts = {}
        for row in written:
            counts[row["status"]] = counts.get(row["status"], 0) + 1
        print(f"[done] wrote {root}/latest.json and latest.md counts={json.dumps(counts, sort_keys=True)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
