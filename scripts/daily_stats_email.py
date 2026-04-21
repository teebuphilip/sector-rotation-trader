#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
from datetime import datetime, timedelta
from pathlib import Path


SECTOR_ETFS = {"XLK", "XLF", "XLY", "XLP", "XLU", "XLV", "XLI", "XLB", "XLRE", "XLC", "XLE"}


def _primary_sector_etf(item: dict) -> str | None:
    universe = item.get("universe") or []
    if not isinstance(universe, list):
        return None
    matches = [str(x).strip().upper() for x in universe if str(x).strip().upper() in SECTOR_ETFS]
    if len(matches) == 1:
        return matches[0]
    return None


def _load_algos_index() -> list[dict]:
    payload = _load_json(Path("data/product/algos_index.json"))
    if not isinstance(payload, dict):
        return []
    algos = payload.get("algos") or []
    return [a for a in algos if isinstance(a, dict)]


def _comparator_section(lines: list[str]) -> None:
    comparison = _load_json(Path("docs/comparison/today.json"))
    if not isinstance(comparison, dict):
        lines.append("")
        lines.append("Comparator snapshot: missing")
        return

    comparators = comparison.get("comparators") or {}
    if not isinstance(comparators, dict) or not comparators:
        lines.append("")
        lines.append("Comparator snapshot: empty")
        return

    lines.append("")
    lines.append("Comparator snapshot:")
    for name, payload in sorted(comparators.items()):
        if not isinstance(payload, dict):
            continue
        counts = {"UP": 0, "DOWN": 0, "NEUTRAL": 0}
        for row in payload.values():
            if not isinstance(row, dict):
                continue
            direction = str(row.get("direction") or "NEUTRAL")
            if direction in counts:
                counts[direction] += 1
        lines.append(f"- {name}: UP {counts['UP']} / DOWN {counts['DOWN']} / NEUTRAL {counts['NEUTRAL']}")

    algos = _load_algos_index()
    beaters = []
    aligned = []
    for algo in algos:
        etf = _primary_sector_etf(algo)
        if not etf:
            continue
        ytd = algo.get("ytd_pct")
        try:
            ytdf = float(ytd)
        except Exception:
            continue
        signals = {}
        for name, payload in comparators.items():
            if not isinstance(payload, dict):
                continue
            row = payload.get(etf)
            if isinstance(row, dict) and row.get("direction") in {"UP", "DOWN", "NEUTRAL"}:
                signals[name] = row.get("direction")
        if not signals:
            continue
        dirs = set(signals.values())
        row = f"{algo.get('name', algo.get('algo_id', '?'))} [{etf}] {ytdf:+.2f}% :: " + ", ".join(f"{k}={v}" for k, v in sorted(signals.items()))
        if ytdf > 0 and dirs <= {"DOWN", "NEUTRAL"} and "DOWN" in dirs:
            beaters.append(row)
        elif ytdf > 0 and dirs == {"UP"}:
            aligned.append(row)

    if beaters:
        lines.append("- Potential comparator beaters (positive YTD while mapped comparators are not UP):")
        for row in sorted(beaters)[:10]:
            lines.append(f"  - {row}")
    else:
        lines.append("- Potential comparator beaters: none today")

    if aligned:
        lines.append("- Comparator-aligned leaders:")
        for row in sorted(aligned)[:10]:
            lines.append(f"  - {row}")


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


def _load_ideas(path: Path) -> list[dict]:
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


def _collect_algo_status() -> dict[str, list[dict]]:
    entries = {"baseline": [], "normal": [], "crazy": []}

    # Baseline
    base_path = Path("state.json")
    if base_path.exists():
        last = _state_last_run(base_path)
        entries["baseline"].append({"name": "NRWise Acceleration", "path": str(base_path), "last_run": last})

    # Normal
    normal_dir = Path("data/normal/state")
    if normal_dir.exists():
        for p in sorted(normal_dir.glob("*.json")):
            state = _load_json(p)
            meta = (state or {}).get("meta", {}).get(p.stem, {}) if isinstance(state, dict) else {}
            name = meta.get("name") or p.stem
            last = state.get("last_run") if isinstance(state, dict) else "missing"
            entries["normal"].append({"name": name, "path": str(p), "last_run": last})

    # Crazy
    crazy_dir = Path("data/crazy/state")
    if crazy_dir.exists():
        for p in sorted(crazy_dir.glob("*.json")):
            state = _load_json(p)
            meta = (state or {}).get("meta", {}).get(p.stem, {}) if isinstance(state, dict) else {}
            name = meta.get("name") or p.stem
            last = state.get("last_run") if isinstance(state, dict) else "missing"
            entries["crazy"].append({"name": name, "path": str(p), "last_run": last})

    return entries


