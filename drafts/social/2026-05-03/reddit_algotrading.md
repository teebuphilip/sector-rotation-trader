# Lab Report: 167 Signals, 1 Beating SPY — What's Breaking

**TL;DR:** We're running 167 force-ranked algos across 105 tickers. One is ahead of SPY. Zero are beating it on the rolling 30-day window. The lab is publishing all of it.

---

## The Pipeline

Each signal runs on a 89-day window (most launched mid-February). We measure two things:

1. **Force rank** — full-window cumulative return vs. SPY, ranked 1–167
2. **Rolling 30D rank** — last 30 days only, separate leaderboard

Why both? Force rank shows staying power. Rolling 30D catches regime shifts and recent momentum. They often disagree wildly. That disagreement is the data.

**Data sources:** Mix of momentum, sector rotation, alternative data (Google Trends, electricity consumption, dark pool signals), and volatility structure. Some are labeled "normal," others "crazy" — the latter are experimental signals we expect to fail more often.

---

## The Failure Rate (Lead with This)

- **166 of 167 algos are underwater vs. SPY on force rank.** SPY returned 5.77% YTD. 
- **168 rolling 30D algos tracked. Zero beat SPY's 9.98% return in the last 30 days.**

That's the story. Everything else is noise.

---

## The One Winner

**Algo Baileymol (Chaos Monger)** — +6.87% YTD, +1.1% alpha vs. SPY.

- Equity: $106,870
- Days running: 89
- Rolling 30D: +4.55% (Sharpe 3.03), SPY delta –5.43%
- Rank jump: 157 → 1 (yes, really)

This is a normal-type momentum signal. It's also #1 on the rolling 30D leaderboard. But one winner out of 167 is not a pattern — it's a data point. We're watching it.

---

## The Divergence Problem

Three algos show a weird split: strong recent 30D performance, weak full-window rank.

| Algo | Force Rank | Rolling 30D | Rank Gap | 30D Return |
|------|-----------|-----------|----------|-----------|
| VIX Term Structure | 165 | 2 | 163 | +4.28% |
| Chaos Rotation Lab | 166 | 3 | 163 | +3.75% |
| Biscotti (Normal) | 164 | 5 | 159 | +3.09% |

All three are beating SPY *this month* but losing YTD. This suggests either:
- Recent regime favors their logic (temporary)
- They were deeply underwater and just recovering (mean reversion)
- The 89-day window is too long to catch their edge

We don't know yet. That's why we publish both.

---

## The Failures

**VIX Fear Rotation** is the worst: –12.56% alpha, –6.79% YTD, rank 167.

**Biscotti (Unconditional Loyalty)** variants are in the bottom 5 on force rank (–8.6% and –8.9% alpha) but somehow rank #5 on rolling 30D (+3.09% last month). This is the divergence problem in action.

**Google Gusts** and **Weekly Google Trends Fast Food Job Openings** both returned near-zero in the last 30 days with negative Sharpe ratios. Alternative data is not magic.

---

## Sector Consensus

31 signals vote on 5 sectors. Technology (XLK) is the only mixed signal (39% bullish). Everything else is bearish: Utilities, Consumer Defensive, Industrials, and Consumer Cyclical all under 21% bullish.

---

## What We're Not Claiming

- These algos will keep working
- One winner validates the methodology
- Alternative data beats price action
- You should trade any of this

What we *are* doing: running signals live, measuring them honestly, and showing you the corpses.

---

**Full leaderboard at stockarithm.com — all signals public, failures included.**

What's your read on the force rank /