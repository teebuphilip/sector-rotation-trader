#!/usr/bin/env python3
"""
morning_email.py
----------------
Morning ideation summary email. Runs after crazy_ideas_daily (and
normal_ideas_weekly on Mondays). Answers one question: did we ideate?

Usage:
  python scripts/morning_email.py
"""
from __future__ import annotations

import json
import os
from datetime import datetime, timedelta
from pathlib import Path


def _latest_run_dir(base: Path):
    if not base.exists():
        return None
    runs = [p for p in base.iterdir() if p.is_dir()]
    if not runs:
        return None
    runs.sort()
    return runs[-1]


def _load_json(path: Path):
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


def _load_ideas(path: Path) -> list:
    items = []
    if not path.exists():
        return items
    for line in path.read_text().splitlines():
        s = line.strip()
        if not s:
            continue
        try:
            items.append(json.loads(s))
        except Exception:
            continue
    return items


def _collect_blocked_ideas(run_dir: Path) -> list:
    blocked = []
    raw_dir = run_dir / "raw"
    for src in ["chatgpt", "claude"]:
        path = raw_dir / "{src}_{date}.jsonl".format(src=src, date=run_dir.name)
        if not path.exists():
            continue
        for idea in _load_ideas(path):
            keys = idea.get("required_keys", [])
            if keys:
                blocked.append("{id} ({src}) -> {keys}".format(
                    id=idea.get("idea_id", "(unknown)"),
                    src=src,
                    keys=", ".join(keys),
                ))
    return blocked


def _daily_cost(path: Path, run_date: str) -> float:
    if not path.exists():
        return 0.0
    total = 0.0
    with path.open("r", encoding="utf-8", errors="replace") as f:
        f.readline()  # skip header
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(",")
            if len(parts) < 7:
                continue
            if parts[0] != run_date:
                continue
            try:
                total += float(parts[6])
            except ValueError:
                continue
    return total


def _render_idea_run(lines, label, run_dir):
    if not run_dir:
        lines.append("{label}: no run found".format(label=label))
        return

    run_date = run_dir.name
    lines.append("{label}: {date}".format(label=label, date=run_date))

    chat_path = run_dir / "raw" / "chatgpt_{}.jsonl".format(run_date)
    claude_path = run_dir / "raw" / "claude_{}.jsonl".format(run_date)
    chat_count = _count_jsonl(chat_path)
    claude_count = _count_jsonl(claude_path)
    total = chat_count + claude_count

    lines.append("  ChatGPT: {} ideas".format(chat_count))
    lines.append("  Claude:  {} ideas".format(claude_count))
    lines.append("  Total:   {} ideas".format(total))

    if total == 0:
        lines.append("  *** NO IDEAS GENERATED — CHECK PIPELINE ***")

    # Score file
    score = _load_json(run_dir / "score.json")
    lines.append("  Score file: {}".format("present" if score is not None else "MISSING"))

    # Errors
    err_dir = run_dir / "errors"
    if err_dir.exists():
        err_files = sorted([
            p.name for p in err_dir.glob("*.txt")
            if p.stat().st_size > 0 and not p.name.endswith("_http_code.txt")
        ])
        if err_files:
            lines.append("  Errors:")
            for name in err_files:
                lines.append("    - {}".format(name))
        else:
            lines.append("  Errors: none")
    else:
        lines.append("  Errors: none")

    # Blocked ideas
    blocked = _collect_blocked_ideas(run_dir)
    if blocked:
        lines.append("  Blocked (missing keys): {}".format(len(blocked)))
        for b in blocked:
            lines.append("    - {}".format(b))
    else:
        lines.append("  Blocked: 0")

    # Idea list
    ideas = []
    for src, path in [("chatgpt", chat_path), ("claude", claude_path)]:
        for idea in _load_ideas(path):
            ideas.append({
                "src": src,
                "idea_id": idea.get("idea_id", "(unknown)"),
                "title": idea.get("title", "").strip(),
            })
    if ideas:
        lines.append("  Ideas:")
        for item in ideas:
            title = " — {}".format(item["title"]) if item["title"] else ""
            lines.append("    - {} ({}){}".format(item["idea_id"], item["src"], title))

    return run_date


