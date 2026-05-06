#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from algo_copy_registry import build_algo_copy_registry


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

    run_dir = Path("data") / "normal_ideas" / "runs" / args.date
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
        docs_dir = Path("docs") / "normal_ideas"
        docs_dir.mkdir(parents=True, exist_ok=True)
        (docs_dir / f"{args.date}.md").write_text("\n\n---\n\n".join(combined_md))
        build_algo_copy_registry()

    print(f"✅ Published markdown to {pub_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
