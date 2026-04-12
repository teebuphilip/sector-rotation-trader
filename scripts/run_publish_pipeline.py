#!/usr/bin/env python3
"""
Pipeline: triage published ideas, build+seed, and move to completed/failed.
"""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
from pathlib import Path


def _extract_run_date(publish_dir: Path) -> str:
    parts = list(publish_dir.parts)
    if "runs" in parts:
        idx = parts.index("runs")
        if idx + 1 < len(parts):
            return parts[idx + 1]
    return "undated"


def _idea_id_from_path(path: Path) -> str:
    name = path.stem
    if "_" in name:
        name = name.split("_", 1)[1]
    return name.replace("_", "-")


def _run(cmd: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, text=True, capture_output=True)


def _class_name_from_idea_id(idea_id: str) -> str:
    return "".join(w.title() for w in idea_id.replace("-", " ").split()) + "Algo"


def _append_registry_line(module_name: str, class_name: str) -> None:
    path = Path("data/algos_registry_crazy.txt")
    path.parent.mkdir(parents=True, exist_ok=True)
    line = f"{module_name}:{class_name}"
    if path.exists():
        existing = {l.strip() for l in path.read_text(encoding="utf-8").splitlines()}
        if line in existing:
            return
    with path.open("a", encoding="utf-8") as f:
        f.write(line + "\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--publish-dir", default="data/ideas/runs")
    parser.add_argument("--algos-dir", default="crazy/algos")
    parser.add_argument("--completed-dir", default="data/ideas/completed")
    parser.add_argument("--intervention-dir", default="data/ideas/intervention")
    parser.add_argument("--failed-dir", default="data/ideas/failed")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    publish_root = Path(args.publish_dir)
    if not publish_root.exists():
        raise SystemExit(f"Publish dir not found: {publish_root}")

    results = {"completed": 0, "intervention": 0, "failed": 0, "skipped": 0}

    # If user points to runs root, process all publish dirs under it.
    if publish_root.name == "runs":
        publish_dirs = sorted(publish_root.glob("*/publish"))
    else:
        publish_dirs = [publish_root]

    for publish_dir in publish_dirs:
        if not publish_dir.exists():
            continue

        run_date = _extract_run_date(publish_dir)
        completed_dir = Path(args.completed_dir) / run_date
        intervention_dir = Path(args.intervention_dir) / run_date
        failed_dir = Path(args.failed_dir) / run_date
        completed_dir.mkdir(parents=True, exist_ok=True)
        intervention_dir.mkdir(parents=True, exist_ok=True)
        failed_dir.mkdir(parents=True, exist_ok=True)

        for spec_file in sorted(publish_dir.glob("*.md")):
            # Adapter check
            adapter_proc = _run(["python", "scripts/adapter_router.py", "--spec-file", str(spec_file)])
            adapters = []
            if adapter_proc.stdout.strip():
                try:
                    adapters = json.loads(adapter_proc.stdout).get("adapters") or []
                except Exception:
                    adapters = []
            print(f"[adapter] {spec_file} -> {adapters or 'none'}")

            # Skip if already triaged
            if (completed_dir / spec_file.name).exists() or (intervention_dir / spec_file.name).exists() or (failed_dir / spec_file.name).exists():
                results["skipped"] += 1
                print(f"[skip] already triaged: {spec_file}")
                continue

            if adapter_proc.returncode != 0 or not adapters:
                dest = intervention_dir / spec_file.name
                results["intervention"] += 1
                if args.dry_run:
                    print(f"[dry-run] {spec_file} -> {dest}")
                else:
                    shutil.move(str(spec_file), str(dest))
                    print(f"[move] {spec_file} -> {dest}")
                continue

            # Build algorithm
            idea_id = _idea_id_from_path(spec_file)
            algo_path = Path(args.algos_dir) / f"{idea_id.replace('-', '_')}.py"
            if args.dry_run:
                print(f"[dry-run] build {spec_file} -> {algo_path}")
            else:
                build_proc = _run([
                    "scripts/run_structural_build.sh",
                    "--spec-file", str(spec_file),
                    "--output-path", str(algo_path),
                ])
                if build_proc.returncode != 0 or not algo_path.exists() or algo_path.stat().st_size == 0:
                    dest = failed_dir / spec_file.name
                    results["failed"] += 1
                    shutil.move(str(spec_file), str(dest))
                    print(f"[move] {spec_file} -> {dest}")
                    continue
                # Auto-append registry entry on successful build
                _append_registry_line(algo_path.stem, _class_name_from_idea_id(idea_id))

            # Seed algo
            if args.dry_run:
                print(f"[dry-run] seed {algo_path}")
            else:
                seed_proc = _run(["python", "crazy_seed.py", "--algo-file", str(algo_path)])
                if seed_proc.returncode != 0:
                    dest = failed_dir / spec_file.name
                    results["failed"] += 1
                    shutil.move(str(spec_file), str(dest))
                    print(f"[move] {spec_file} -> {dest}")
                    continue

            dest = completed_dir / spec_file.name
            results["completed"] += 1
            if args.dry_run:
                print(f"[dry-run] {spec_file} -> {dest}")
            else:
                shutil.move(str(spec_file), str(dest))
                print(f"[move] {spec_file} -> {dest}")

    print(
        f"[done] completed={results['completed']} intervention={results['intervention']} "
        f"failed={results['failed']} skipped={results['skipped']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
