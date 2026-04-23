#!/usr/bin/env python3
"""
score_feature_virality.py

Scores feature draft markdown files against the V-Factor virality framework.
Reads all drafts from a directory, scores each via Claude, writes a ranked
top-N list to a dated output file.

Usage:
    python score_feature_virality.py
    python score_feature_virality.py --drafts-dir drafts/features/2026-04-22
    python score_feature_virality.py --top 5 --out reports/virality/

Dependencies:
    pip install anthropic
"""

import os
import sys
import json
import argparse
import re
from datetime import date
from pathlib import Path
import anthropic

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

DEFAULT_DRAFTS_DIR = "drafts/features"
DEFAULT_OUT_DIR = "reports/virality"
DEFAULT_TOP_N = 10
MODEL = "claude-haiku-4-5-20251001"

# Stockarithm-specific virality multipliers fed into the prompt
CSA_CONTEXT = """
Product context for scoring:
- stockarithm.com is a paper-trading signal lab that publishes BOTH winners and failures publicly.
- The Biscotti algo (named after the founder's dog who died April 2025) is a character with emotional resonance.
- Core audience: r/algotrading, r/investing, r/stocks — skeptical, data-literate, anti-hype.
- Unfair advantages: transparency (failures published), 25-year empirical foundation, Kronos AI disagreement data.
- Anti-patterns: hype language, hiding losses, anything that looks like a generic fintech dashboard.
- A feature scores HIGHER if it exploits the failures-published angle or the Biscotti character.
- A feature scores LOWER if it requires significant new infrastructure before July 1 launch.
"""

SCORE_PROMPT = """
You are scoring a product feature spec for viral potential using the V-Factor framework.
Score each dimension 1-5. Be harsh. Most features score 2-3. Only genuinely viral mechanics score 4-5.

{csa_context}

V-Factor dimensions:
A. Proof of Work (Social Currency): Does it let users look smart or prove success to others?
B. Invitation Loop (Incentivized Growth): Does it require/encourage others to join for more value?
C. Public Evidence (Built-in Ad): Does using it naturally leave a public footprint?
D. Cooperative Gain (Network Effect): Does the product get better as more users join?

Also score:
E. Build Complexity (1=simple/days, 5=complex/weeks) — LOWER is better for pre-launch
F. Stockarithm Fit (1=generic SaaS, 5=only makes sense for THIS product)

Feature spec:
---
{feature_text}
---

Respond ONLY with valid JSON, no markdown, no explanation outside the JSON:
{{
  "feature_name": "short name extracted from spec",
  "scores": {{
    "proof_of_work": <1-5>,
    "invitation_loop": <1-5>,
    "public_evidence": <1-5>,
    "cooperative_gain": <1-5>,
    "build_complexity": <1-5>,
    "stockarithm_fit": <1-5>
  }},
  "viral_total": <sum of A+B+C+D, max 20>,
  "adjusted_score": <viral_total * (6 - build_complexity) * stockarithm_fit / 25.0, rounded to 2 decimal places>,
  "top_viral_mechanic": "one sentence — what specifically makes this shareable or not",
  "biggest_weakness": "one sentence — what kills the viral potential",
  "verdict": "BUILD_NOW | BUILD_LATER | SKIP"
}}

Verdict rules:
- BUILD_NOW: adjusted_score >= 8 AND build_complexity <= 3
- BUILD_LATER: adjusted_score >= 5 OR (high viral but complex)
- SKIP: adjusted_score < 5 AND no standout mechanic
"""

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def find_draft_files(drafts_dir: str) -> list[Path]:
    """Find all markdown draft files, searching dated subdirs if needed."""
    base = Path(drafts_dir)
    if not base.exists():
        print(f"ERROR: drafts dir not found: {base}")
        sys.exit(1)

    # Direct markdown files in the dir
    files = list(base.glob("*.md"))

    # Also search one level of dated subdirs (2026-04-22/)
    for subdir in sorted(base.iterdir()):
        if subdir.is_dir() and re.match(r"\d{4}-\d{2}-\d{2}", subdir.name):
            files.extend(subdir.glob("*.md"))

    if not files:
        print(f"ERROR: no .md files found under {base}")
        sys.exit(1)

    return sorted(files)


def read_draft(path: Path) -> str:
    return path.read_text(encoding="utf-8").strip()


def score_feature(client: anthropic.Anthropic, feature_text: str) -> dict:
    prompt = SCORE_PROMPT.format(
        csa_context=CSA_CONTEXT,
        feature_text=feature_text[:4000]  # cap to avoid huge context
    )

    response = client.messages.create(
        model=MODEL,
        max_tokens=1000,
        messages=[{"role": "user", "content": prompt}]
    )

    raw = response.content[0].text.strip()

    # Strip markdown fences if model adds them anyway
    raw = re.sub(r"^```json\s*", "", raw)
    raw = re.sub(r"```$", "", raw).strip()

    return json.loads(raw)


