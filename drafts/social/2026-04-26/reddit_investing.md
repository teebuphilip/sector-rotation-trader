# StockArithm Lab Report: When Sector Rotation Signals Clash with Market Reality

We're running 133 signals across 105 tickers, and the results are messy—which is exactly why we publish them.

## The Setup

Most of our algos measure sector rotation using economic data: retail sales momentum, dark pool activity, VIX term structure, dual momentum across sectors. The idea is simple—when economic conditions shift, capital rotates. These signals should catch that rotation early.

**The problem:** Only 2 out of 133 signals are beating SPY right now. SPY is up 4.79% over the past month. Most of our lab is lagging.

## What's Working (Barely)

**Baileymol (Chaos Monger)** is the outlier. It's up 7.06% YTD with a 2.28% alpha over SPY. Over the last 30 days, it returned 7.87% vs SPY's 8.70%—a small miss, but it's the only signal consistently in the green across both timeframes. Sharpe ratio of 4.84 over 30 days.

**DMSR (Antonacci Dual Momentum Sector Rotation)** is second, up 5.29% YTD with 0.5% alpha. It's measuring momentum across sectors and holding up, though it's also trailing SPY in the recent window.

## What's Failing Loudly

**VIX Term Structure** is down 4.88% YTD and -9.67% alpha. **Biscotti (Unconditional Loyalty)** in its "crazy" variant is down 2.51% YTD. **VIX Fear Rotation** is the worst performer at -6.7% YTD, ranked dead last.

The fringe signals—earthquake activity near logistics hubs, electricity consumption, XLE rebound patterns—are all underwater. These aren't close calls. They're failing.

## The Divergence

Here's what's interesting: **Biscotti** is ranked #129 overall but #2 in the last 30 days (7.31% return). **VIX Term Structure** is ranked #131 overall but #3 in the last 30 days (5.32% return). Something shifted recently that these signals caught, but they've been wrong for months.

Meanwhile, **Faber Momentum Rotation** is ranked #3 overall but #134 in the last 30 days. It's been right historically but is breaking down now.

## The Sector Call

Across 18 signals measuring sector consensus, only 33% are bullish on Consumer Defensive (XLP). Technology is at 32% bullish. Everything else is below 25%. The lab is broadly bearish, but that bearishness hasn't translated to outperformance.

## What This Means

Economic data signals work until they don't. Sector rotation is real, but timing it is hard. We're publishing both the wins and the failures because that's the only way to know if a signal actually works or just got lucky.

Everything is public at stockarithm.com.