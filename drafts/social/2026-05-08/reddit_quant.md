# StockArithm Lab Report: 2026-05-08 — One Algo Beating SPY Across 202 Signals

We're running 202 live paper-trading algorithms across 105 tickers. Today's snapshot: **1 algo is beating SPY on force rank. 1 is beating SPY on rolling 30D momentum.** That's the honest baseline.

## The Setup

StockArithm publishes two ranking systems because they answer different questions:

1. **Force rank** (full-window since seed, ~96 days): cumulative alpha. Tells you which signals have sustained edge over the entire live period.
2. **Rolling 30D momentum**: recent performance. Captures regime shifts and signal decay.

SPY returned 8.27% YTD and 9.11% over the last 30 days. That's the hurdle.

## What's Working

**Quantified Simple Monthly Rotation** (simple_monthly) leads both leaderboards:
- Force rank #1: +10.03% YTD, +1.77% alpha vs. SPY
- Rolling 30D rank #1: +10.03% return, +0.92% delta vs. SPY, Sharpe 5.15
- 96 days live. Equity: $110,033.

This is a monthly rebalance strategy. It's simple. It's beating the benchmark. Sample size is still small—96 trading days is not statistically significant—but the consistency across both ranking systems is notable.

## The Divergences Worth Watching

Three algos show sharp rank gaps between force and rolling 30D:

- **VIX Fear Rotation**: Force rank 199, rolling 30D rank 3. YTD -3.2%, but +4.6% last 30 days. Max drawdown 30D: -2.0%.
- **VIX Term Structure**: Force rank 197, rolling 30D rank 2. YTD -1.45%, but +7.6% last 30 days. Sharpe 5.26 (30D).
- **Algo Baileymol (Chaos Monger)**: Force rank 202 (dead last), rolling 30D rank 10. YTD -6.2%, but +1.75% last 30 days.

These are regime-dependent signals. They're failing on full-window alpha but capturing recent market structure. This is exactly the kind of failure mode you want to see published—it tells you *when* and *why* an approach breaks.

## The Losses

**Algo Biscotti (Unconditional Loyalty)** is the failure of the day:
- Force rank 200: -3.94% YTD, -12.21% alpha
- Rolling 30D rank 200: -0.94% return, -10.05% delta vs. SPY
- Equity: $96,056 (down from $100k seed)

**Liquor Store Leading Indicator** (rolling 30D rank 201): -1.19% return, Sharpe -5.70. The signal is inverted or the data source (likely FRED or proprietary foot-traffic data) has decoupled from equity returns.

## Sector Consensus

Across all 202 algos, Technology (XLK) shows the highest bullish conviction: 41% of signals are bullish, composite "MIXED." Everything else is bearish—Consumer Defensive, Utilities, Basic Materials, Industrials all below 20% bullish.

This is not a market-timing call. It's a snapshot of where the algos are positioned.

## The Caveats

- 96 days is not enough to claim statistical significance. Sharpe ratios and alpha estimates have wide confidence intervals.
- Alternative data sources (TSA mobility, FRED economic series, Reddit sentiment, job openings) have their own lag and measurement error.
- Force rank is dominated by early-period performance. Recency bias is real.
- 1 out of 202 beating SPY is a baseline. It could be luck.

We publish the failures because that's the only way to know if the methodology is sound.

**Methodology and full leaderboard at stockarithm.com.**