def render_report(results: list[dict], top_n: int) -> str:
    today = date.today().isoformat()
    lines = [
        f"# Virality Score Report — {today}",
        f"Scored {len(results)} features. Top {top_n} by adjusted score.",
        "",
        "## Scoring Key",
        "- **Viral Total** = Proof of Work + Invitation Loop + Public Evidence + Cooperative Gain (max 20)",
        "- **Adjusted Score** = viral_total × (6 − build_complexity) × csa_fit / 25",
        "- **Verdict**: BUILD_NOW (score≥8, complexity≤3) | BUILD_LATER | SKIP",
        "",
        "---",
        ""
    ]

    top = sorted(results, key=lambda x: x.get("adjusted_score", 0), reverse=True)[:top_n]

    for i, r in enumerate(top, 1):
        s = r.get("scores", {})
        lines += [
            f"## #{i} — {r.get('feature_name', 'Unknown')}",
            f"**Verdict: {r.get('verdict', '?')}** | "
            f"Adjusted Score: {r.get('adjusted_score', 0)} | "
            f"Viral Total: {r.get('viral_total', 0)}/20",
            "",
            f"| Proof of Work | Invitation Loop | Public Evidence | Cooperative Gain | Build Complexity | CSA Fit |",
            f"|:---:|:---:|:---:|:---:|:---:|:---:|",
            f"| {s.get('proof_of_work','?')} | {s.get('invitation_loop','?')} | "
            f"{s.get('public_evidence','?')} | {s.get('cooperative_gain','?')} | "
            f"{s.get('build_complexity','?')} | {s.get('stockarithm_fit','?')} |",
            "",
            f"**Top mechanic:** {r.get('top_viral_mechanic', '')}",
            f"**Biggest weakness:** {r.get('biggest_weakness', '')}",
            f"**Source file:** `{r.get('source_file', '')}`",
            "",
            "---",
            ""
        ]

    # Remaining features summary table
    rest = sorted(results, key=lambda x: x.get("adjusted_score", 0), reverse=True)[top_n:]
    if rest:
        lines += [
            f"## Remaining {len(rest)} Features",
            "",
            "| Feature | Adjusted Score | Verdict |",
            "|---|:---:|:---:|"
        ]
        for r in rest:
            lines.append(
                f"| {r.get('feature_name','?')} | "
                f"{r.get('adjusted_score', 0)} | "
                f"{r.get('verdict','?')} |"
            )
        lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Score feature drafts for virality")
    parser.add_argument("--drafts-dir", default=DEFAULT_DRAFTS_DIR)
    parser.add_argument("--out", default=DEFAULT_OUT_DIR)
    parser.add_argument("--top", type=int, default=DEFAULT_TOP_N)
    args = parser.parse_args()

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("ERROR: ANTHROPIC_API_KEY not set")
        sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key)

    draft_files = find_draft_files(args.drafts_dir)
    print(f"Found {len(draft_files)} draft files in {args.drafts_dir}")

    results = []
    for path in draft_files:
        print(f"  Scoring: {path.name} ... ", end="", flush=True)
        try:
            text = read_draft(path)
            scored = score_feature(client, text)
            scored["source_file"] = str(path)
            results.append(scored)
            print(f"{scored.get('verdict','?')} (adjusted={scored.get('adjusted_score',0)})")
        except Exception as e:
            print(f"ERROR — {e}")
            results.append({
                "feature_name": path.stem,
                "source_file": str(path),
                "adjusted_score": 0,
                "viral_total": 0,
                "verdict": "ERROR",
                "top_viral_mechanic": "",
                "biggest_weakness": str(e),
                "scores": {}
            })

    # Write outputs
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    today = date.today().isoformat()

    # JSON
    json_path = out_dir / f"{today}.json"
    json_path.write_text(json.dumps(results, indent=2))

    # Markdown report
    md_path = out_dir / f"{today}.md"
    md_path.write_text(render_report(results, args.top))

    # Latest symlink targets
    (out_dir / "latest.json").write_text(json.dumps(results, indent=2))
    (out_dir / "latest.md").write_text(render_report(results, args.top))

    print(f"\nDone. {len(results)} features scored.")
    print(f"  Report: {md_path}")
    print(f"  JSON:   {json_path}")

    # Print top 3 to stdout
    top3 = sorted(results, key=lambda x: x.get("adjusted_score", 0), reverse=True)[:3]
    print(f"\nTop 3:")
    for i, r in enumerate(top3, 1):
        print(f"  #{i} {r.get('feature_name','?')} — {r.get('verdict','?')} (score={r.get('adjusted_score',0)})")


if __name__ == "__main__":
    main()
