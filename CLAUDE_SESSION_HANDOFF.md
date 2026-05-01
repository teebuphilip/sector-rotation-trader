# Session Handoff — 2026-04-29

## Where We Are

Free public launch + Reddit: May 15. July 1 = traction review / paid-path decision, not an automatic paid open.

**Single most important thing before May 15:** MailerLite signup form live on the landing page. Nothing else matters if people can't sign up.

## Added This Session (2026-04-29)

- **4 Claude Code Routines scheduled** (automatic, no maintenance needed):
  - Saturday 1am EST: code review → GitHub issues for `new-courtdominion` and `dbb2-engine`
  - Sunday 1am EST: code review → GitHub issues for `sector-rotation-trader`
  - Sunday 2am EST: content + website review → GitHub issues for `sector-rotation-trader`
  - Manage at: https://claude.ai/code/scheduled

- **Launch drafts written** — `drafts/launch/`:
  - `may15_reddit_algotrading.md` — ready to post, update "Why I'm posting" in your own words
  - `june1_subscriber_email.md` — first email to list, fill in brackets
  - `july1_paid_open.md` — paid open email + Reddit follow-up, fill in price and real numbers

- **WFO feature PRD added** — `drafts/features/2026-04-29/anthropic-feature-01-walk-forward-backtest.md` — gets auto-scored Friday, targets v1.1 ~Aug 20

- **Feature scoring system confirmed running** — `reports/virality/master_rank.md` has 20 features scored, 15 are BUILD_NOW. Top pick for July blitz: Receipts Guy's Trade History Scroll (score 11.2).

- **First session rule saved to memory**: Every session opens with "how do we get signups?" before any code/ops work.

## Immediate Stack (in order)

1. **Thesis text for top 10 algos** — Teebu writes, not code. 10 sentences, lab-notebook voice.
   - Pattern: "**Biscotti (Unconditional Loyalty)** — Bets that when consumer sentiment collapses, defensive sectors absorb the rotation first. Good month. Bad long-run record. Still running."
   - Do NOT use Chat's "Tests whether X predicts Y" voice — sounds generic.
   - Before writing: verify Biscotti's actual signal logic (it's top rolling-30D, not mean reversion).
   - Before writing: check FINRA Dark Pool Signal sourcing — if shaky, swap it out.

2. **Ops/pipeline integrity deep scan** — Sunday Apr 27 (Quality Check #3 on CSV).

3. **Landing page copy pass** — Tuesday Apr 29.
   - Agreed outline: hero sharpening, proof strip, "What you're looking at" block with Biscotti hook.
   - Biscotti hook: "Each row is one live paper-traded signal. Some are working. Some are failing. One of them is named after my dog. That is the point."
   - Drop the free/paid bridge section entirely.
   - Do after Yahoo pipeline stabilizes.

## Due Dates from CSV

- Apr 27: Quality Check #3
- May 12: Update landing page with real content
- May 14: MailerLite setup
- May 15: Write Biscotti origin email + Reddit first post
- May 19: Polygon runtime-only migration sprint (post-launch)

## May 15 Reddit Post Checklist

- Run `python scripts/refresh_reddit_drafts.py --date 2026-05-15` day before
- Add personal questions to algotrading.md and quant.md manually
- Check Biscotti line is current
- Rewrite macro note in security_analysis.md by hand (script keeps it neutral)

## Key Architecture Facts

- Force rank = `data/rank_history.csv` (full-window since seed, long-term trust)
- Rolling 30D = `docs/leaderboards/rolling_30d.json` (recent momentum)
- Public contract = `docs/data/public/` (schema v1, feeds static pages)
- Reddit draft templates = `drafts/reddit_launch/*.md`, refreshed daily by `reddit_draft_refresh.yml` until May 15
- Social drafts (daily) = `drafts/social/YYYY-MM-DD/` via `scripts/social_content_generator.py`
- Deep validation = `reports/deep_validation/latest.json` (source of truth for content)

## Deferred (Post May 15)

- Polygon runtime-only migration (week of May 19): snapshot builder → 4 runtime consumers → 7-day shadow run → flip
- Bucket Thesis Statement feature: Teebu writes copy, wire as data field, ship before June 15 second Reddit post
- needs_history 80 algos: NOT a Polygon problem — alt-data signals can't be backtested regardless of price provider

## Urgent May 2-4

- Pre-8:30am on `2026-05-02`: move durable algo-page rendering into `dashboard.py`
- Pre-8:30am on `2026-05-03`: validate rebuilt preview algo pages after overnight refresh
- Pre-8:30am on `2026-05-04`: finish minimizing `scripts/build_vercel_preview_site.py` into a thin bundler only
- Goal: preview builder stays temporary glue; lasting algo-page logic lives in `dashboard.py` + `algo_copy_registry.py`

## Claude Code Situation

- Old laptop, Claude Code upgraded, can't restart
- Current session running in RAM
- If it dies: uninstall, reinstall older version
- On restart: read this file + MEMORY.md + tldr-architecture.md to rebuild context
- Then `/compact` and start fresh

## Files to Read on Restart

1. `SESSION_HANDOFF.md` (this file)
2. `~/.claude/projects/.../memory/MEMORY.md`
3. `tldr-architecture.md`
4. `stockarithm_execution_plan.csv`
