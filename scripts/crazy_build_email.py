#!/usr/bin/env python3
"""
Summarize the Crazy Daily Build Factory run for email/GitHub Actions.
"""
from __future__ import annotations

import json
import os
from pathlib import Path


def _load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def _count_files(path: Path, pattern: str = "*.md") -> int:
    return len(list(path.glob(pattern))) if path.exists() else 0


def _names(path: Path, limit: int = 20) -> list[str]:
    if not path.exists():
        return []
    return [p.stem for p in sorted(path.glob("*.md"))[:limit]]


def _new_algos(run_date: str) -> list[dict]:
    path = Path("data/algos/new_algos.jsonl")
    out = []
    if not path.exists():
        return out
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if not line.strip():
            continue
        try:
            obj = json.loads(line)
        except Exception:
            continue
        if obj.get("date") == run_date:
            out.append(obj)
    return out


def build_report() -> str:
    run_date = os.getenv("RUN_DATE") or os.getenv("AFH_RUN_DATE") or "unknown"
    run_dir = Path("data/ideas/runs") / run_date
    gate = _load_json(run_dir / "publish_gate_reports" / "summary.json")
    factory = _load_json(run_dir / "factory_results" / "summary.json")

    lines = []
    lines.append(f"Crazy Daily Build Factory - {run_date}")
    lines.append("=" * 50)
    lines.append("")

    lines.append("Status:")
    if factory:
        run_ok = factory.get("run_ok", "n/a")
        failed = int(factory.get("failed") or 0)
        completed = int(factory.get("completed") or 0)
        seeded = int(factory.get("seeded") or 0)
        if run_ok is False or completed == 0 or seeded == 0:
            lines.append("  FAILED - no usable signal build, or final run failed")
        elif failed:
            lines.append("  OK WITH PARKED SPECS - usable algos shipped")
        else:
            lines.append("  OK")
    else:
        lines.append("  UNKNOWN - factory summary missing")
    lines.append("")

    lines.append("Gate:")
    if gate:
        counts = gate.get('counts', {}) if isinstance(gate.get('counts'), dict) else {}
        lines.append(f"  Build:        {counts.get('BUILD', gate.get('build', 0))}")
        lines.append(f"  Intervention: {counts.get('INTERVENTION', gate.get('intervention', 0))}")
        lines.append(f"  Reject:       {counts.get('REJECT', gate.get('reject', 0))}")
        cost = gate.get("costs", {}).get("total") if isinstance(gate.get("costs"), dict) else gate.get("total_cost")
        if cost is not None:
            try:
                lines.append(f"  LLM cost:     ${float(cost):.4f}")
            except Exception:
                pass
    else:
        lines.append("  Missing gate summary")
    lines.append("")

    lines.append("Factory:")
    if factory:
        lines.append(f"  Attempted:    {factory.get('attempted', 0)}")
        lines.append(f"  Built:        {factory.get('built', 0)}")
        lines.append(f"  Seeded:       {factory.get('seeded', 0)}")
        lines.append(f"  Completed:    {factory.get('completed', 0)}")
        lines.append(f"  Failed:       {factory.get('failed', 0)}")
        lines.append(f"  Skipped:      {factory.get('skipped', 0)}")
        lines.append(f"  Final run OK: {factory.get('run_ok', 'n/a')}")
    else:
        lines.append("  Missing factory summary")
    lines.append("")

    algos = _new_algos(run_date)
    lines.append(f"New algos recorded: {len(algos)}")
    for item in algos[:30]:
        lines.append(f"  - {item.get('name', item.get('algo_id', '(unknown)'))}")
    if len(algos) > 30:
        lines.append(f"  ... {len(algos) - 30} more")
    lines.append("")

    completed_dir = Path("data/ideas/completed") / run_date
    failed_dir = Path("data/ideas/failed") / run_date
    intervention_dir = run_dir / "intervention"
    lines.append("Spec buckets:")
    lines.append(f"  Completed:    {_count_files(completed_dir)}")
    lines.append(f"  Failed:       {_count_files(failed_dir)}")
    lines.append(f"  Intervention: {_count_files(intervention_dir)}")
    lines.append("")

    failed_names = _names(failed_dir)
    if failed_names:
        lines.append("Failed specs:")
        for name in failed_names:
            lines.append(f"  - {name}")
        lines.append("")

    intervention_names = _names(intervention_dir)
    if intervention_names:
        lines.append("Intervention specs:")
        for name in intervention_names:
            lines.append(f"  - {name}")
        lines.append("")

    lines.append("Links:")
    lines.append(f"  Ideas run: data/ideas/runs/{run_date}")
    lines.append("  Public algos: docs/algos/index.md")
    lines.append("  Signal index: docs/signals/index.json")

    return "\n".join(lines)


def main() -> None:
    print(build_report())


if __name__ == "__main__":
    main()
