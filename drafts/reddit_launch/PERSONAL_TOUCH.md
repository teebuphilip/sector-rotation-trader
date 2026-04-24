# What Needs Your Voice Before Posting

The numbers are filled in by the script. These are the parts where you — not an LLM — need to decide what to say.

---

## The Biscotti Decision (affects ALL 5 posts)

Every post mentions Biscotti and the fact that it's named after your dog who died in April 2025.

**You need to decide how much you want to say.**

The current drafts use: *"named after my dog, who died in April 2025 while I was building the first version of this."*

That sentence is doing real work — it's the thing that makes the whole project feel human and not like another fintech dashboard. But it's your call how much you want to share about that publicly and on post day.

Options:
- Leave it as-is (probably the right call)
- Expand it by one sentence if you feel like it
- Cut it to just "named after my late dog Biscotti" if you don't want to go there on day one

Don't overthink it. The shorter version still works.

---

## r/algotrading — Needs the Most Work

**The "Why I'm posting" section at the bottom.**

Currently reads as 3 generic questions. Replace at least one with something you're *actually* puzzling over right now. Something that came up in a quality check, a signal that's behaving weirdly, a methodology choice you're unsure about.

The r/algotrading crowd will smell generic questions from a mile away. One specific "I genuinely don't know the answer to this" question is worth more than three polished ones.

Also: **the title**. It's good but you can sharpen it if something more specific is on your mind that day.

---

## r/quant — The 3 Questions at the Bottom

Same issue as r/algotrading. The 3 questions I wrote are technically reasonable but they're not *your* questions.

Before you post, read through the questions and ask yourself: do I actually want to know these answers? If yes, keep them. If not, replace with what you're actually wondering about the methodology.

---

## r/investing and r/stocks — Minimal Touch Needed

These are almost post-ready as-is after the numbers refresh.

The only thing to check: does the Biscotti sentence feel right on post day? If something bigger has happened with that algo by May 15 (good run, bad run, something interesting), update that one line to reflect the current state.

---

## r/SecurityAnalysis — Check the Macro Commentary

The post includes: *"internally consistent with a late-cycle, risk-off positioning read."*

That line is based on today's data (XLK mixed, XLP/XLI bearish). On May 15, the sector consensus will be different. Update that sentence to match whatever the leaderboard is actually saying about sector positioning that week. Don't leave stale macro commentary.

---

## The One Rule Across All Posts

Never sound like a founder marketing a product. You're a builder sharing an experiment.

The moment you catch yourself writing something that sounds like a press release, delete it.

---

## Workflow

```bash
# 1. Refresh numbers (run day before posting)
python scripts/refresh_reddit_drafts.py --date 2026-05-15

# 2. Open the dated folder
open drafts/reddit_launch/2026-05-15/

# 3. Edit algotrading.md and quant.md (add your personal questions)
# 4. Check the Biscotti line across all 5
# 5. Update the macro line in security_analysis.md
# 6. Post r/algotrading first, then the others over the following days
```
