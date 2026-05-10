# Lab Report: 202 Signals Running, 1 Beating SPY (Force Rank)

We're running 202 algorithmic signals across 105 tickers. One is beating SPY on a force-ranked basis. That's the starting point.

## The Pipeline

Each signal generates a daily paper trade. We measure two things:

1. **Force Rank** — full-window performance since launch (96 days for most signals). This is your long-term edge test.
2. **Rolling 30D** — last 30 calendar days. This catches regime shifts and recent momentum that force rank might miss.

Both matter. They tell different stories.

## The Failure Rate (Lead With This)

**201 of 202 signals are NOT beating SPY on force rank.** That's 99.5% failure rate by the strictest measure.

On rolling 30D, it's slightly better: **202 of 203 signals are not beating SPY over the last month.** Still brutal.

Here's why we publish this: most algo labs hide the graveyard. We don't. If you're testing signals, you need to see what losing looks like at scale.

## The One Winner

**Quantified Simple Monthly Rotation** (`simple_monthly`):
- Force rank alpha: **+1.77%** vs SPY's +8.27%
- YTD: +10.03% (equity: $110,032.94)
- Rolling 30D: +10.03%, Sharpe 5.15, max drawdown -0.2%
- Days running: 96

It's also #1 on rolling 30D. Consistency matters.

## The Divergences (Why Both Metrics Matter)

Three signals show massive rank gaps between force rank and rolling 30D:

| Algo | Force Rank | 30D Rank | Gap | 30D Return |
|------|-----------|----------|-----|-----------|
| VIX Term Structure | 197 | 2 | 195 | +7.61% |
| VIX Fear Rotation | 199 | 3 | 196 | +4.60% |
| Baileymol (Chaos Monger) | 202 | 10 | 192 | +1.75% |

These three are *recently* working but have been underwater for months. Are they regime-dependent? Luck? Too early to call. But the gap is the signal.

## The Basement

**Baileymol** is the force-rank failure of the day:
- YTD: -6.2%
- Full-window alpha: -14.46%
- But 30D rank: #10 (+1.75%)

**Biscotti** (Unconditional Loyalty) is also struggling:
- YTD: -3.94%
- Force rank: 200
- 30D rank: 200 (consistent loser)

Both are "crazy" type signals (alternative data experiments). They're not hiding.

## Sector Consensus

Across all 202 signals, Technology (XLK) is the only sector with bullish lean: 41% of signals bullish, composite "MIXED." Everything else is red — Consumer Defensive, Utilities, Materials, Industrials all under 20% bullish.

This is consensus, not prediction. It's what the lab is seeing *right now*.

## What We're Not Claiming

- No alpha discovery here yet (1 winner ≠ edge)
- No regime prediction (sector consensus is descriptive, not prescriptive)
- No stock picks (we trade sector ETFs and indices)

## What We're Asking

If you're running signals at scale, what's your failure rate? How do you separate regime-dependent wins from real edge? And what would make you trust a leaderboard that *doesn't* show the losses?

Full leaderboard at stockarithm.com — all signals public, failures included.