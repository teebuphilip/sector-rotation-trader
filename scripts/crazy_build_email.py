#!/usr/bin/env python3
"""
Summarize the Crazy Daily Build Factory run for email/GitHub Actions.

This intentionally reads the current run artifacts instead of assuming one JSON
shape. The idea generator has changed schemas over time; the email should still
answer: how many ideas came in, how many survived each gate, and what shipped.
"""
from __future__ import annotations

import json
import os
from collections import Counter
from pathlib import Path
from typing import Any


def _load_json(path: Path) -> Any:
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None


def _load_jsonl(path: Path) -> list[dict]:
    rows: list[dict] = []
    if not path.exists():
        return rows
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        s = line.strip()
        if not s:
            continue
        try:
            obj = json.loads(s)
        except Exception:
            continue
        if isinstance(obj, dict):
            rows.append(obj)
    return rows


def _count_files(path: Path, pattern: str = "*.md") -> int:
    return len(list(path.glob(pattern))) if path.exists() else 0


def _names(path: Path, limit: int = 20) -> list[str]:
    if not path.exists():
        return []
    return [p.stem for p in sorted(path.glob("*.md"))[:limit]]


def _idea_id(obj: dict, fallback: str = "(unknown)") -> str:
    if obj.get("idea_id"):
        return str(obj["idea_id"])
    if obj.get("id"):
        return str(obj["id"])
    if obj.get("idea"):
        return str(obj["idea"]).lower().replace(" ", "-")[:80]
    if obj.get("title"):
        return str(obj["title"]).lower().replace(" ", "-")[:80]
    return fallback


def _title(obj: dict) -> str:
    return str(obj.get("title") or obj.get("idea") or obj.get("name") or _idea_id(obj))


def _provider_counts(run_dir: Path, subdir: str) -> dict[str, int]:
    out: dict[str, int] = {}
    date = run_dir.name
    for src in ("chatgpt", "claude"):
        out[src] = len(_load_jsonl(run_dir / subdir / f"{src}_{date}.jsonl"))
    return out


def _score_count(run_dir: Path) -> int:
    obj = _load_json(run_dir / "score.json")
    if isinstance(obj, list):
        return len(obj)
    if isinstance(obj, dict):
        for key in ("ideas", "scores", "items", "results"):
            if isinstance(obj.get(key), list):
                return len(obj[key])
    return 0


def _publish_count(run_dir: Path) -> int:
    return _count_files(run_dir / "publish")


def _gate_counts(gate: dict | None) -> dict[str, int]:
    if not isinstance(gate, dict):
        return {"BUILD": 0, "INTERVENTION": 0, "REJECT": 0}
    counts = gate.get("counts")
    if isinstance(counts, dict):
        return {
            "BUILD": int(counts.get("BUILD") or 0),
            "INTERVENTION": int(counts.get("INTERVENTION") or 0),
            "REJECT": int(counts.get("REJECT") or 0),
        }
    files = gate.get("files")
    counter: Counter[str] = Counter()
    if isinstance(files, list):
        for item in files:
            if isinstance(item, dict):
                counter[str(item.get("decision") or "UNKNOWN").upper()] += 1
    return {
        "BUILD": counter.get("BUILD", int(gate.get("build") or 0)),
        "INTERVENTION": counter.get("INTERVENTION", int(gate.get("intervention") or 0)),
        "REJECT": counter.get("REJECT", int(gate.get("reject") or 0)),
    }


def _new_algos_from_registry(run_date: str) -> list[dict]:
    path = Path("data/algos/new_algos.jsonl")
    out: list[dict] = []
    if not path.exists():
        return out
    for obj in _load_jsonl(path):
        if obj.get("date") == run_date:
            out.append(obj)
    return out


def _completed_specs(run_date: str) -> list[str]:
    return _names(Path("data/ideas/completed") / run_date, limit=200)


def _factory_built_names(run_dir: Path) -> list[str]:
    root = run_dir / "factory_results"
    if not root.exists():
        return []
    names: list[str] = []
    for path in sorted(root.glob("*.json")):
        if path.name.endswith("_template_build.json") or path.name == "summary.json":
            continue
        obj = _load_json(path)
        if isinstance(obj, dict) and obj.get("built"):
            names.append(str(obj.get("idea_id") or path.stem))
    return names


