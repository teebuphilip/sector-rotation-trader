#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import json
import shutil
import subprocess
import sys
from pathlib import Path


def _today_iso() -> str:
    return dt.date.today().isoformat()


def _run(cmd: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, text=True, capture_output=True)


def _extract_run_date(path: Path) -> str:
    parts = list(path.parts)
    if "runs" in parts:
        idx = parts.index("runs")
        if idx + 1 < len(parts):
            return parts[idx + 1]
    for bucket in ("failed", "completed", "intervention"):
        if bucket in parts:
            idx = parts.index(bucket)
            if idx + 1 < len(parts):
                return parts[idx + 1]
    return _today_iso()


def _idea_id_from_path(path: Path) -> str:
    name = path.stem
    if "_" in name:
        name = name.split("_", 1)[1]
    return name.replace("_", "-")


def _class_name_from_idea_id(idea_id: str) -> str:
    return "".join(w.title() for w in idea_id.replace("-", " ").split()) + "Algo"


def _append_registry_line(module_name: str, class_name: str, dry_run: bool) -> None:
    path = Path("data/algos_registry_crazy.txt")
    line = f"{module_name}:{class_name}"
    existing = set(path.read_text(encoding="utf-8").splitlines()) if path.exists() else set()
    if line in existing:
        return
    if dry_run:
        print(f"[dry-run] registry append {line}")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(line + "\n")


def _publish_dirs(root: Path, date: str | None) -> list[Path]:
    if root.name == "publish":
        return [root]
    if root.name in {"build", "intervention", "reject"}:
        return [root]
    if root.exists() and any(root.glob("*.md")):
        return [root]
    if date:
        candidate = root / date / "publish" if root.name == "runs" else root / "publish"
        return [candidate] if candidate.exists() else []
    if root.name == "runs":
        return sorted(root.glob("*/publish"))
    return [root]


def _move(src: Path, dest_dir: Path, dry_run: bool) -> Path:
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / src.name
    if src.resolve() == dest.resolve():
        print(f"[move] already in place: {src}")
        return dest
    if dry_run:
        print(f"[dry-run] move {src} -> {dest}")
        return dest
    shutil.move(str(src), str(dest))
    print(f"[move] {src} -> {dest}")
    return dest


def _write_result(path: Path, result: dict, dry_run: bool) -> None:
    if dry_run:
        print(f"[dry-run] result {path}: {result['status']}")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(result, indent=2, sort_keys=True), encoding="utf-8")


def _completed_or_triaged(
    spec_file: Path,
    run_date: str,
    retry_failed: bool = False,
    retry_intervention: bool = False,
) -> bool:
    bases = ["data/ideas/completed"]
    if not retry_intervention:
        bases.append("data/ideas/intervention")
    if not retry_failed:
        bases.append("data/ideas/failed")
    for base in bases:
        if (Path(base) / run_date / spec_file.name).exists():
            return True
    return False


def _print_proc(label: str, proc: subprocess.CompletedProcess, verbose: bool) -> None:
    if not verbose:
        return
    if proc.stdout:
        print(f"[{label}] stdout:\n{proc.stdout}", end="" if proc.stdout.endswith("\n") else "\n")
    if proc.stderr:
        print(f"[{label}] stderr:\n{proc.stderr}", end="" if proc.stderr.endswith("\n") else "\n")


def _failure_excerpt(proc: subprocess.CompletedProcess) -> str:
    text = (proc.stderr.strip() or proc.stdout.strip() or "command_failed").strip()
    return text[-3000:]


