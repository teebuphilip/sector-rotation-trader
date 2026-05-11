# Lab Report: 202 Signals Running, 1 Beating SPY (Force Rank)

We're running 202 algorithmic signals across 105 tickers. As of May 8, **only 1 is beating SPY on force rank**. That's the actual state of the lab. Everything else is underwater or treading water.

## The Setup

Each signal generates a daily trade recommendation. We measure two things:

1. **Force Rank** — cumulative return from day 1 (96 days in for most signals). This is the long-term scoreboard.
2. **Rolling 30D** — last 30 calendar days of returns. This catches recent regime shifts and momentum reversals.

Both matter. Force rank tells you if an idea has legs. Rolling 30D tells you if it's *currently* working.

## The Failure Rate (Lead with This)

**201 of 202 signals are NOT beating SPY on force rank.** That's 99.5% failure.

The one winner:

- **Quantified Simple Monthly Rotation** (`simple_monthly`): +10.03% YTD vs SPY's +8.27%. Alpha: +1.77%. Equity: $110,032.94 (96 days running).

The rest are negative alpha. Here's the top 5 by force rank return:

| Algo | YTD Return | Alpha | Days Running |
|------|-----------|-------|--------------|
| Quantified Simple Monthly Rotation | +10.03% | +1.77% | 96 |
| Algo Baileymol (Chaos Monger) | +7.54% | -0.72% | 96 |
| Faber Momentum Rotation | +5.01% | -3.25% | 96 |
| Antonacci Dual Momentum Sector Rotation | +4.66% | -3.61% | 96 |
| Uber Mobility Index | +4.37% | -3.89% | 95 |

At the bottom: **Algo Biscotti** (-3.94% YTD, -12.21% alpha), **VIX Fear Rotation** (-3.2% YTD, -11.46% alpha), **Electricity Consumption** (-2.02% YTD, -10.29% alpha).

## The Rolling 30D Split

This is where it gets interesting. The 30-day leaderboard shows **different winners**:

1. **Quantified Simple Monthly Rotation**: +10.03% (30D), Sharpe 5.15
2. **VIX Term Structure**: +7.61% (30D), Sharpe 5.26 — but force rank #197
3. **VIX Fear Rotation**: +4.60% (30D), Sharpe 3.38 — but force rank #199

**Notable divergence:** Baileymol ranks #202 on force rank (YTD: -6.2%) but #10 on rolling 30D (+1.75% last month). It's either recovering or noise. We'll watch.

SPY returned +9.11% over the last 30 days. Most signals are lagging.

## Why Both Metrics Matter

Force rank catches structural edge. Rolling 30D catches tactical shifts. When they diverge (like VIX Fear Rotation: 196-rank gap), you're either looking at a regime change or a signal that's finally working after months of failure. The lab publishes both so you can decide which to trust.

## The Sector Consensus

Across all 202 signals, Technology (XLK) is the only sector with mixed bullish lean: 41% of signals bullish. Everything else is bearish — Utilities, Consumer Defensive, Basic Materials, Industrials all under 20% bullish.

## What We're Not Claiming

No edge here is "working." One signal beat SPY. The rest are learning what doesn't work. That's the lab.

---

**Full leaderboard at stockarithm.com — all signals public, failures included.**

What's your read on the force rank vs. rolling 30D split? Are you tracking any of these signals yourself?