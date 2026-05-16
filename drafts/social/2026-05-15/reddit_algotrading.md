# Lab Report: 266 Signals, 1 Winner. Here's What We're Seeing.

**TL;DR:** One algo is beating SPY across both force rank and rolling 30D. The other 265 are not. We're publishing all of it.

---

## The Setup

We're running 266 signals across 105 tickers. Each signal gets two scorecards:

1. **Force rank** — full-window cumulative performance (101 days running for most)
2. **Rolling 30D** — last 30 calendar days only

Why both? Force rank shows staying power. Rolling 30D catches regime shifts. They often disagree wildly, and that disagreement is where the lab gets interesting.

SPY returned **5.60%** over the last 30 days. **8.49%** YTD.

---

## The Failure Rate (Lead With This)

**265 of 266 algos are underperforming SPY on force rank.**

That's a 99.6% failure rate by the metric that matters most — can you beat the benchmark over time?

The one winner:

- **Quantified Simple Monthly Rotation** (`simple_monthly`)
  - Force rank alpha: **+2.0%**
  - YTD: **+10.5%** vs SPY **+8.49%**
  - Equity: $110,496.84 (started at $100k)
  - 101 days running
  - Rolling 30D Sharpe: **4.51** (SPY delta: +4.89%)

Everything else is red. Baileymol, Faber, DMSR, Uber Mobility Index — all negative alpha. The bottom dwellers (Biscotti variants, VIX Fear Rotation, Lumber Momentum) are down 2–12% YTD while SPY climbs.

---

## The Divergence Problem

Here's where it gets messy. Some algos rank *terrible* on force rank but *decent* on rolling 30D:

| Algo | Force Rank | Rolling 30D | Gap | 30D Return |
|------|-----------|-----------|-----|-----------|
| VIX Fear Rotation | 264 | 2 | 262 | +5.17% |
| VIX Term Structure | 260 | 3 | 257 | +4.75% |
| Biscotti | 262 | 9 | 253 | +2.30% |

These three are *recently* outperforming. But they're still underwater YTD. The question: is this mean reversion, or did they find a new edge in the last month?

**We don't know yet.** That's the point of publishing both metrics.

---

## What the Sector Consensus Says (Not Much)

Across 46 signals covering Industrials (XLI), only 14 are bullish. That's 30% — the highest conviction sector in the lab. Everything else is 12–19% bullish.

**Composite stance: bearish across all major sectors.**

This doesn't predict price. It's just a snapshot of what the algos are positioning into.

---

## The Failure of the Day

**Chaos Rotation Lab** (`baileymol`) dropped from rank 251 to rank 2 in alpha — a 249-position swing in one day. It's now the worst performer on force rank, down 6.1% YTD while SPY is up 8.49%.

This is what happens when you run 266 experiments. Some will crater. We're showing you the crater.

---

## Open Questions

- Why is `simple_monthly` the only consistent winner? Is it luck, or does monthly rebalancing have an edge in this regime?
- Are VIX-based signals catching a real 30D bounce, or is this noise before another drawdown?
- What happens to the 265 losers if we extend the window to 6 months? 1 year?

**Full leaderboard at stockarithm.com — all signals public, failures included.**

What's your read on the force rank vs. rolling 30D split? Are you seeing similar divergences in your own backtests?