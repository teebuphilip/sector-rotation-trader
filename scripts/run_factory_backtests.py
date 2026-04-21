#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from backtest.engine import run_backtest
from backtest.report import write_result, write_master
from crazy.algos import get_crazy_algos


def _load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _norm(value: str) -> str:
    return value.strip().lower().replace("_", "-")


def _seeded_ids(factory_root: Path) -> list[str]:
    ids: list[str] = []
    for path in sorted(factory_root.glob("*.json")):
        if path.name == "summary.json" or path.name.endswith("_template_build.json"):
            continue
        obj = _load_json(path)
        if obj.get("seeded") and obj.get("idea_id"):
            ids.append(str(obj["idea_id"]))
    return ids


def _find_algos(ids: list[str]):
    wanted = {_norm(v) for v in ids}
    out = []
    for algo in get_crazy_algos():
        aliases = {_norm(algo.algo_id), _norm(algo.name), _norm(algo.__class__.__name__)}
        if aliases & wanted:
            out.append(algo)
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description="Run V1 backtests for newly seeded factory algos.")
    parser.add_argument("--date", default=date.today().isoformat())
    parser.add_argument("--start", default="2024-01-01")
    parser.add_argument("--end", default=None)
    parser.add_argument("--slippage-bps", type=float, default=5.0)
    parser.add_argument("--results-root", default="data/ideas/runs")
    parser.add_argument("--output-root", default="reports/backtests/factory")
    args = parser.parse_args()

    end = args.end or args.date
    run_dir = Path(args.results_root) / args.date
    factory_root = run_dir / "factory_results"
    summary_path = factory_root / "summary.json"
    if not factory_root.exists() or not summary_path.exists():
        print(f"Factory results missing for {args.date}", file=sys.stderr)
        return 2

    seeded_ids = _seeded_ids(factory_root)
    print(f"[run] date={args.date} seeded_ids={len(seeded_ids)}")
    if not seeded_ids:
        summary = _load_json(summary_path)
        summary["backtest"] = {"reviewed": 0, "counts": {}, "output_root": str(Path(args.output_root) / args.date)}
        summary_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
        print("[done] no seeded algos to backtest")
        return 0

    algos = _find_algos(seeded_ids)
    by_id = {algo.algo_id: algo for algo in algos}
    output_root = Path(args.output_root) / args.date
    output_root.mkdir(parents=True, exist_ok=True)

    written = []
    counter: Counter[str] = Counter()
    for algo_id in seeded_ids:
        algo = by_id.get(algo_id)
        if not algo:
            counter["MISSING_ALGO"] += 1
            continue
        print(f"[backtest] {algo.algo_id} {algo.name}")
        result = run_backtest(algo, "crazy", args.start, end, args.slippage_bps)
        payload = write_result(result, output_root / "algos", args.date)
        written.append(payload)
        counter[payload["status"]] += 1

        result_path = factory_root / f"{algo_id}.json"
        if result_path.exists():
            obj = _load_json(result_path)
            metrics = payload.get("metrics") or {}
            obj["backtest_status"] = payload["status"]
            obj["backtest_reason"] = payload["reason"]
            obj["backtest_alpha_vs_spy_pct"] = metrics.get("alpha_vs_spy_pct")
            obj["backtest_trade_count"] = metrics.get("trade_count")
            obj["backtest_report_dir"] = str(output_root / "algos" / payload["family"] / payload["algo_id"])
            result_path.write_text(json.dumps(obj, indent=2), encoding="utf-8")

    write_master(written, output_root, args.date, args.start, end, args.slippage_bps)

    summary = _load_json(summary_path)
    summary["backtest"] = {
        "reviewed": len(written),
        "counts": dict(counter),
        "output_root": str(output_root),
        "start": args.start,
        "end": end,
        "slippage_bps": args.slippage_bps,
    }
    summary_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(f"[done] reviewed={len(written)} counts={json.dumps(dict(counter), sort_keys=True)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
