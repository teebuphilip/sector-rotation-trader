# StockArithm Lab Report: When Sector Rotation Signals Diverge

We're running 133 signals across 105 tickers, and today's results show a sharp split: two algos are beating SPY, 131 are not. Here's what's actually happening.

## The Winners (and They're Narrow)

**Baileymol** (Chaos Monger) is up 7.06% YTD and returned 7.87% over the last 30 days—beating SPY's 8.70% by a small margin. It's ranked #1 on the rolling 30-day leaderboard with a Sharpe of 4.84.

**DMSR** (Antonacci Dual Momentum Sector Rotation) is up 5.29% YTD, also beating SPY. It measures momentum across sectors and rotates into the strongest performers. Over 30 days it returned 4.2%, trailing SPY but holding a solid force rank of #2 overall.

Both have been running 83 days. Both are real wins. Both are also small edges.

## The Failures (and They're Loud)

**VIX Fear Rotation** is down 6.7% YTD and ranks dead last (#133). **Biscotti** (Unconditional Loyalty) in its "crazy" variant is down 2.51% YTD. **VIX Term Structure** is down 4.88% YTD despite ranking #3 on the 30-day board—a stark divergence showing recent strength masking longer-term underperformance.

The lab publishes these openly. That's the point.

## The Divergence Story

Three algos show wild rank gaps between full-window and recent 30-day performance:

- **Faber Momentum Rotation**: Force rank #3 overall, but #134 (dead last) in the last 30 days. It's up 3.85% YTD but has gone flat recently.
- **Biscotti** and **VIX Term Structure**: Both weak on full-window returns but strong in the last month. Recent tailwinds, not sustained edges.

## Sector Consensus: Mostly Bearish

Across 18 signals measuring sector rotation, only 33% are bullish on Consumer Defensive (XLP). Technology, Industrials, and Consumer Cyclical are all below 33% bullish. The lab's sector consensus is bearish across the board.

## What This Means

Two signals beat a 4.79% market return in 83 days. The rest didn't. Some recent winners may be riding short-term momentum, not structural edges. Sector rotation signals are currently tilted bearish, but that's a consensus call, not a prediction.

The lab runs 133 different approaches to see which actually work. Most don't. Some do, barely. That transparency is the experiment.

Everything is public at stockarithm.com.