#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
from pathlib import Path


def _today_iso() -> str:
    return dt.date.today().isoformat()


def _load_jsonl(path: Path) -> list[dict]:
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


def _norm_title(s: str) -> str:
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", " ", s)
    return " ".join(s.split())


def _score_summary(score_path: Path) -> dict:
    if not score_path.exists():
        return {}
    try:
        data = json.loads(score_path.read_text())
    except Exception:
        return {}
    by_src = {"chatgpt": [], "claude": []}
    for row in data:
        src = row.get("source")
        if src in by_src and isinstance(row.get("score"), int):
            by_src[src].append(row["score"])
    out = {}
    for src, scores in by_src.items():
        if scores:
            out[src] = {
                "count": len(scores),
                "avg": sum(scores) / len(scores),
                "min": min(scores),
                "max": max(scores),
            }
    return out


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", required=True, help="Base directory, e.g. data/ideas or data/normal_ideas")
    parser.add_argument("--date", default=_today_iso())
    args = parser.parse_args()

    base = Path(args.base)
    run_dir = base / "runs" / args.date
    raw_dir = run_dir / "raw"

    chat = _load_jsonl(raw_dir / f"chatgpt_{args.date}.jsonl")
    claude = _load_jsonl(raw_dir / f"claude_{args.date}.jsonl")

    chat_ids = {i.get("idea_id") for i in chat if i.get("idea_id")}
    claude_ids = {i.get("idea_id") for i in claude if i.get("idea_id")}

    chat_titles = {_norm_title(i.get("title", "")) for i in chat if i.get("title")}
    claude_titles = {_norm_title(i.get("title", "")) for i in claude if i.get("title")}

    overlap_ids = sorted(chat_ids & claude_ids)
    overlap_titles = sorted(chat_titles & claude_titles)

    report = {
        "date": args.date,
        "base": str(base),
        "counts": {
            "chatgpt": len(chat),
            "claude": len(claude),
        },
        "overlap": {
            "idea_id": overlap_ids,
            "title": overlap_titles,
        },
        "unique": {
            "chatgpt": sorted(chat_ids - claude_ids),
            "claude": sorted(claude_ids - chat_ids),
        },
        "score_summary": _score_summary(run_dir / "score.json"),
    }

    out_path = run_dir / "compare.json"
    out_path.write_text(json.dumps(report, indent=2))

    docs_dir = Path("docs") / ("ideas" if base.name == "ideas" else "normal_ideas")
    docs_dir.mkdir(parents=True, exist_ok=True)
    md_path = docs_dir / f"compare_{args.date}.md"
    md_lines = [
        f"# Model Comparison — {args.date}",
        "",
        f"ChatGPT ideas: {len(chat)}",
        f"Claude ideas: {len(claude)}",
        "",
        f"Overlap by idea_id: {len(overlap_ids)}",
        f"Overlap by title: {len(overlap_titles)}",
        "",
        "## Unique to ChatGPT",
    ]
    for i in report["unique"]["chatgpt"]:
        md_lines.append(f"- {i}")
    md_lines += ["", "## Unique to Claude"]
    for i in report["unique"]["claude"]:
        md_lines.append(f"- {i}")

    md_path.write_text("\n".join(md_lines) + "\n")
    print(f"Wrote {out_path} and {md_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
