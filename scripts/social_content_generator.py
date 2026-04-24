#!/usr/bin/env python3
"""
social_content_generator.py

Generates daily channel-specific social media drafts from the deep validation
report. One LLM call per channel. All facts come from the report — nothing invented.

Outputs to drafts/social/YYYY-MM-DD/:
  reddit_algotrading.md
  reddit_investing.md
  reddit_stocks.md
  reddit_quant.md
  reddit_security_analysis.md
  twitter_x.md

Usage:
    python scripts/social_content_generator.py
    python scripts/social_content_generator.py --date 2026-04-24
    python scripts/social_content_generator.py --dry-run
    python scripts/social_content_generator.py --channel reddit_algotrading
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import date
from pathlib import Path

import anthropic

MODEL = os.getenv("ANTHROPIC_MODEL") or "claude-haiku-4-5-20251001"
REPORTS_DIR = Path("reports/deep_validation")
DRAFTS_DIR = Path("drafts/social")

_SHARED_RULES = """\
Hard rules (non-negotiable):
- Use ONLY facts present in the JSON data block. Do not invent metrics, returns, or reasons.
- Named algos stay named: Biscotti, Baileymol, etc. as they appear in the data.
- stockarithm.com is the URL. Never invent a different URL.
- Forbidden words: cutting-edge, proprietary algorithm, AI-powered, seamless, robust, revolutionary, game-changing, unlock your potential.
- Show losses as clearly as wins. The lab publishes failures publicly. That is the differentiator.
- No investment advice, no price predictions, no stock picks.
"""

CHANNELS = {
    "reddit_algotrading": {
        "filename": "reddit_algotrading.md",
        "system": f"""\
You are writing a Reddit post for r/algotrading for Stockarithm — a public paper-trading lab \
running alternative-data algorithmic signals.

{_SHARED_RULES}

Audience: engineers, quant hobbyists, algo traders. Highly skeptical. They will call out bullshit immediately.

Tone: lab notebook. Self-deprecating. Show your work.
- Lead with the pipeline setup and methodology — how many signals, what data sources, how you measure edge
- Be explicit about the failure rate (how many are NOT beating SPY — lead with this, not the wins)
- Show the force rank vs rolling 30D split and why both matter
- Invite criticism and questions in the last line
- Do NOT pitch a product. You are sharing an experiment.
- Reddit markdown is fine (headers, bold, bullet lists)

Length: 400-600 words. No filler. Real numbers from the data only.

End with: "Full leaderboard at stockarithm.com — all signals public, failures included."
""",
    },
    "reddit_investing": {
        "filename": "reddit_investing.md",
        "system": f"""\
You are writing a Reddit post for r/investing for Stockarithm — a public paper-trading lab \
running alternative-data algorithmic signals.

{_SHARED_RULES}

Audience: general retail investors. Less technical than r/algotrading. They care about results \
and whether signals actually work.

Tone: curious experimenter sharing results transparently.
- Lead with what the signals measure (economic data as sector rotation triggers) and what the results look like
- Minimal code or pipeline talk — focus on WHAT signals measure and HOW they performed
- Show wins AND failures prominently. The lab publishes both.
- Do NOT pitch a product. Frame it as a transparent public experiment.
- Reddit markdown is fine

Length: 300-400 words. Accessible. Real numbers from the data only.

End with: "Everything is public at stockarithm.com."
""",
    },
    "reddit_stocks": {
        "filename": "reddit_stocks.md",
        "system": f"""\
You are writing a Reddit post for r/stocks for Stockarithm — a public paper-trading lab \
running alternative-data algorithmic signals.

{_SHARED_RULES}

Audience: casual retail stock traders. They want the short version. Numbers first.

Tone: punchy, direct, zero jargon. Lead with the scoreboard immediately.
- First sentence: total signal count, how many beating SPY, how many getting wrecked
- Pick 2-3 specific named signals and their returns — the most interesting ones from the data
- One sentence on what makes this different (public lab, failures included)
- No methodology deep-dive

Length: 150-250 words. Short and readable.

End with: "stockarithm.com — leaderboard is public."
""",
    },
    "reddit_quant": {
        "filename": "reddit_quant.md",
        "system": f"""\
You are writing a Reddit post for r/quant for Stockarithm — a public paper-trading lab \
running alternative-data algorithmic signals.

{_SHARED_RULES}

Audience: quants, statisticians, finance academics. High bar. They will immediately ask \
about sample size, methodology flaws, and statistical significance.

Tone: precise and honest. Pre-empt the obvious critiques by naming them yourself.
- State the data sources explicitly (FRED, TSA, Reddit sentiment, job openings, etc.)
- Name the sample size limitation honestly — N days of live paper trading is not statistically \
  significant and say so directly
- Explain the two ranking systems: force rank (full-window since seed) vs rolling 30D momentum, \
  and why both are reported
- Show the spread: what fraction are actually beating SPY vs. underperforming
- Do NOT oversell the edge — the point is the methodology and the public transparency

Length: 400-500 words. Dense. Technical vocabulary is fine.

End with: "Methodology and full leaderboard at stockarithm.com."
""",
    },
    "reddit_security_analysis": {
        "filename": "reddit_security_analysis.md",
        "system": f"""\
You are writing a Reddit post for r/SecurityAnalysis for Stockarithm — a public paper-trading lab \
using economic leading indicators as sector rotation signals.

{_SHARED_RULES}

