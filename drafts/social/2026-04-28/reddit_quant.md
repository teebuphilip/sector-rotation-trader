# StockArithm Lab Report: 2026-04-28 — When Full-Window and Recent Performance Diverge Sharply

We're running 138 live signals across 105 tickers. SPY returned 4.46% YTD. Here's what the data shows, and what it doesn't.

## The Headline Numbers (With Caveats)

**Force rank (full-window since seed):** Only 2 of 138 algos are beating SPY. Baileymol (Chaos Monger) leads with +1.04% alpha over 85 days; DMSR (Antonacci Dual Momentum Sector Rotation) follows at +0.5%. The median algo is underwater. VIX Fear Rotation sits at rank 138, down 12.18% YTD.

**Rolling 30-day momentum:** Zero algos beat SPY in the last month. SPY returned 12.61% in 30 days. The top performer, Algo Biscotti (Unconditional Loyalty), returned 7.90% — a 4.7% drag. This is the critical observation: recent market conditions have been hostile to the signal set.

## The Divergence Problem

This is where methodology transparency matters. We report both rankings because they tell different stories:

- **Baileymol (Chaos Rotation Lab):** Rank 137 force, rank 3 rolling 30D. It's been a drag over 84 days but has caught fire in the last month (+4.54%, Sharpe 2.65).
- **Faber Momentum Rotation:** Rank 3 force, rank 139 rolling 30D. Solid 85-day track record (+3.85% YTD) but collapsed in the last 30 days (−1.14%).
- **Algo Biscotti (Unconditional Loyalty):** Rank 134 force (−1.89% YTD), rank 1 rolling 30D (+7.90% in 30 days). The signal is either recovering or the full-window sample is too noisy to trust.

**Sample size problem:** 85 days is ~17 weeks. That's not statistically significant for equity strategy validation. A single month of outperformance doesn't reverse a YTD loss. We're publishing this anyway because the point is transparency, not hype.

## Data Sources & Signal Composition

The 138 signals mix standard momentum/rotation algos (Faber, DMSR, Baileymol variants) with alternative-data experiments: FINRA dark pool flow, Uber mobility indices, electricity consumption, lumber futures, VIX term structure. The "crazy" category is explicitly experimental. Some will fail. VIX Term Structure is down 6.5% YTD; Lumber Momentum is down 0.88% in 30 days.

## Sector Consensus

Across the signal set, Technology (XLK) shows the weakest bearish lean: 40% bullish, composite MIXED. Everything else is red. Consumer Cyclical (XLY), Utilities (XLU), and Industrials (XLI) all show <25% bullish signals. This is a defensive posture, not a market call.

## What This Isn't

- No prediction of future returns.
- No claim that 2 winners out of 138 proves an edge.
- No explanation of *why* the signals work (that's the research phase).
- No recommendation to trade any of these.

## What This Is

A live leaderboard of 138 paper-trading experiments, updated daily, with losses shown as prominently as wins. Methodology and full leaderboard at **stockarithm.com**.