def _collect_blocked_ideas(run_dir: Path) -> list[str]:
    blocked = []
    raw_dir = run_dir / "raw"
    for src in ["chatgpt", "claude"]:
        path = raw_dir / f"{src}_{run_dir.name}.jsonl"
        if not path.exists():
            continue
        for idea in _load_ideas(path):
            keys = idea.get("required_keys", [])
            if keys:
                blocked.append(f"{idea.get('idea_id','(unknown)')} ({src}) -> {', '.join(keys)}")
    return blocked


def _collect_new_algos(run_date: str) -> list[dict]:
    path = Path("data/algos/new_algos.jsonl")
    if not path.exists():
        return []
    items = []
    for line in path.read_text().splitlines():
        s = line.strip()
        if not s:
            continue
        try:
            obj = json.loads(s)
        except Exception:
            continue
        if obj.get("date") == run_date:
            items.append(obj)
    return items


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
        chat_path = latest_run / "raw" / f"chatgpt_{run_date}.jsonl"
        claude_path = latest_run / "raw" / f"claude_{run_date}.jsonl"
        chat_count = _count_jsonl(chat_path)
        claude_count = _count_jsonl(claude_path)
        lines.append(f"- ChatGPT ideas: {chat_count}")
        lines.append(f"- Claude ideas:  {claude_count}")
        lines.append(f"- Total ideas: {chat_count + claude_count}")
        score = _load_json(latest_run / "score.json")
        lines.append(f"- Score file: {'present' if score is not None else 'missing'}")
        err_dir = latest_run / "errors"
        if err_dir.exists():
            err_files = sorted([
                p.name for p in err_dir.glob("*.txt")
                if p.stat().st_size > 0 and not p.name.endswith("_http_code.txt")
            ])
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
            lines.append(f"- Blocked ideas total: {len(blocked)}")
            lines.append("- Blocked ideas (missing keys):")
            for b in blocked:
                lines.append(f"  - {b}")
        else:
            lines.append("- Blocked ideas total: 0")
            lines.append("- Blocked ideas: none")

        # Idea summaries
        ideas = []
        for src, path in [("chatgpt", chat_path), ("claude", claude_path)]:
            for idea in _load_ideas(path):
                ideas.append({
                    "src": src,
                    "idea_id": idea.get("idea_id", "(unknown)"),
                    "title": idea.get("title", "").strip(),
                })
        if ideas:
            lines.append("- Ideas generated:")
            for item in ideas:
                title = f" — {item['title']}" if item["title"] else ""
                lines.append(f"  - {item['idea_id']} ({item['src']}){title}")
    else:
        lines.append("Latest idea run: missing")

    lines.append("")

    # New algos added today
    new_algos = _collect_new_algos(run_date)
    if new_algos:
        lines.append("New algos added:")
        for item in new_algos:
            lines.append(f"- {item.get('name','(unknown)')} ({item.get('category','?')})")
    else:
        lines.append("New algos added: none")

    lines.append("")

    # Normal idea run (weekly)
    normal_base = Path("data/normal_ideas/runs")
    normal_run = _latest_run_dir(normal_base)
    if normal_run:
        n_date = normal_run.name
        lines.append(f"Latest normal idea run: {n_date}")
        chat_path = normal_run / "raw" / f"chatgpt_{n_date}.jsonl"
        claude_path = normal_run / "raw" / f"claude_{n_date}.jsonl"
        chat_count = _count_jsonl(chat_path)
        claude_count = _count_jsonl(claude_path)
        lines.append(f"- ChatGPT ideas: {chat_count}")
        lines.append(f"- Claude ideas:  {claude_count}")
        lines.append(f"- Total ideas: {chat_count + claude_count}")
        n_score = _load_json(normal_run / "score.json")
        lines.append(f"- Score file: {'present' if n_score is not None else 'missing'}")
        err_dir = normal_run / "errors"
        if err_dir.exists():
            err_files = sorted([
                p.name for p in err_dir.glob("*.txt")
                if p.stat().st_size > 0 and not p.name.endswith("_http_code.txt")
            ])
            if err_files:
                lines.append("- Generator errors:")
                for name in err_files:
                    lines.append(f"  - {name}")
            else:
                lines.append("- Generator errors: none")
        else:
            lines.append("- Generator errors: none")

        blocked = _collect_blocked_ideas(normal_run)
        if blocked:
            lines.append(f"- Blocked ideas total: {len(blocked)}")
            lines.append("- Blocked ideas (missing keys):")
            for b in blocked:
                lines.append(f"  - {b}")
        else:
            lines.append("- Blocked ideas total: 0")

        ideas = []
        for src, path in [("chatgpt", chat_path), ("claude", claude_path)]:
            for idea in _load_ideas(path):
                ideas.append({
                    "src": src,
                    "idea_id": idea.get("idea_id", "(unknown)"),
                    "title": idea.get("title", "").strip(),
                })
        if ideas:
            lines.append("- Ideas generated:")
            for item in ideas:
                title = f" — {item['title']}" if item["title"] else ""
                lines.append(f"  - {item['idea_id']} ({item['src']}){title}")
    else:
        lines.append("Latest normal idea run: missing")

    lines.append("")

    # Daily AI cost (idea generation)
    def _daily_cost(path: Path, run_date: str) -> float:
        if not path.exists():
            return 0.0
        total = 0.0
        with path.open("r", encoding="utf-8", errors="replace") as f:
            header = f.readline()
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

    lines.append("Daily AI cost (idea generation):")
    chat_cost = _daily_cost(Path("logs/ai_costs_chatgpt_ideas.csv"), run_date)
    claude_cost = _daily_cost(Path("logs/ai_costs_claude_ideas.csv"), run_date)
    normal_chat_cost = _daily_cost(Path("logs/ai_costs_chatgpt_normal.csv"), run_date)
    normal_claude_cost = _daily_cost(Path("logs/ai_costs_claude_normal.csv"), run_date)
    lines.append(f"- ChatGPT (crazy): ${chat_cost:.2f}")
    lines.append(f"- Claude (crazy): ${claude_cost:.2f}")
    if normal_run:
        lines.append(f"- ChatGPT (normal): ${normal_chat_cost:.2f}")
        lines.append(f"- Claude (normal): ${normal_claude_cost:.2f}")
    lines.append(f"- Total: ${(chat_cost + claude_cost + normal_chat_cost + normal_claude_cost):.2f}")

    # Algo status
    lines.append("Algo run status:")
    algos = _collect_algo_status()
    if not any(algos.values()):
        lines.append("- No algo states found")
    else:
        if algos["baseline"]:
            lines.append("- Baseline:")
            for a in algos["baseline"]:
                flag = "STALE" if _stale(a["last_run"]) else "OK"
                lines.append(f"  - {a['name']}: {a['last_run']} [{flag}]")
        if algos["normal"]:
            lines.append("- Normal:")
            for a in algos["normal"]:
                flag = "STALE" if _stale(a["last_run"]) else "OK"
                lines.append(f"  - {a['name']}: {a['last_run']} [{flag}]")
        if algos["crazy"]:
            lines.append("- Crazy:")
            for a in algos["crazy"]:
                flag = "STALE" if _stale(a["last_run"]) else "OK"
                lines.append(f"  - {a['name']}: {a['last_run']} [{flag}]")

    # Leaderboard
    lb_json = Path("docs/leaderboards/rolling_30d.json")
    lines.append("")
    lines.append(f"Rolling 30D leaderboard: {'present' if lb_json.exists() else 'missing'}")

    # ── Top performers (from rank_history.csv) ────────────────────────
    lines.append("")
    rank_csv = Path("data/rank_history.csv")
    if rank_csv.exists():
        import csv
        with rank_csv.open("r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            today_rows = [r for r in reader if r.get("date") == run_date]
        if today_rows:
            by_return = sorted(today_rows, key=lambda r: float(r.get("ytd_pct", 0)), reverse=True)
            beating = sum(1 for r in by_return if r.get("beat_spy", "").lower() == "true")
            lines.append(f"Force Rank Summary ({len(by_return)} algos):")
            lines.append(f"- Beating SPY: {beating}/{len(by_return)}")
            lines.append("")
            lines.append("Top 10 by Return:")
            for i, r in enumerate(by_return[:10], 1):
                name = r.get("name", r.get("algo_id", "?"))
                ytd = float(r.get("ytd_pct", 0))
                alpha = float(r.get("alpha_pct", 0))
                flag = "BEAT" if r.get("beat_spy", "").lower() == "true" else "LAG"
                lines.append(f"  {i:2d}. {name:40s}  {ytd:+7.2f}%  alpha:{alpha:+6.2f}%  [{flag}]")
            lines.append("")
            lines.append("Bottom 5 by Return:")
            for r in by_return[-5:]:
                name = r.get("name", r.get("algo_id", "?"))
                ytd = float(r.get("ytd_pct", 0))
                alpha = float(r.get("alpha_pct", 0))
                rank = r.get("rank_return", "?")
                lines.append(f"  #{rank:>3s}  {name:40s}  {ytd:+7.2f}%  alpha:{alpha:+6.2f}%")
        else:
            lines.append("Force Rank: no rows for today")
    else:
        lines.append("Force Rank: rank_history.csv missing")

    _comparator_section(lines)

    # ── Validation summary ────────────────────────────────────────────
    lines.append("")
    validation_cache = Path("data/.validation_cache/snapshot_counts.json")
    if validation_cache.exists():
        counts = _load_json(validation_cache)
        if isinstance(counts, dict):
            lines.append(f"Validation cache: {len(counts)} algos tracked")
        else:
            lines.append("Validation cache: present but unreadable")
    else:
        lines.append("Validation cache: not yet established")

    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    report = _build_report()
    print(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
