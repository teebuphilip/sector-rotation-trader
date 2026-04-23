"""
LLM post generator for Stockarithm daily Substack draft.

Reads reports/deep_validation/latest.json (or a dated version),
calls Claude API with locked facts only, and writes a 300-400 word
draft to drafts/YYYY-MM-DD.md.

Rules:
- Only facts present in the JSON are used. No invention.
- Voice: honest, curious, human, transparent. No hype.
- Forbidden: cutting-edge, proprietary algorithm, AI-powered, seamless.
- Named algos stay named (Biscotti, Baileymol, etc.)

Usage:
    python scripts/post_generator.py
    python scripts/post_generator.py --date 2026-04-21
    python scripts/post_generator.py --dry-run
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import date, datetime
from pathlib import Path

import anthropic

MODEL = os.getenv("ANTHROPIC_MODEL", "claude-haiku-4-5-20251001")
DRAFTS_DIR = Path("drafts")
REPORTS_DIR = Path("reports/deep_validation")

SYSTEM_PROMPT = """\
You are writing the daily lab bulletin for Stockarithm — a public paper trading \
experiment running alternative-data algorithmic signals. The author is an engineer, \
not a finance writer. He named an algo after his dead dog.

Tone rules:
- Direct, slightly irreverent, zero hype
- Show losses and failures as clearly as wins
- Use the algo names as given (Biscotti, Baileymol, etc.)
- Sound like lab notes, not content marketing
- Never write: cutting-edge, proprietary algorithm, AI-powered, seamless, robust, \
revolutionary, game-changing, our platform, unlock your potential

Format (300-400 words total, no fluff):
1. One headline (plain, specific, no clickbait)
2. 2-3 sentence lede: what actually happened today
3. Top 3 signals with return figures from the data
4. One weird signal or notable divergence from the data
5. One honest observation — could be a failure, a pattern, or a caveat
6. One CTA: "Check the leaderboard" (free) — no paid tier mention yet

Use ONLY the facts provided in the JSON below. Do not invent metrics, \
returns, or reasons not present in the data.\
"""


def _load_report(run_date: str) -> dict:
    dated = REPORTS_DIR / f"{run_date}.json"
    latest = REPORTS_DIR / "latest.json"
    for path in (dated, latest):
        if path.exists():
            try:
                return json.loads(path.read_text())
            except Exception:
                continue
    return {}


def _build_facts_block(report: dict) -> str:
    """Distill report into a compact JSON block for the prompt."""
    cf = report.get("content_facts", {})
    ss = report.get("system_state", {})
    fr = report.get("force_rank", {})
    r30 = report.get("rolling_30d", {})
    sc = report.get("sector_consensus", {})

    facts = {
        "report_date": report.get("report_date"),
        "system": {
            "total_algos": ss.get("total_algos"),
            "algos_with_positions": ss.get("algos_with_positions"),
            "algos_beating_spy": ss.get("algos_beating_spy"),
        },
        "top_force_ranked": (fr.get("top_algos") or [])[:3],
        "top_rolling_30d": (r30.get("top_algos") or [])[:3],
        "signal_of_day": cf.get("signal_of_day"),
        "failure_of_day": cf.get("failure_of_day"),
        "call_of_day": cf.get("call_of_day"),
        "notable_divergences": (cf.get("notable_divergences") or [])[:2],
        "sector_consensus_top": (sc.get("top_bullish") or [])[:3],
    }
    return json.dumps(facts, indent=2)


def generate(run_date: str, dry_run: bool = False) -> str:
    report = _load_report(run_date)
    if not report:
        print(f"[post_generator] no report found for {run_date}", file=sys.stderr)
        return ""

    facts_block = _build_facts_block(report)
    user_message = f"Here are today's locked facts:\n\n```json\n{facts_block}\n```\n\nWrite the daily lab bulletin."

    if dry_run:
        print("[post_generator] dry-run — facts block:")
        print(facts_block)
        return facts_block

    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("[post_generator] ANTHROPIC_API_KEY not set", file=sys.stderr)
        sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key)
    message = client.messages.create(
        model=MODEL,
        max_tokens=1024,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": user_message}],
    )
    draft = message.content[0].text.strip()

    DRAFTS_DIR.mkdir(parents=True, exist_ok=True)
    out = DRAFTS_DIR / f"{run_date}.md"
    out.write_text(draft)
    print(f"[post_generator] wrote {out}")
    return draft


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", default=None, help="YYYY-MM-DD (default: today)")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    run_date = args.date or date.today().isoformat()
    generate(run_date, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
