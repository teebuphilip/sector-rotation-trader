"""
Weekly feature idea generator.

Calls BOTH OpenAI and Anthropic independently — 4 ideas each, 8 total.
Writes PRDs to drafts/features/YYYY-MM-DD/ with provider prefix.
Writes a summary file for the email step.

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

OPENAI_MODEL = os.getenv("OPENAI_MODEL") or "gpt-4.1-mini"
ANTHROPIC_MODEL = os.getenv("ANTHROPIC_MODEL") or "claude-haiku-4-5-20251001"

SYSTEM_PROMPT = """\
You are a product manager for CrazyStockAlgo — a public paper-trading signal lab.
You have deep knowledge of the product context provided.

Your job: generate 4 distinct, grounded feature ideas for post-launch.

Rules:
- Each idea must serve one of the three user archetypes (Receipts Guy, Signal Hunter, Alt-Data Nerd).
- Each idea must pass the on-brand test: sounds like it was built by the guy who named an algo \
after his dead dog — not a marketing team.
- No onboarding wizards. No notification centers. No activity feeds. No AI stock-picking claims.
- Losses and failures must remain first-class citizens in any feature touching the leaderboard or signals.
- Features must fit the core interaction: a user scans the leaderboard to see which weird signals \
are holding up.
- Keep each PRD tight. 1-2 sentences max per field. No fluff.

Output format: return a JSON array of exactly 4 objects, each with these keys:
  name, status, problem, goal, metric, user_stories (array of 2 strings),
  requirements (array of 3 strings), ux_notes, acceptance_criteria (array of 3 strings),
  out_of_scope (array of 2 strings)

Return only the JSON array. No commentary before or after.\
"""


def _build_prompt(product_ctx: str, template: str) -> str:
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


def _parse_ideas(raw: str) -> list[dict]:
    raw = raw.strip()
    if raw.startswith("```"):
        raw = re.sub(r"^```[a-z]*\n?", "", raw)
        raw = re.sub(r"\n?```$", "", raw)
    return json.loads(raw)


def _slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")[:50]


def _render_prd(idea: dict, run_date: str, provider: str) -> str:
    user_stories = "\n".join(f"- {s}" for s in idea.get("user_stories", []))
    requirements = "\n".join(
        f"- **Requirement {i+1}:** {r}"
        for i, r in enumerate(idea.get("requirements", []))
    )
    ac = "\n".join(f"- {c}" for c in idea.get("acceptance_criteria", []))
    oos = "\n".join(f"- {o}" for o in idea.get("out_of_scope", []))

    return f"""# {idea.get("name", "Untitled Feature")}
Status: {idea.get("status", "Draft")}
Generated: {run_date} | Provider: {provider}

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


def _run_provider(name: str, fn, prompt: str, run_date: str, out_dir: Path, dry_run: bool) -> tuple[int, list[str], str]:
    """Call one provider. Returns (count, titles, error_msg)."""
    print(f"[feature_ideas] calling {name}...")
    try:
        raw = fn(prompt)
        ideas = _parse_ideas(raw)
    except Exception as exc:
        msg = f"{name} failed: {exc}"
        print(f"[feature_ideas] {msg}", file=sys.stderr)
        return 0, [], msg

    titles = []
    if not dry_run:
        out_dir.mkdir(parents=True, exist_ok=True)

    for i, idea in enumerate(ideas, 1):
        title = idea.get("name", f"Feature {i}")
        titles.append(title)
        if dry_run:
            print(f"\n--- {name.upper()} IDEA {i}: {title} ---")
            print(_render_prd(idea, run_date, name))
        else:
            slug = _slugify(title)
            path = out_dir / f"{name}-feature-{i:02d}-{slug}.md"
            path.write_text(_render_prd(idea, run_date, name))
            print(f"[feature_ideas] wrote {path}")

    return len(ideas), titles, ""


def run(run_date: str, dry_run: bool = False) -> None:
    if not PRODUCT_CONTEXT.exists():
        print(f"[feature_ideas] missing {PRODUCT_CONTEXT}", file=sys.stderr)
        sys.exit(1)
    if not PRD_TEMPLATE.exists():
        print(f"[feature_ideas] missing {PRD_TEMPLATE}", file=sys.stderr)
        sys.exit(1)

    product_ctx = PRODUCT_CONTEXT.read_text()
    template = PRD_TEMPLATE.read_text()
    prompt = _build_prompt(product_ctx, template)
    out_dir = OUT_ROOT / run_date

    results = {}

    if os.getenv("OPENAI_API_KEY"):
        count, titles, err = _run_provider("openai", _call_openai, prompt, run_date, out_dir, dry_run)
        results["openai"] = {"count": count, "titles": titles, "error": err}
    else:
        results["openai"] = {"count": 0, "titles": [], "error": "OPENAI_API_KEY not set"}

    if os.getenv("ANTHROPIC_API_KEY"):
        count, titles, err = _run_provider("anthropic", _call_anthropic, prompt, run_date, out_dir, dry_run)
        results["anthropic"] = {"count": count, "titles": titles, "error": err}
    else:
        results["anthropic"] = {"count": 0, "titles": [], "error": "ANTHROPIC_API_KEY not set"}

    total = sum(r["count"] for r in results.values())
    print(f"[feature_ideas] done — {total} PRDs total")

    if not dry_run:
        _write_summary(run_date, results, out_dir)


def _write_summary(run_date: str, results: dict, out_dir: Path) -> None:
    lines = [
        f"FEATURE IDEAS RUN — {run_date}",
        "=" * 50,
        "",
    ]

    total = sum(r["count"] for r in results.values())
    lines.append(f"Total PRDs generated: {total}")
    lines.append("")

    for provider, data in results.items():
        label = "ChatGPT (OpenAI)" if provider == "openai" else "Claude (Anthropic)"
        lines.append(f"{label}: {data['count']} ideas")
        if data["error"]:
            lines.append(f"  ERROR: {data['error']}")
        for i, title in enumerate(data["titles"], 1):
            lines.append(f"  {i}. {title}")
        lines.append("")

    lines.append("=" * 50)
    lines.append(f"PRDs saved to: drafts/features/{run_date}/")

    summary_path = out_dir / "summary.txt"
    out_dir.mkdir(parents=True, exist_ok=True)
    summary_path.write_text("\n".join(lines))
    print(f"[feature_ideas] summary written to {summary_path}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", default=None, help="YYYY-MM-DD (default: today)")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    run_date = args.date or date.today().isoformat()
    run(run_date, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