def _used_deterministic_fallback(proc: subprocess.CompletedProcess) -> bool:
    combined = f"{proc.stdout}\n{proc.stderr}"
    return (
        "[done] deterministic fallback complete" in combined
        or "[step] patch (deterministic fallback)" in combined
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Full crazy idea -> algo factory with hard gates.")
    parser.add_argument("--date", default=_today_iso())
    parser.add_argument("--publish-root", default="data/ideas/runs")
    parser.add_argument("--algos-dir", default="crazy/algos")
    parser.add_argument("--limit", type=int, default=0, help="Max publish specs to attempt after adapter triage. 0 = no limit")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--skip-generate", action="store_true", help="Use existing publish specs instead of generating high-action ideas first")
    parser.add_argument("--build-only", action="store_true", help="Build algos but do not seed/run/move to completed")
    parser.add_argument("--seed-only", action="store_true", help="Seed existing built algos for publish specs; do not build")
    parser.add_argument("--template-build", action="store_true", help="Use deterministic adapter templates instead of LLM structural build")
    parser.add_argument("--skip-run", action="store_true", help="Skip final crazy_run/precompute after seeding")
    parser.add_argument("--max-failures", type=int, default=5)
    parser.add_argument("--retry-failed", action="store_true", help="Do not skip specs already present in data/ideas/failed/<date>")
    parser.add_argument("--retry-intervention", action="store_true", help="Do not skip specs already present in data/ideas/intervention/<date>")
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()

    try:
        dt.date.fromisoformat(args.date)
    except ValueError:
        print("Invalid --date, expected YYYY-MM-DD", file=sys.stderr)
        return 2

    results_root = Path("data/ideas/runs") / args.date / "factory_results"
    summary = {
        "date": args.date,
        "dry_run": args.dry_run,
        "generated": False,
        "completed": 0,
        "intervention": 0,
        "failed": 0,
        "skipped": 0,
        "built": 0,
        "seeded": 0,
        "attempted": 0,
    }

    if not args.skip_generate and not args.seed_only:
        cmd = ["python", "scripts/crazy_generate_high_action_ideas.py", "--date", args.date]
        if args.dry_run:
            print("[dry-run] " + " ".join(cmd))
        else:
            print("[step] generate high-action ideas")
            proc = _run(cmd)
            _print_proc("generate", proc, True)
            if proc.returncode != 0:
                print("[error] generation failed", file=sys.stderr)
                return proc.returncode
            summary["generated"] = True

    publish_dirs = _publish_dirs(Path(args.publish_root), args.date)
    specs = []
    for publish_dir in publish_dirs:
        specs.extend(sorted(publish_dir.glob("*.md")))
    if args.limit:
        specs = specs[: args.limit]

    print(f"[run] date={args.date} specs={len(specs)} dry_run={args.dry_run}")

    failures = 0
    built_algo_files: list[Path] = []

    for spec_file in specs:
        run_date = _extract_run_date(spec_file)
        idea_id = _idea_id_from_path(spec_file)
        module_name = idea_id.replace("-", "_")
        algo_path = Path(args.algos_dir) / f"{module_name}.py"
        result_path = results_root / f"{idea_id}.json"
        result = {
            "idea_id": idea_id,
            "spec_file": str(spec_file),
            "algo_file": str(algo_path),
            "status": "started",
            "adapter": None,
            "seeded": False,
            "built": False,
            "run_ok": None,
            "errors": [],
        }

        print(f"[spec] {spec_file}")

        if _completed_or_triaged(
            spec_file,
            run_date,
            retry_failed=args.retry_failed,
            retry_intervention=args.retry_intervention,
        ):
            result["status"] = "skipped_already_triaged"
            summary["skipped"] += 1
            print(f"[skip] already triaged: {spec_file}")
            _write_result(result_path, result, args.dry_run)
            continue

        adapter_proc = _run(["python", "scripts/adapter_router.py", "--spec-file", str(spec_file)])
        _print_proc("adapter", adapter_proc, args.verbose)
        adapters = []
        if adapter_proc.stdout.strip():
            try:
                adapters = json.loads(adapter_proc.stdout).get("adapters") or []
            except Exception as exc:
                result["errors"].append(f"adapter_json_error: {exc}")
        result["adapter"] = adapters[0] if adapters else None
        print(f"[adapter] {idea_id} -> {adapters or 'none'}")

        if adapter_proc.returncode != 0 or not adapters:
            result["status"] = "intervention"
            result["errors"].append(adapter_proc.stderr.strip() or "no_adapter_match")
            summary["intervention"] += 1
            _move(spec_file, Path("data/ideas/intervention") / run_date, args.dry_run)
            _write_result(result_path, result, args.dry_run)
            continue

        summary["attempted"] += 1

        if not args.seed_only:
            if args.dry_run:
                print(f"[dry-run] build {spec_file} -> {algo_path}")
                result["built"] = True
                summary["built"] += 1
            else:
                if args.template_build:
                    build_proc = _run([
                        "python",
                        "scripts/build_template_algo.py",
                        "--spec-file", str(spec_file),
                        "--output-path", str(algo_path),
                        "--adapter", adapters[0],
                        "--report", str(results_root / f"{idea_id}_template_build.json"),
                    ])
                else:
                    build_proc = _run([
                        "scripts/run_structural_build.sh",
                        "--spec-file", str(spec_file),
                        "--output-path", str(algo_path),
                    ])
                _print_proc("build", build_proc, args.verbose)
                if build_proc.returncode != 0 or not algo_path.exists() or algo_path.stat().st_size == 0:
                    result["status"] = "failed_build"
                    excerpt = _failure_excerpt(build_proc)
                    result["errors"].append(excerpt)
                    summary["failed"] += 1
                    failures += 1
                    print(f"[error] build failed for {idea_id}")
                    print(excerpt)
                    _move(spec_file, Path("data/ideas/failed") / run_date, args.dry_run)
                    _write_result(result_path, result, args.dry_run)
                    if failures >= args.max_failures:
                        print(f"[stop] max failures reached: {failures}")
                        break
                    continue
                if _used_deterministic_fallback(build_proc):
                    result["status"] = "intervention_fallback_used"
                    result["errors"].append(
                        "deterministic_fallback_used_after_llm_validation_failure"
                    )
                    summary["intervention"] += 1
                    print(f"[intervention] fallback used for {idea_id}; not seeding")
                    _move(spec_file, Path("data/ideas/intervention") / run_date, args.dry_run)
                    _write_result(result_path, result, args.dry_run)
                    continue
                result["built"] = True
                summary["built"] += 1
            built_algo_files.append(algo_path)

        if args.build_only:
            result["status"] = "built"
            _write_result(result_path, result, args.dry_run)
            continue

        if args.dry_run:
            print(f"[dry-run] seed {algo_path}")
            result["seeded"] = True
            summary["seeded"] += 1
        else:
            seed_proc = _run(["python", "crazy_seed.py", "--algo-file", str(algo_path)])
            _print_proc("seed", seed_proc, args.verbose)
            seed_failed = (
                seed_proc.returncode != 0
                or "No matching crazy algos found to seed" in seed_proc.stdout
                or "failed to load" in seed_proc.stdout
            )
            if seed_failed:
                result["status"] = "failed_seed"
                result["errors"].append(seed_proc.stderr.strip() or seed_proc.stdout[-2000:] or "seed_failed")
                summary["failed"] += 1
                failures += 1
                _move(spec_file, Path("data/ideas/failed") / run_date, args.dry_run)
                _write_result(result_path, result, args.dry_run)
                if failures >= args.max_failures:
                    print(f"[stop] max failures reached: {failures}")
                    break
                continue
            result["seeded"] = True
            summary["seeded"] += 1

        result["status"] = "completed_pending_run" if args.skip_run else "completed"
        summary["completed"] += 1
        if not args.seed_only:
            _append_registry_line(module_name, _class_name_from_idea_id(idea_id), args.dry_run)
        _move(spec_file, Path("data/ideas/completed") / run_date, args.dry_run)
        _write_result(result_path, result, args.dry_run)

    if not args.build_only and not args.skip_run and summary["seeded"] > 0:
        if args.dry_run:
            print("[dry-run] python crazy_run.py")
            print("[dry-run] python precompute_signals.py")
            print("[dry-run] python scripts/update_algos_index.py")
            print("[dry-run] python scripts/build_product_index.py")
            print("[dry-run] python scripts/build_public_artifacts.py")
        else:
            print("[step] run crazy pipeline once")
            run_proc = _run(["python", "crazy_run.py"])
            _print_proc("crazy_run", run_proc, True)
            run_ok = run_proc.returncode == 0
            print("[step] precompute signals once")
            pre_proc = _run(["python", "precompute_signals.py"])
            _print_proc("precompute", pre_proc, True)
            run_ok = run_ok and pre_proc.returncode == 0
            print("[step] rebuild product/public artifacts")
            for label, cmd in [
                ("update_algos_index", ["python", "scripts/update_algos_index.py"]),
                ("build_product_index", ["python", "scripts/build_product_index.py"]),
                ("build_public_artifacts", ["python", "scripts/build_public_artifacts.py"]),
            ]:
                proc = _run(cmd)
                _print_proc(label, proc, True)
                run_ok = run_ok and proc.returncode == 0
            summary["run_ok"] = run_ok
            if not run_ok:
                summary["failed"] += 1
                print("[warn] final run/precompute failed")

    summary_path = results_root / "summary.json"
    _write_result(summary_path, {"status": "summary", **summary}, args.dry_run)
    print(
        f"[done] completed={summary['completed']} intervention={summary['intervention']} "
        f"failed={summary['failed']} skipped={summary['skipped']} built={summary['built']} seeded={summary['seeded']}"
    )
    return 0 if summary["failed"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
