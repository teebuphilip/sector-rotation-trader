# StockArithm Lab Report: 2026-05-05 — One Winner in 179 Algos

We're running 179 signals across 105 tickers in live paper trading. Today's snapshot: **1 algo is beating SPY on force rank. Zero are beating it on rolling 30D momentum.** This is the state of the lab right now, and it's worth examining honestly.

## The Setup

StockArithm publishes two ranking systems because they answer different questions:

1. **Force rank** (full-window since seed): cumulative alpha from day one. This is your long-term signal quality.
2. **Rolling 30D momentum**: recent performance, Sharpe-adjusted. This catches regime shifts and recent edge decay.

Both matter. Neither alone tells the full story.

## What's Working (Barely)

**Algo Baileymol (Chaos Monger)** is the sole force-rank winner: +1.38% alpha over 93 days, +7.62% YTD. It's also #1 on the 30D leaderboard with +6.15% return and a 3.19 Sharpe ratio—though that's still -3.69% behind SPY's 30D move. The algo is trading 105 tickers using alternative data signals (we'll detail methodology at stockarithm.com).

The next two—Faber Momentum Rotation and Antonacci Dual Momentum Sector Rotation—are both underwater relative to SPY, with -1.19% and -1.67% alpha respectively.

## The Brutal Part

Of 180 algos ranked on rolling 30D, **zero beat SPY**. SPY returned +9.84% in the last month. The top performer (Baileymol again) returned +6.15%. The median is deeply negative.

Bottom dwellers: Copper Momentum (-0.59% 30D), Liquor Store Leading Indicator (-0.20%), Google Gusts (-0.19%). These are "crazy" category signals—experimental, sourced from FRED, TSA mobility, Reddit sentiment, job openings, and other alternative data. Some work. Most don't. We publish them anyway.

## The Divergence Problem

Three algos show a striking pattern: strong recent 30D rank but weak full-window rank. **VIX Term Structure** ranks #177 force but #2 rolling 30D (+4.82% last month, -4.38% YTD). **VIX Fear Rotation** ranks dead last at #179 force but #7 rolling 30D. This is regime-dependent edge—it works now, failed before.

This is *exactly* the kind of divergence that should make you skeptical. A 175-rank gap between full-window and recent performance suggests either:
- The algo found a new edge in May 2026 (possible but unproven)
- It's curve-fit to recent market conditions (more likely)
- Sample size is too small to distinguish signal from noise (almost certainly true)

## Sector Consensus

Algos are 41% bullish on Technology (XLK), 22% on Consumer Defensive (XLP). Everything else is bearish. This is weak consensus—no sector has >50% bullish signals.

## The Honest Critique

93 days is not statistically significant. One winner in 179 algos could be luck. The lab's edge, if it exists, is in *methodology transparency*—we show losses as clearly as wins. We don't cherry-pick. We don't hide the 178 algos that are underwater.

If you're here to find the next 10-bagger, this isn't it. If you're here to study how alternative data signals perform in live conditions, with full failure disclosure, this is the lab.

**Methodology and full leaderboard at stockarithm.com.**