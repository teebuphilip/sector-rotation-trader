"""
Weekly feature idea generator.

Reads the product context and PRD template, calls OpenAI (primary) or
Anthropic (fallback), and writes 4 filled-out PRD files to
drafts/features/YYYY-MM-DD/.

Run manually:
    python scripts/feature_idea_generator.py
    python scripts/feature_idea_generator.py --date 2026-04-25
    python scripts/feature_idea_generator.py --dry-run

Wired into .github/workflows/feature_ideas.yml (Fridays 22:00 UTC).
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from datetime import date
from pathlib import Path

PRODUCT_CONTEXT = Path(".claude/skills/crazystockalgo-context/product.md")
PRD_TEMPLATE = Path(".claude/skills/crazystockalgo-context/feature-prd-template.md")
OUT_ROOT = Path("drafts/features")

OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")
ANTHROPIC_MODEL = os.getenv("ANTHROPIC_MODEL", "claude-haiku-4-5-20251001")

SYSTEM_PROMPT = """\
You are a product manager for CrazyStockAlgo — a public paper-trading signal lab.
You have deep knowledge of the product context provided.

Your job: generate 4 distinct, grounded feature ideas for post-launch.

Rules:
- Each idea must serve one of the three user archetypes (Receipts Guy, Signal Hunter, Alt-Data Nerd).
- Each idea must pass the on-brand test: sounds like it was built by the guy who named an algo after his dead dog — not a marketing team.
- No onboarding wizards. No notification centers. No activity feeds. No AI stock-picking claims.
- Losses and failures must remain first-class citizens in any feature touching the leaderboard or signals.
- Features must fit the core interaction: a user scans the leaderboard to see which weird signals are holding up.
- Keep each PRD tight. 1-2 sentences max per field. No fluff.

Output format: return a JSON array of exactly 4 objects, each with these keys:
  name, status, problem, goal, metric, user_stories (array of 2 strings),
  requirements (array of 3 strings), ux_notes, acceptance_criteria (array of 3 strings),
  out_of_scope (array of 2 strings)

Return only the JSON array. No commentary before or after.\
"""


def _build_user_prompt(product_ctx: str, template: str) -> str:
    return f"""Here is the product context:

{product_ctx}

Here is the PRD template structure to fill out for each idea:

{template}

Generate 4 feature ideas as a JSON array following the output format specified."""


def _call_openai(prompt: str) -> str:
    import openai
    client = openai.OpenAI(api_key=os.environ["OPENAI_API_KEY"])
    resp = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ],
        temperature=0.7,
        max_tokens=4096,
    )
    return resp.choices[0].message.content.strip()


def _call_anthropic(prompt: str) -> str:
    import anthropic
    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    resp = client.messages.create(
        model=ANTHROPIC_MODEL,
        max_tokens=4096,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": prompt}],
    )
    return resp.content[0].text.strip()


def _call_llm(prompt: str) -> str:
    if os.getenv("OPENAI_API_KEY"):
        try:
            return _call_openai(prompt)
        except Exception as exc:
            print(f"[feature_ideas] OpenAI failed: {exc} — trying Anthropic", file=sys.stderr)
    if os.getenv("ANTHROPIC_API_KEY"):
        return _call_anthropic(prompt)
    print("[feature_ideas] No API keys found (OPENAI_API_KEY or ANTHROPIC_API_KEY)", file=sys.stderr)
    sys.exit(1)


def _slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")[:50]


def _render_prd(idea: dict, run_date: str) -> str:
    user_stories = "\n".join(f"- {s}" for s in idea.get("user_stories", []))
    requirements = "\n".join(f"- **Requirement {i+1}:** {r}" for i, r in enumerate(idea.get("requirements", [])))
    ac = "\n".join(f"- {c}" for c in idea.get("acceptance_criteria", []))
    oos = "\n".join(f"- {o}" for o in idea.get("out_of_scope", []))

    return f"""# {idea.get("name", "Untitled Feature")}
Status: {idea.get("status", "Draft")}
Generated: {run_date}

## 1. The "Why" (Context)

- **Problem:** {idea.get("problem", "")}
- **Goal:** {idea.get("goal", "")}
- **Metric:** {idea.get("metric", "")}

## 2. User Stories

{user_stories}

## 3. Functional Requirements (The "What")

{requirements}

## 4. Design & UX

- **Mockups:** TBD
- **Key Interaction:** {idea.get("ux_notes", "")}

## 5. Acceptance Criteria (AC)

{ac}

## 6. Out of Scope

{oos}
"""


def _parse_ideas(raw: str) -> list[dict]:
    raw = raw.strip()
    if raw.startswith("```"):
        raw = re.sub(r"^```[a-z]*\n?", "", raw)
        raw = re.sub(r"\n?```$", "", raw)
    return json.loads(raw)


def run(run_date: str, dry_run: bool = False) -> None:
    if not PRODUCT_CONTEXT.exists():
        print(f"[feature_ideas] missing {PRODUCT_CONTEXT}", file=sys.stderr)
        sys.exit(1)
    if not PRD_TEMPLATE.exists():
        print(f"[feature_ideas] missing {PRD_TEMPLATE}", file=sys.stderr)
        sys.exit(1)

    product_ctx = PRODUCT_CONTEXT.read_text()
    template = PRD_TEMPLATE.read_text()
    prompt = _build_user_prompt(product_ctx, template)

    print("[feature_ideas] calling LLM...")
    raw = _call_llm(prompt)

    try:
        ideas = _parse_ideas(raw)
    except Exception as exc:
        print(f"[feature_ideas] failed to parse LLM response: {exc}", file=sys.stderr)
        print(raw, file=sys.stderr)
        sys.exit(1)

    if dry_run:
        for i, idea in enumerate(ideas, 1):
            print(f"\n--- IDEA {i}: {idea.get('name')} ---")
            print(_render_prd(idea, run_date))
        return

    out_dir = OUT_ROOT / run_date
    out_dir.mkdir(parents=True, exist_ok=True)

    for i, idea in enumerate(ideas, 1):
        slug = _slugify(idea.get("name", f"feature-{i}"))
        filename = f"feature-{i:02d}-{slug}.md"
        path = out_dir / filename
        path.write_text(_render_prd(idea, run_date))
        print(f"[feature_ideas] wrote {path}")

    print(f"[feature_ideas] done — {len(ideas)} PRDs in {out_dir}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", default=None, help="YYYY-MM-DD (default: today)")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    run_date = args.date or date.today().isoformat()
    run(run_date, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