def build_report() -> str:
    lines = []
    now = datetime.utcnow().strftime("%Y-%m-%d")
    run_date = os.getenv("AFH_RUN_DATE") or now

    lines.append("Morning Ideation Report — {}".format(run_date))
    lines.append("=" * 50)
    lines.append("")

    # Crazy ideas (daily)
    ideas_base = Path("data/ideas/runs")
    latest_run = ideas_base / run_date
    if not latest_run.exists():
        latest_run = _latest_run_dir(ideas_base)
    actual_date = _render_idea_run(lines, "Crazy Ideas", latest_run)
    lines.append("")

    # Normal ideas (weekly — show latest regardless)
    normal_base = Path("data/normal_ideas/runs")
    normal_run = _latest_run_dir(normal_base)
    if normal_run:
        days_ago = (datetime.utcnow().date() - datetime.strptime(normal_run.name, "%Y-%m-%d").date()).days
        lines.append("Normal Ideas (weekly, last run {} days ago):".format(days_ago))
        _render_idea_run(lines, "Normal Ideas", normal_run)
        if days_ago > 9:
            lines.append("  *** STALE — last normal idea run was {} days ago ***".format(days_ago))
    else:
        lines.append("Normal Ideas: no runs found")
    lines.append("")

    # AI costs — read from all source files + aggregated
    import math
    cost_date = actual_date or run_date
    lines.append("AI Costs ({}):".format(cost_date))

    cost_by_provider = {}  # provider -> total
    cost_files = [
        Path("logs/ai_costs_chatgpt_ideas.csv"),
        Path("logs/ai_costs_claude_ideas.csv"),
        Path("logs/ai_costs_chatgpt_normal.csv"),
        Path("logs/ai_costs_claude_normal.csv"),
        Path("logs/ai_costs_aggregated.csv"),
    ]
    seen_rows = set()
    for cf in cost_files:
        if not cf.exists():
            continue
        import csv as _csv
        with cf.open("r", encoding="utf-8", errors="replace") as f:
            reader = _csv.DictReader(f)
            for row in reader:
                if row.get("date") != cost_date:
                    continue
                # Dedupe by (date, time, provider, model)
                key = (row.get("date"), row.get("time"), row.get("provider"), row.get("model"))
                if key in seen_rows:
                    continue
                seen_rows.add(key)
                provider = row.get("provider", "unknown")
                try:
                    cost = float(row.get("cost_usd", 0))
                except ValueError:
                    cost = 0.0
                cost_by_provider[provider] = cost_by_provider.get(provider, 0.0) + cost

    def _ceil_cent(v):
        """Round up to nearest cent."""
        return math.ceil(v * 100) / 100.0

    total = sum(cost_by_provider.values())
    if cost_by_provider:
        for provider in sorted(cost_by_provider.keys()):
            lines.append("  {:10s} ${:.2f}".format(provider + ":", _ceil_cent(cost_by_provider[provider])))
    else:
        lines.append("  No cost data found for today")
    lines.append("  Total:     ${:.2f}".format(_ceil_cent(total)))

    # New algos
    lines.append("")
    new_path = Path("data/algos/new_algos.jsonl")
    if new_path.exists():
        new_today = []
        for line in new_path.read_text().splitlines():
            s = line.strip()
            if not s:
                continue
            try:
                obj = json.loads(s)
            except Exception:
                continue
            if obj.get("date") == cost_date:
                new_today.append(obj)
        if new_today:
            lines.append("New algos added today:")
            for item in new_today:
                lines.append("  - {} ({})".format(
                    item.get("name", "(unknown)"),
                    item.get("category", "?"),
                ))
        else:
            lines.append("New algos added today: none")
    else:
        lines.append("New algos added today: none")

    # Blocked algos (missing API keys)
    lines.append("")
    blocked_file = Path("data/blocked/algos.jsonl")
    if blocked_file.exists():
        from collections import Counter
        blocked_entries = []
        key_counter = Counter()
        for line in blocked_file.read_text().splitlines():
            s = line.strip()
            if not s:
                continue
            try:
                obj = json.loads(s)
            except Exception:
                continue
            blocked_entries.append(obj)
            for k in obj.get("keys", []):
                key_counter[k] += 1

        # Dedupe by algo_id (keep latest entry per algo)
        seen_algos = {}
        for entry in blocked_entries:
            aid = entry.get("algo_id", "")
            seen_algos[aid] = entry
        unique_blocked = list(seen_algos.values())

        if unique_blocked:
            lines.append("Blocked Algos ({} unique):".format(len(unique_blocked)))
            # Group by missing key
            by_key = {}
            for entry in unique_blocked:
                for k in entry.get("keys", ["unknown"]):
                    by_key.setdefault(k, []).append(entry.get("name", entry.get("algo_id", "?")))
            for key in sorted(by_key.keys()):
                algos = by_key[key]
                lines.append("  {} ({}):".format(key, len(algos)))
                for name in sorted(algos):
                    lines.append("    - {}".format(name))
        else:
            lines.append("Blocked Algos: none")
    else:
        lines.append("Blocked Algos: none")

    return "\n".join(lines)


def main():
    print(build_report())


if __name__ == "__main__":
    main()
