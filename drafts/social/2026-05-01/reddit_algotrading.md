# Lab Report: 158 Signals, 1 Winner, 0 in the Last 30 Days

We're running 158 alternative-data signals across 105 tickers. Today's snapshot: **157 are underwater vs. SPY**. One algo is beating the benchmark on force rank. Zero are beating it on the rolling 30-day window.

This is the experiment. This is what we publish.

## The Setup

**Force rank** = full-window cumulative return since launch (88 days for most signals). **Rolling 30D** = last month only, with Sharpe and max drawdown. Both matter because they answer different questions: *Does this signal work at all?* vs. *Is it working right now?*

SPY returned **9.98%** in the last 30 days. Our median signal returned... less.

## The One Winner

**Algo Baileymol (Chaos Monger)** is the sole force-rank outperformer:
- **+6.87% YTD** vs. SPY's +5.77%
- **+1.1% alpha** (the gap)
- Equity: $106,870 (started at $100k)
- 88 days running

It also ranks **#2 on rolling 30D** with 4.31% return and a 2.78 Sharpe. Rank jumped 149 spots in one day—that's either signal strength or noise. We'll watch.

## The Failure Rate

**157 of 158 algos are losing to SPY on force rank.** The bottom tier:

- **VIX Fear Rotation**: -6.79% YTD, ranked #158
- **Algo Biscotti (Unconditional Loyalty)**: -3.13% YTD, ranked #155 (normal variant)
- **VIX Term Structure**: -5.1% YTD, ranked #156

But here's the wrinkle: **VIX Term Structure ranks #1 on rolling 30D** with 4.68% return and a 3.73 Sharpe. It's up 4.68% in the last month while down 5.1% YTD. That's a 155-rank gap between force and rolling windows—a signal that either recently found edge or is curve-fitting the last 30 days. We can't tell yet.

## The Divergence Problem

Three algos show massive rank gaps:

1. **VIX Term Structure**: Force rank #156 → Rolling 30D rank #1 (gap: 155)
2. **Chaos Rotation Lab** (Baileymol variant): Force rank #157 → Rolling 30D rank #5 (gap: 152)
3. **Algo Biscotti**: Force rank #155 → Rolling 30D rank #4 (gap: 151)

These aren't edge. They're regime shifts. When the market environment changes, old signals die and new ones wake up. We're documenting both states because both are real.

## Sector Consensus

All five major sectors are **BEARISH** across our signal set:
- Technology (XLK): 29% bullish signals
- Consumer Cyclical (XLY): 23% bullish
- Basic Materials (XLB): 19% bullish

This is not a prediction. It's a count of what 158 signals are saying *right now*. Tomorrow it changes.

## What We're Not Claiming

No alpha here is statistically significant at 88 days. Baileymol's +1.1% could be luck. The rolling 30D leaders could be overfitting. We're publishing failures alongside wins because that's the only honest way to run a lab.

---

**Full leaderboard at stockarithm.com — all signals public, failures included.**

What's your read on the force/rolling divergence? Are we watching regime change or just noise?