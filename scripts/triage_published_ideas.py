#!/usr/bin/env python3
"""
Move published idea specs into completed or intervention buckets.
Completed: adapter exists AND algo file exists.
Intervention: no adapter match (needs new adapter).
"""
from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _idea_id_from_path(path: Path) -> str:
    name = path.stem
    if "_" in name:
        name = name.split("_", 1)[1]
    return name.replace("_", "-")


def _extract_run_date(publish_dir: Path) -> str:
    parts = list(publish_dir.parts)
    if "runs" in parts:
        idx = parts.index("runs")
        if idx + 1 < len(parts):
            return parts[idx + 1]
    return "undated"


def _route_adapter(spec_file: Path) -> list[str]:
    from subprocess import check_output, CalledProcessError

    try:
        raw = check_output(["python", "scripts/adapter_router.py", "--spec-file", str(spec_file)], text=True)
    except CalledProcessError as exc:
        raw = exc.output or ""
    if not raw:
        return []
    data = json.loads(raw)
    return data.get("adapters") or []


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--publish-dir", required=True, help="Path to publish directory of .md specs")
    parser.add_argument("--algos-dir", default="crazy/algos", help="Algo directory to check for completion")
    parser.add_argument("--completed-dir", default="data/ideas/completed", help="Completed bucket base")
    parser.add_argument("--intervention-dir", default="data/ideas/intervention", help="Intervention bucket base")
    parser.add_argument("--pending-dir", default="data/ideas/pending", help="Pending bucket base (adapter ok, algo missing)")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    publish_dir = Path(args.publish_dir)
    if not publish_dir.exists():
        raise SystemExit(f"Publish dir not found: {publish_dir}")

    algos_dir = Path(args.algos_dir)
    completed_base = Path(args.completed_dir)
    intervention_base = Path(args.intervention_dir)
    pending_base = Path(args.pending_dir)
    run_date = _extract_run_date(publish_dir)

    completed_dir = completed_base / run_date
    intervention_dir = intervention_base / run_date
    pending_dir = pending_base / run_date
    completed_dir.mkdir(parents=True, exist_ok=True)
    intervention_dir.mkdir(parents=True, exist_ok=True)
    pending_dir.mkdir(parents=True, exist_ok=True)

    moved = {"completed": 0, "intervention": 0, "pending": 0}

    for spec_file in sorted(publish_dir.glob("*.md")):
        adapters = _route_adapter(spec_file)
        if not adapters:
            dest = intervention_dir / spec_file.name
            moved["intervention"] += 1
        else:
            idea_id = _idea_id_from_path(spec_file)
            algo_file = algos_dir / f"{idea_id.replace('-', '_')}.py"
            if algo_file.exists():
                dest = completed_dir / spec_file.name
                moved["completed"] += 1
            else:
                dest = pending_dir / spec_file.name
                moved["pending"] += 1

        if args.dry_run:
            print(f"[dry-run] {spec_file} -> {dest}")
        else:
            shutil.move(str(spec_file), str(dest))
            print(f"[move] {spec_file} -> {dest}")

    print(f"[done] completed={moved['completed']} intervention={moved['intervention']} pending={moved['pending']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
