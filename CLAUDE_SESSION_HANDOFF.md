# Session Handoff — 2026-05-01

## Where We Are

Free public launch + Reddit: May 15. July 1 = traction review / paid-path decision.

**Single most important thing before May 15:** MailerLite signup form live on the landing page.

---

## Completed This Session (2026-05-01 evening)

**Marketing strategy locked:**
- Full content schedule committed: `CONTENT_SCHEDULE.md` (May 7 – July 1)
- First post May 7 (r/algotrading), launch May 15, IndieHackers May 16
- Reddit cadence: 3-4 posts/week across r/algotrading, r/quant, r/SecurityAnalysis, r/investing, r/stocks
- X cadence: 4-7 posts/week, reply-first strategy for first 2 weeks
- Success metrics defined: 50+ upvotes = good, <25 after 24h = flop, slow down

**Drafts ready:**
- `drafts/launch/indiehackerspost.05162026.txt` — Biscotti story for IndieHackers
- `drafts/launch/x_post_samples.md` — 4 X post templates (lab update, Biscotti spotlight, failure mention, alt data hook)
- `drafts/launch/grok_strategy_prompt.txt` — strategy prompt used for schedule review
- May 7 r/algotrading post ready (from Codex, reviewed by Claude/Gemini/Grok)

**Content engine v2 planned:**
- Spec at `specs/content_v2_spec.md`
- Parallel engine with `--theme` and `--focus-algo` flags
- Does NOT touch existing v1 engine
- Outputs to `content_v2/output/` for inspection
- If v2 sucks, operator uses Grok manually
- Scheduled for build: **Saturday May 3**

---

## Immediate Stack (in order)

1. **May 2 pre-8:30am:** Move durable algo-page rendering into `dashboard.py`
2. **May 3 (Saturday):** Build content engine v2 (spec ready)
3. **May 3 pre-8:30am:** Validate rebuilt preview algo pages
4. **May 4 pre-8:30am:** Minimize `build_vercel_preview_site.py` to thin bundler
5. **May 4:** Quality Check #4 — first real signal check, comparator patterns
6. **May 5:** MailerLite verification/update (Critical)
7. **May 7:** First Reddit post (r/algotrading)

---

## Key Files Added This Session

| File | Purpose |
|------|---------|
| `CONTENT_SCHEDULE.md` | Full posting schedule May 7 – July 1 |
| `specs/content_v2_spec.md` | Content engine v2 spec |
| `drafts/launch/indiehackerspost.05162026.txt` | IndieHackers Biscotti post |
| `drafts/launch/x_post_samples.md` | X post templates |
| `drafts/launch/grok_strategy_prompt.txt` | Strategy prompt for LLM review |

---

## Session Rules

- Every session opens with "how do we get signups?"
- Grok is better for social hooks/timing, Claude is better for scope control
- Gemini is being set up as personal assistant — needs visibility into schedule

---

## Architecture Reminder

- Content engine v1: `scripts/social_content_generator.py` → `drafts/social/YYYY-MM-DD/`
- Content engine v2 (to build): `content_v2/` → `content_v2/output/YYYY-MM-DD/`
- Deep validation report: `reports/deep_validation/latest.json`
- Force rank: `data/rank_history.csv`
- Rolling 30D: `docs/leaderboards/rolling_30d.json`

---

## Files to Read on Restart

1. `CLAUDE_SESSION_HANDOFF.md` (this file)
2. `CONTENT_SCHEDULE.md`
3. `specs/content_v2_spec.md`
4. `stockarithm_execution_plan.csv`
5. `tldr-architecture.md`
