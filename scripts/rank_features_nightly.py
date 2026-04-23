#!/usr/bin/env python3
"""
rank_features_nightly.py

Nightly job. Finds all feature drafts under drafts/features/, scores any
that haven't been scored yet, then force-ranks everything 1-N and writes
the master ranked list.

Incremental: already-scored features are read from cache, not re-scored.
Cache lives at reports/virality/.score_cache.json

Usage:
    python scripts/rank_features_nightly.py
    python scripts/rank_features_nightly.py --drafts-dir drafts/features --force-rescore

Wire into daily_run.yml as a step after your feature generator runs.
"""

import os
import sys
import json
import argparse
import re
import hashlib
from datetime import date
from pathlib import Path
import anthropic

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

DEFAULT_DRAFTS_DIR = "drafts/features"
DEFAULT_OUT_DIR = "reports/virality"
CACHE_FILE = "reports/virality/.score_cache.json"
MODEL = "claude-haiku-4-5-20251001"

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
  "top_viral_mechanic": "one sentence what specifically makes this shareable or not",
  "biggest_weakness": "one sentence what kills the viral potential",
  "verdict": "BUILD_NOW | BUILD_LATER | SKIP"
}}

Verdict rules:
- BUILD_NOW: adjusted_score >= 8 AND build_complexity <= 3
- BUILD_LATER: adjusted_score >= 5 OR high viral but complex
- SKIP: adjusted_score < 5 AND no standout mechanic
"""

# ---------------------------------------------------------------------------
# Cache
# ---------------------------------------------------------------------------

def load_cache(cache_path: str) -> dict:
    p = Path(cache_path)
    if p.exists():
        try:
            return json.loads(p.read_text())
        except Exception:
            return {}
    return {}


def save_cache(cache_path: str, cache: dict):
    p = Path(cache_path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(cache, indent=2))


def file_hash(path: Path) -> str:
    """MD5 of file contents — used as cache key so edits trigger rescore."""
    return hashlib.md5(path.read_bytes()).hexdigest()


# ---------------------------------------------------------------------------
# File discovery
# ---------------------------------------------------------------------------

def find_all_drafts(drafts_dir: str) -> list[Path]:
    base = Path(drafts_dir)
    if not base.exists():
        print(f"ERROR: drafts dir not found: {base}")
        sys.exit(1)

    files = list(base.glob("*.md"))
    for subdir in sorted(base.iterdir()):
        if subdir.is_dir() and re.match(r"\d{4}-\d{2}-\d{2}", subdir.name):
            files.extend(subdir.glob("*.md"))

    return sorted(files)


# ---------------------------------------------------------------------------
# Scoring
# ---------------------------------------------------------------------------

def score_feature(client: anthropic.Anthropic, feature_text: str) -> dict:
    prompt = SCORE_PROMPT.format(
        csa_context=CSA_CONTEXT,
        feature_text=feature_text[:4000]
    )
    response = client.messages.create(
        model=MODEL,
        max_tokens=1000,
        messages=[{"role": "user", "content": prompt}]
    )
    raw = response.content[0].text.strip()
    raw = re.sub(r"^```json\s*", "", raw)
    raw = re.sub(r"```$", "", raw).strip()
    return json.loads(raw)


# ---------------------------------------------------------------------------
# Force rank output
# ---------------------------------------------------------------------------

def render_master_rank(ranked: list[dict], today: str) -> str:
    lines = [
        f"# Feature Virality Force Rank — {today}",
        f"Total features ranked: {len(ranked)}",
        "",
        "## Scoring Key",
        "- **Adjusted Score** = viral_total × (6 − build_complexity) × csa_fit / 25",
        "- **Verdict**: BUILD_NOW | BUILD_LATER | SKIP",
        "",
        "---",
        "",
        "| Rank | Feature | Adj Score | Viral/20 | Complexity | CSA Fit | Verdict | Source |",
        "|:---:|---|:---:|:---:|:---:|:---:|:---:|---|"
    ]

    for i, r in enumerate(ranked, 1):
        s = r.get("scores", {})
        src = Path(r.get("source_file", "")).name
        lines.append(
            f"| {i} "
            f"| {r.get('feature_name', '?')} "
            f"| {r.get('adjusted_score', 0)} "
            f"| {r.get('viral_total', 0)} "
            f"| {s.get('build_complexity', '?')} "
            f"| {s.get('stockarithm_fit', '?')} "
            f"| {r.get('verdict', '?')} "
            f"| `{src}` |"
        )

    lines += [
        "",
        "---",
        "",
        "## BUILD_NOW List",
        ""
    ]

    build_now = [r for r in ranked if r.get("verdict") == "BUILD_NOW"]
    if build_now:
        for i, r in enumerate(build_now, 1):
            lines += [
                f"### {i}. {r.get('feature_name', '?')} (score={r.get('adjusted_score', 0)})",
                f"- **Top mechanic:** {r.get('top_viral_mechanic', '')}",
                f"- **Weakness:** {r.get('biggest_weakness', '')}",
                f"- **Source:** `{r.get('source_file', '')}`",
                ""
            ]
    else:
        lines.append("_No BUILD_NOW features yet._\n")

    lines += ["---", "", "## BUILD_LATER List", ""]
    build_later = [r for r in ranked if r.get("verdict") == "BUILD_LATER"]
    if build_later:
        for r in build_later:
            lines.append(
                f"- **{r.get('feature_name','?')}** (score={r.get('adjusted_score',0)}) — "
                f"{r.get('top_viral_mechanic','')}"
            )
        lines.append("")
    else:
        lines.append("_None._\n")

    lines += ["---", "", "## SKIP List", ""]
    skips = [r for r in ranked if r.get("verdict") == "SKIP"]
    if skips:
        for r in skips:
            lines.append(f"- {r.get('feature_name','?')} — {r.get('biggest_weakness','')}")
        lines.append("")
    else:
        lines.append("_None._\n")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--drafts-dir", default=DEFAULT_DRAFTS_DIR)
    parser.add_argument("--out", default=DEFAULT_OUT_DIR)
    parser.add_argument("--force-rescore", action="store_true",
                        help="Ignore cache and rescore everything")
    args = parser.parse_args()

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("ERROR: ANTHROPIC_API_KEY not set")
        sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key)
    cache = {} if args.force_rescore else load_cache(CACHE_FILE)

    draft_files = find_all_drafts(args.drafts_dir)
    print(f"Found {len(draft_files)} draft files")

    scored_count = 0
    cached_count = 0
    error_count = 0
    all_results = []

    for path in draft_files:
        fhash = file_hash(path)
        cache_key = str(path)

        if not args.force_rescore and cache_key in cache and cache[cache_key].get("_hash") == fhash:
            result = cache[cache_key]
            cached_count += 1
            print(f"  [cached] {path.name} — {result.get('verdict','?')} ({result.get('adjusted_score',0)})")
        else:
            print(f"  [scoring] {path.name} ... ", end="", flush=True)
            try:
                text = path.read_text(encoding="utf-8").strip()
                result = score_feature(client, text)
                result["source_file"] = str(path)
                result["_hash"] = fhash
                cache[cache_key] = result
                scored_count += 1
                print(f"{result.get('verdict','?')} ({result.get('adjusted_score',0)})")
            except Exception as e:
                print(f"ERROR — {e}")
                result = {
                    "feature_name": path.stem,
                    "source_file": str(path),
                    "adjusted_score": 0,
                    "viral_total": 0,
                    "verdict": "ERROR",
                    "top_viral_mechanic": "",
                    "biggest_weakness": str(e),
                    "scores": {},
                    "_hash": fhash
                }
                error_count += 1

        all_results.append(result)

    # Save updated cache
    save_cache(CACHE_FILE, cache)

    # Force rank by adjusted_score descending
    ranked = sorted(all_results, key=lambda x: x.get("adjusted_score", 0), reverse=True)

    # Write outputs
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    today = date.today().isoformat()

    json_path = out_dir / "master_rank.json"
    md_path = out_dir / "master_rank.md"

    # Clean results for output (strip internal _hash)
    clean = [{k: v for k, v in r.items() if k != "_hash"} for r in ranked]

    json_path.write_text(json.dumps(clean, indent=2))
    md_path.write_text(render_master_rank(clean, today))

    print(f"\nDone.")
    print(f"  Scored:  {scored_count} new")
    print(f"  Cached:  {cached_count}")
    print(f"  Errors:  {error_count}")
    print(f"  Total:   {len(ranked)} features ranked")
    print(f"  Output:  {md_path}")

    # Stdout summary
    build_now = [r for r in ranked if r.get("verdict") == "BUILD_NOW"]
    print(f"\nBUILD_NOW ({len(build_now)}):")
    for r in build_now:
        print(f"  - {r.get('feature_name','?')} (score={r.get('adjusted_score',0)})")


if __name__ == "__main__":
    main()
