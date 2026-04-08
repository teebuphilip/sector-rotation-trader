#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import json
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
        items.append(json.loads(s))
    return items


def _idea_to_md(idea: dict) -> str:
    def _list(v):
        if isinstance(v, list):
            return "\n".join([f"- {x}" for x in v])
        return str(v)

    return f"""# {idea.get('title','(untitled)')}

**Idea ID:** `{idea.get('idea_id','')}`
**Source:** {idea.get('source_provider','')} / {idea.get('source_model','')}
**Frequency:** {idea.get('frequency','')}

## Thesis
{idea.get('thesis','')}

## Universe
{_list(idea.get('universe', []))}

## Data Sources
{_list(idea.get('data_sources', []))}

## Signal Logic
{idea.get('signal_logic','')}

## Entry / Exit
{idea.get('entry_exit','')}

## Position Sizing
{idea.get('position_sizing','')}

## Risks
{idea.get('risks','')}

## Implementation Notes
{idea.get('implementation_notes','')}

## Required Keys
{_list(idea.get('required_keys', [])) or '- None'}
"""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", default=_today_iso())
    args = parser.parse_args()

    run_dir = Path("data") / "ideas" / "runs" / args.date
    raw_dir = run_dir / "raw"
    pub_dir = run_dir / "publish"
    pub_dir.mkdir(parents=True, exist_ok=True)

    combined_md = []

    for src in ["chatgpt", "claude"]:
        path = raw_dir / f"{src}_{args.date}.jsonl"
        ideas = _load_jsonl(path)
        for idea in ideas:
            md = _idea_to_md(idea)
            out = pub_dir / f"{src}_{idea.get('idea_id','idea')}.md"
            out.write_text(md)
            combined_md.append(md)

    if combined_md:
        docs_dir = Path("docs") / "ideas"
        docs_dir.mkdir(parents=True, exist_ok=True)
        daily_path = docs_dir / f"{args.date}.md"
        daily_path.write_text("\n\n---\n\n".join(combined_md))

        index_path = docs_dir / "index.md"
        if index_path.exists():
            index_text = index_path.read_text()
        else:
            index_text = "# Crazy Ideas Index\n\n"

        entry = f"- {args.date}: `{daily_path}`\n"
        if entry not in index_text:
            index_text = index_text.strip() + "\n" + entry
            index_path.write_text(index_text + ("\n" if not index_text.endswith("\n") else ""))

    print(f"✅ Published markdown to {pub_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