Audience: fundamental analysts, value investors, macro-focused traders. They care about the \
economic rationale and whether the underlying thesis is sound.

Tone: analytical and macro-framed. Less "weird algo," more "systematic sector rotation using \
economic leading indicators."
- Frame the signals as macro thesis tests: why would TSA checkpoint counts predict travel sector \
  rotation? Why would the misery index lead defensive positioning?
- Lead with the economic rationale, then the paper-trading result
- Reference the sector consensus from the report
- Use fundamental/macro vocabulary: sector rotation, leading indicators, signal confirmation, \
  thesis validation
- Avoid engineering or code language entirely

Length: 350-500 words. Thoughtful.

End with: "Full signal methodology and sector consensus at stockarithm.com."
""",
    },
    "twitter_x": {
        "filename": "twitter_x.md",
        "system": f"""\
You are writing a Twitter/X post (Fintwit style) for Stockarithm — a public paper-trading lab \
running alternative-data algorithmic signals.

{_SHARED_RULES}

Audience: finance Twitter. Data-literate, moves fast, responds to specific numbers and contrarian takes.

Tone: terse, specific, slightly provocative. No explanation. Let the stat do the work.
- Lead with ONE killer number or fact from the data
- Main tweet must be 280 characters or fewer
- Optionally add 2-3 thread tweets (each under 280 chars) if the data justifies it
- Use specific named algos when they are interesting (Biscotti, etc.)
- No hashtags except #algotrading or #fintwit if genuinely relevant
- stockarithm.com goes in the main tweet or thread 2

Format your output exactly as:
TWEET 1: [main tweet text, max 280 chars]
THREAD 2: [optional follow-up tweet]
THREAD 3: [optional follow-up tweet]
SCREENSHOT: [one sentence describing what to screenshot — leaderboard, a specific signal chart, etc.]
""",
    },
}


def _load_report(run_date):
    dated = REPORTS_DIR / f"{run_date}.json"
    latest = REPORTS_DIR / "latest.json"
    for path in (dated, latest):
        if path.exists():
            try:
                return json.loads(path.read_text())
            except Exception:
                continue
    return {}


def _build_facts_block(report):
    cf = report.get("content_facts", {})
    ss = report.get("system_state", {})
    fr = report.get("force_rank", {})
    r30 = report.get("rolling_30d", {})
    sc = report.get("sector_consensus", {})

    facts = {
        "report_date": report.get("report_date"),
        "system": {
            "total_algos": ss.get("total_algos"),
            "algos_beating_spy": ss.get("algos_beating_spy"),
            "algos_with_positions": ss.get("algos_with_positions"),
        },
        "top_force_ranked": (fr.get("top_algos") or [])[:5],
        "bottom_force_ranked": (fr.get("bottom_algos") or [])[:3],
        "top_rolling_30d": (r30.get("top_algos") or [])[:5],
        "signal_of_day": cf.get("signal_of_day"),
        "failure_of_day": cf.get("failure_of_day"),
        "call_of_day": cf.get("call_of_day"),
        "notable_divergences": (cf.get("notable_divergences") or [])[:3],
        "sector_consensus": (sc.get("sectors_ranked") or [])[:5],
    }
    return json.dumps(facts, indent=2)


def _generate_one(client, channel_key, channel_cfg, facts_block, run_date, out_dir):
    user_message = (
        f"Here are today's locked facts for {run_date}:\n\n"
        f"```json\n{facts_block}\n```\n\nWrite the post."
    )
    try:
        message = client.messages.create(
            model=MODEL,
            max_tokens=1024,
            system=channel_cfg["system"],
            messages=[{"role": "user", "content": user_message}],
        )
        draft = message.content[0].text.strip()
        out_path = out_dir / channel_cfg["filename"]
        out_path.write_text(draft)
        print(f"[social] wrote {out_path}")
    except Exception as e:
        print(f"[social] ERROR {channel_key}: {e}", file=sys.stderr)


def generate(run_date, dry_run=False, only_channel=None):
    report = _load_report(run_date)
    if not report:
        print(f"[social_content_generator] no report found for {run_date}", file=sys.stderr)
        return

    facts_block = _build_facts_block(report)
    out_dir = DRAFTS_DIR / run_date
    out_dir.mkdir(parents=True, exist_ok=True)

    if dry_run:
        print(f"[social_content_generator] dry-run for {run_date}")
        print(facts_block)
        channels = [only_channel] if only_channel else list(CHANNELS.keys())
        for key in channels:
            cfg = CHANNELS.get(key)
            if cfg:
                print(f"  would write: {out_dir / cfg['filename']}")
        return

    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("[social_content_generator] ANTHROPIC_API_KEY not set", file=sys.stderr)
        sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key)

    channels = {only_channel: CHANNELS[only_channel]} if only_channel else CHANNELS
    for channel_key, channel_cfg in channels.items():
        _generate_one(client, channel_key, channel_cfg, facts_block, run_date, out_dir)


def main():
    parser = argparse.ArgumentParser(description="Generate social media drafts from deep validation report")
    parser.add_argument("--date", default=None, help="YYYY-MM-DD (default: today)")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--channel", default=None,
                        choices=list(CHANNELS.keys()),
                        help="Generate only one channel (default: all)")
    args = parser.parse_args()

    run_date = args.date or date.today().isoformat()
    generate(run_date, dry_run=args.dry_run, only_channel=args.channel)


if __name__ == "__main__":
    main()