def _top_ideas(run_dir: Path, limit: int = 10) -> list[str]:
    obj = _load_json(run_dir / "score.json")
    items: list[dict] = []
    if isinstance(obj, list):
        items = [x for x in obj if isinstance(x, dict)]
    elif isinstance(obj, dict):
        for key in ("ideas", "scores", "items", "results"):
            if isinstance(obj.get(key), list):
                items = [x for x in obj[key] if isinstance(x, dict)]
                break
    out = []
    for item in items[:limit]:
        score = item.get("score")
        suffix = f" score={score}" if score is not None else ""
        out.append(f"{_idea_id(item)} ({item.get('source', '?')}){suffix}")
    return out


def build_report() -> str:
    run_date = os.getenv("RUN_DATE") or os.getenv("AFH_RUN_DATE") or "unknown"
    run_dir = Path("data/ideas/runs") / run_date
    gate = _load_json(run_dir / "publish_gate_reports" / "summary.json")
    factory = _load_json(run_dir / "factory_results" / "summary.json")
    factory = factory if isinstance(factory, dict) else {}

    raw_counts = _provider_counts(run_dir, "raw")
    filtered_counts = _provider_counts(run_dir, "filtered")
    rejected_counts = _provider_counts(run_dir, "rejected")
    gate_counts = _gate_counts(gate if isinstance(gate, dict) else None)

    lines: list[str] = []
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

    lines.append("Idea Generation:")
    lines.append(f"  Raw ChatGPT:       {raw_counts.get('chatgpt', 0)}")
    lines.append(f"  Raw Claude:        {raw_counts.get('claude', 0)}")
    lines.append(f"  Raw Total:         {sum(raw_counts.values())}")
    lines.append(f"  Schema kept:       {sum(filtered_counts.values())}")
    lines.append(f"  Schema rejected:   {sum(rejected_counts.values())}")
    lines.append(f"  Scored:            {_score_count(run_dir)}")
    lines.append(f"  Published specs:   {_publish_count(run_dir)}")
    lines.append("")

    top = _top_ideas(run_dir)
    if top:
        lines.append("Top scored ideas:")
        for item in top:
            lines.append(f"  - {item}")
        lines.append("")

    lines.append("Final Publish Gate:")
    lines.append(f"  BUILD:        {gate_counts['BUILD']}")
    lines.append(f"  INTERVENTION: {gate_counts['INTERVENTION']}")
    lines.append(f"  REJECT:       {gate_counts['REJECT']}")
    if isinstance(gate, dict):
        cost = gate.get("costs", {}).get("total") if isinstance(gate.get("costs"), dict) else gate.get("total_cost")
        if cost is not None:
            try:
                lines.append(f"  LLM cost:     ${float(cost):.4f}")
            except Exception:
                pass
    lines.append("")

    completed_dir = Path("data/ideas/completed") / run_date
    failed_dir = Path("data/ideas/failed") / run_date
    intervention_dir = run_dir / "intervention"

    backtest = factory.get("backtest") if isinstance(factory, dict) else None
    lines.append("Build Factory:")
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
    if isinstance(backtest, dict):
        counts = backtest.get("counts") or {}
        lines.append("Backtest / Classification:")
        lines.append(f"  Reviewed:     {backtest.get('reviewed', 0)}")
        for key in sorted(counts):
            lines.append(f"  {key}: {counts[key]}")
        if backtest.get("output_root"):
            lines.append(f"  Output dir:   {backtest.get('output_root')}")
        lines.append("")

    lines.append("Spec Buckets:")
    lines.append(f"  Completed:    {_count_files(completed_dir)}")
    lines.append(f"  Failed:       {_count_files(failed_dir)}")
    lines.append(f"  Intervention: {_count_files(intervention_dir)}")
    lines.append("")

    shipped = _completed_specs(run_date) or _factory_built_names(run_dir)
    lines.append(f"Shipped algos/specs: {len(shipped)}")
    for name in shipped[:30]:
        lines.append(f"  - {name}")
    if len(shipped) > 30:
        lines.append(f"  ... {len(shipped) - 30} more")
    lines.append("")

    registry_algos = _new_algos_from_registry(run_date)
    if registry_algos:
        lines.append(f"New algos registry entries: {len(registry_algos)}")
        for item in registry_algos[:30]:
            lines.append(f"  - {item.get('name', item.get('algo_id', '(unknown)'))}")
        if len(registry_algos) > 30:
            lines.append(f"  ... {len(registry_algos) - 30} more")
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
