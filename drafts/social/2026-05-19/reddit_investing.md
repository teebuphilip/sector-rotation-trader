# StockArithm Lab Report: 292 Signals Running, Only 3 Beating SPY

We're running 292 alternative-data signals across 105 tickers in our public paper-trading lab. Today's snapshot: **only 3 are beating SPY year-to-date**. That's the reality of signal testing at scale.

## What's Working (Barely)

**Quantified Simple Monthly Rotation** leads the pack with **+8.6% YTD** vs SPY's **+7.69%**—a 0.91% alpha edge. It's been running 103 days and ranks #1 on the 30-day leaderboard with a 3.9 Sharpe ratio. The signal measures sector rotation based on monthly momentum cycles.

**Algo Baileymol (Chaos Monger)** just climbed 276 spots to #2 overall, posting **+8.23% YTD** with 0.54% alpha. It was ranked 278th two weeks ago. This is the lab's transparency in action—we show the winners *and* the ones that suddenly work after months of failure.

**Faber Momentum Rotation** rounds out the winners at **+7.76% YTD**, measuring sector momentum on a rolling basis. Minimal alpha (0.07%), but it's consistent.

## What's Failing (Loudly)

**Copper Momentum**, **Port Container Volume**, and **VIX Fear Rotation** are down 3–5% YTD. These measure commodity cycles and volatility structure—real economic signals that simply haven't worked this year. We publish these losses publicly because that's how you learn what *doesn't* work.

The standout failure: **Chaos Rotation Lab** (Baileymol's sister signal) is down **-5.96% YTD**, ranked dead last. Same data source, opposite results.

## The Divergence Story

Three signals show a wild pattern: **VIX Fear Rotation** ranks #290 all-time but #3 in the last 30 days (+2.8%). **Biscotti (Unconditional Loyalty)** is #282 overall but #8 in the rolling window. These are signals that *just started working*—or got lucky recently. We flag these divergences because they matter for live trading.

## Sector Consensus: Bearish Across the Board

Our 292 signals vote on sector rotation. Today's consensus: **bearish on everything**. Utilities (XLU) shows the highest bullish percentage at just 25%. Tech, Industrials, and Consumer Defensive all below 20%. This isn't a prediction—it's what the signals are measuring in real time.

## The Bottom Line

Out of 292 signals, 2 are beating SPY on a rolling 30-day basis. The lab publishes wins, losses, and the weird divergences in between. No hype. Just data.

Everything is public at stockarithm.com.