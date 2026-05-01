# Content Engine V2 Spec

**Status:** Planned
**Target:** Saturday May 3, 2026
**Owner:** Claude Code

---

## Problem

The current content engine (`scripts/social_content_generator.py`) generates daily "lab report" style posts from the deep validation report. It works well for generic daily updates.

The new content schedule (CONTENT_SCHEDULE.md) requires **themed content**:
- Failure autopsies (May 20, June 17)
- Alt-data deep dives (May 9)
- Biscotti spotlights (May 16, June 3, June 28)
- Comparison posts (June 28)
- Macro series spotlights (June 14)

The current engine cannot produce themed content.

---

## Solution

Build a **parallel v2 engine** that:
1. Does NOT touch the existing engine
2. Copies the existing code to `content_v2/`
3. Adds theme support via `--theme` flag
4. Adds algo focus via `--focus-algo` flag
5. Outputs to a separate staging directory for inspection
6. Can be ignored if output sucks — operator uses Grok manually instead

---

## Directory Structure

```
content_v2/
├── social_content_generator.py   # Copy of original + theme/focus support
├── themes.py                     # Theme definitions (system prompts)
├── output/                       # Staged drafts for inspection
│   └── YYYY-MM-DD/
│       ├── reddit_algotrading.md
│       └── ...
└── README.md                     # Usage instructions
```

---

## Themes

Each theme modifies the system prompt to focus the LLM on a specific angle.

| Theme Key | Use Case | Prompt Focus |
|-----------|----------|--------------|
| `default` | Daily lab report | Current behavior (no change) |
| `failure_autopsy` | May 20, June 17 | Deep dive on worst performer, what went wrong, lessons |
| `alt_data_deep_dive` | May 9 | Focus on data sources, how they work, why they matter |
| `biscotti_spotlight` | May 16, June 3 | Focus entirely on Biscotti algo, story + numbers |
| `comparison` | June 28 | Biscotti vs top 3 other algos, side-by-side |
| `macro_spotlight` | June 14 | Pick one macro series (bankruptcies, freight, etc.) and explain |
| `positive_contrast` | May 28 | Focus on the boring signals that are quietly working |
| `monthly_recap` | May 31 | Summarize the full month: shifts, failures, surprises |

---

## New CLI Flags

```bash
# Default behavior (same as v1)
python content_v2/social_content_generator.py

# With theme
python content_v2/social_content_generator.py --theme failure_autopsy

# With algo focus (injects algo name into prompt)
python content_v2/social_content_generator.py --focus-algo biscotti

# Combined
python content_v2/social_content_generator.py --theme biscotti_spotlight --focus-algo biscotti

# Single channel
python content_v2/social_content_generator.py --theme failure_autopsy --channel reddit_algotrading

# Dry run (shows what would be generated)
python content_v2/social_content_generator.py --theme failure_autopsy --dry-run
```

---

## Output Location

V2 outputs to `content_v2/output/YYYY-MM-DD/` instead of `drafts/social/YYYY-MM-DD/`.

This keeps v1 and v2 completely separate. Operator can diff or inspect before using.

---

## Inspection Workflow

1. Run v2 with theme for the scheduled date
2. Open `content_v2/output/YYYY-MM-DD/reddit_algotrading.md`
3. If good → copy to clipboard, post
4. If sucks → open Grok, paste facts, write manually
5. Either way, the old engine keeps running untouched

---

## Implementation Steps

1. Create `content_v2/` directory
2. Copy `scripts/social_content_generator.py` to `content_v2/social_content_generator.py`
3. Create `content_v2/themes.py` with theme prompt definitions
4. Modify v2 generator to:
   - Import themes from `themes.py`
   - Accept `--theme` flag (default: `default`)
   - Accept `--focus-algo` flag (optional)
   - Output to `content_v2/output/` instead of `drafts/social/`
5. Create `content_v2/README.md` with usage examples
6. Test with `--dry-run` first
7. Generate sample output for May 7 theme and inspect

---

## Success Criteria

- [ ] V1 engine unchanged and still runs
- [ ] V2 produces themed output for at least 3 theme types
- [ ] Output is inspectable before use
- [ ] Operator can fall back to Grok if v2 output is bad
- [ ] No disruption to existing nightly content workflow

---

## Not In Scope (V2)

- Automatic schedule integration (knowing what theme to use on what day)
- Auto-posting to Reddit/X
- Replacing v1 — v2 is additive only

---

## Output Structure (Per Post)

Each v2 generation should output in this structure:

```
1. Internal Factual Seed — what actually happened in the lab that day
2. Public Hook / Title — Reddit-style headline
3. X Version — 1-3 short tweets + optional thread starter
4. Suggested Format — Deep Dive, Failure Autopsy, Snapshot, Personal Story, etc.
5. Engine Notes / Angle — who it's for, key emphasis
6. Visual Suggestion — leaderboard screenshot, chart, table, etc.
```

---

## Tone Guidelines (Baked Into Prompts)

- Honest, slightly self-deprecating, builder mindset
- Never hype results
- Always acknowledge small sample size / paper trading limitations
- Mix data + personality (Biscotti mentions help)
- For broader subs (r/stocks, r/investing): simpler language, no quant jargon
- End every Reddit post with 1-2 genuine questions to drive comments
- Never promise future performance

---

## X Tactics

- First 2 weeks: Heavy replying to other threads + low own posting
- Style: Short, visual, transparent, personality
- Goal: Drive clicks to site + mailing list, not immediate followers
- Keep under 280 characters per tweet
- Emojis used sparingly

---

## Dependencies

- `reports/deep_validation/latest.json` must exist (same as v1)
- `ANTHROPIC_API_KEY` environment variable
- Python 3.9 compatible (no `X | None` syntax)
