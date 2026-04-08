#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
from datetime import datetime, timedelta
from pathlib import Path


def _latest_run_dir(base: Path) -> Path | None:
    if not base.exists():
        return None
    runs = [p for p in base.iterdir() if p.is_dir()]
    if not runs:
        return None
    runs.sort()
    return runs[-1]


def _load_json(path: Path) -> dict | list | None:
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text())
    except Exception:
        return None


def _count_jsonl(path: Path) -> int:
    if not path.exists():
        return 0
    return len([line for line in path.read_text().splitlines() if line.strip()])


def _state_last_run(path: Path) -> str:
    state = _load_json(path)
    if not isinstance(state, dict):
        return "missing"
    return state.get("last_run") or "missing"


def _stale(last_run: str, days: int = 2) -> bool:
    try:
        dt = datetime.fromisoformat(last_run)
    except Exception:
        return True
    return (datetime.utcnow().date() - dt.date()) > timedelta(days=days)


def _collect_algo_status() -> list[dict]:
    entries = []

    # Baseline
    base_path = Path("state.json")
    if base_path.exists():
        last = _state_last_run(base_path)
        entries.append({"name": "NRWise Acceleration", "path": str(base_path), "last_run": last})

    # Normal
    normal_dir = Path("data/normal/state")
    if normal_dir.exists():
        for p in sorted(normal_dir.glob("*.json")):
            state = _load_json(p)
            meta = (state or {}).get("meta", {}).get(p.stem, {}) if isinstance(state, dict) else {}
            name = meta.get("name") or p.stem
            last = state.get("last_run") if isinstance(state, dict) else "missing"
            entries.append({"name": name, "path": str(p), "last_run": last})

    # Crazy
    crazy_dir = Path("data/crazy/state")
    if crazy_dir.exists():
        for p in sorted(crazy_dir.glob("*.json")):
            state = _load_json(p)
            meta = (state or {}).get("meta", {}).get(p.stem, {}) if isinstance(state, dict) else {}
            name = meta.get("name") or p.stem
            last = state.get("last_run") if isinstance(state, dict) else "missing"
            entries.append({"name": name, "path": str(p), "last_run": last})

    return entries


def _collect_blocked_ideas(run_dir: Path) -> list[str]:
    blocked = []
    raw_dir = run_dir / "raw"
    for src in ["chatgpt", "claude"]:
        path = raw_dir / f"{src}_{run_dir.name}.jsonl"
        if not path.exists():
            continue
        for line in path.read_text().splitlines():
            s = line.strip()
            if not s:
                continue
            try:
                idea = json.loads(s)
            except Exception:
                continue
            keys = idea.get("required_keys", [])
            if keys:
                blocked.append(f"{idea.get('idea_id','(unknown)')} ({src}) -> {', '.join(keys)}")
    return blocked


def _build_report() -> str:
    lines = []
    now = datetime.utcnow().strftime("%Y-%m-%d")
    lines.append(f"Crazy Daily Stats — {now}")
    lines.append("")

    # Idea run
    run_date = os.getenv("AFH_RUN_DATE") or now
    ideas_base = Path("data/ideas/runs")
    latest_run = ideas_base / run_date
    if not latest_run.exists():
        latest_run = _latest_run_dir(ideas_base)
    if latest_run:
        run_date = latest_run.name
        lines.append(f"Latest idea run: {run_date}")
        lines.append(f"- ChatGPT ideas: {_count_jsonl(latest_run / 'raw' / f'chatgpt_{run_date}.jsonl')}")
        lines.append(f"- Claude ideas:  {_count_jsonl(latest_run / 'raw' / f'claude_{run_date}.jsonl')}")
        score = _load_json(latest_run / "score.json")
        lines.append(f"- Score file: {'present' if score is not None else 'missing'}")
        err_dir = latest_run / "errors"
        if err_dir.exists():
            err_files = sorted([p.name for p in err_dir.glob("*.txt")])
            if err_files:
                lines.append("- Generator errors:")
                for name in err_files:
                    lines.append(f"  - {name}")
            else:
                lines.append("- Generator errors: none")
        else:
            lines.append("- Generator errors: none")
        blocked = _collect_blocked_ideas(latest_run)
        if blocked:
            lines.append("- Blocked ideas (missing keys):")
            for b in blocked:
                lines.append(f"  - {b}")
        else:
            lines.append("- Blocked ideas: none")
    else:
        lines.append("Latest idea run: missing")

    lines.append("")

    # Normal idea run (weekly)
    normal_base = Path("data/normal_ideas/runs")
    normal_run = _latest_run_dir(normal_base)
    if normal_run:
        n_date = normal_run.name
        lines.append(f"Latest normal idea run: {n_date}")
        lines.append(f"- ChatGPT ideas: {_count_jsonl(normal_run / 'raw' / f'chatgpt_{n_date}.jsonl')}")
        lines.append(f"- Claude ideas:  {_count_jsonl(normal_run / 'raw' / f'claude_{n_date}.jsonl')}")
        n_score = _load_json(normal_run / "score.json")
        lines.append(f"- Score file: {'present' if n_score is not None else 'missing'}")
        err_dir = normal_run / "errors"
        if err_dir.exists():
            err_files = sorted([p.name for p in err_dir.glob('*.txt')])
            if err_files:
                lines.append("- Generator errors:")
                for name in err_files:
                    lines.append(f"  - {name}")
            else:
                lines.append("- Generator errors: none")
        else:
            lines.append("- Generator errors: none")
    else:
        lines.append("Latest normal idea run: missing")

    lines.append("")

    # Algo status
    lines.append("Algo run status:")
    algos = _collect_algo_status()
    if not algos:
        lines.append("- No algo states found")
    else:
        for a in algos:
            flag = "STALE" if _stale(a["last_run"]) else "OK"
            lines.append(f"- {a['name']}: {a['last_run']} [{flag}]")

    # Leaderboard
    lb_json = Path("docs/leaderboards/rolling_30d.json")
    lines.append("")
    lines.append(f"Rolling 30D leaderboard: {'present' if lb_json.exists() else 'missing'}")

    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    report = _build_report()
    print(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
