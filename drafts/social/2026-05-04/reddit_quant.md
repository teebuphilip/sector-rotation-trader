# StockArithm Lab Report: 2026-05-04 — One Winner in 179 Algos

We're running 179 signals across 105 tickers in live paper trading. Today's snapshot: **1 algo beating SPY on force rank. Zero on rolling 30D.** This is the data. This is why we publish failures.

## The Setup

Two ranking systems run in parallel:

1. **Force rank**: cumulative return since seed (92 days for most algos). This is the full-window view. Survivorship bias is real here—we're not cherry-picking; we're showing the entire cohort.
2. **Rolling 30D momentum**: last 30 calendar days only. Captures recent regime fit without the anchor of early drawdowns.

SPY returned +5.39% over the full period and +8.97% in the last 30 days. That's the benchmark. Everything else is measured against it.

## What's Working (Barely)

**Algo Baileymol (Chaos Monger)** is the sole force-rank winner: +6.79% YTD vs. SPY's +5.39%, generating +1.41% alpha. Equity: $106,793. It also ranks #1 on rolling 30D with a 2.84 Sharpe ratio and +5.34% return over the last month, outpacing SPY by 363 bps.

The next two—Faber Momentum Rotation and Antonacci Dual Momentum Sector Rotation—are underwater relative to SPY by 116 and 165 bps respectively, despite ranking #2 and #3 on force rank.

**Rolling 30D tells a different story.** Three algos posted positive returns in the last month: Baileymol (normal), Baileymol (crazy variant), and VIX Term Structure. All three underperformed SPY on the full window but are catching the recent uptrend. This is regime-dependent edge, not persistent alpha.

## The Failures

**VIX Fear Rotation** is the failure of the day: -7.0% YTD, ranked 179th. **Algo Biscotti** variants sit at 175–176, down -3.1% to -3.4%. The bottom tier includes Truck Tonnage Index and Freight Rail Carloads—both alternative-data signals sourced from FRED and TSA—returning -0.89% and -1.01% respectively over 30 days.

This matters: we're testing signals built on real economic data (tonnage, carloads, electricity consumption). When they fail, we show it. No narrative smoothing.

## The Divergence Problem

Three algos rank strong on rolling 30D but weak on force rank—a 171–176 point gap. Biscotti (normal) is -3.42% YTD but +2.26% in the last 30 days. VIX Term Structure is -5.32% YTD but +3.79% in the last month. This is the regime-fit trap: recent performance ≠ edge.

## Statistical Honesty

92 days is not statistically significant. One algo beating SPY in a 179-algo cohort is not evidence of skill—it's consistent with random walk. The rolling 30D leaderboard is even noisier: we're measuring 30 data points per algo. Sharpe ratios above 2.8 on 30-day windows are suspect without out-of-sample validation.

Sector consensus is uniformly bearish (Technology 35% bullish, Energy 14%). The algos are not aligned with this view; they're generating long-biased signals across the board.

## Why This Matters

We're not claiming edge. We're publishing the methodology, the failures, and the sample-size limitations. The lab is a testbed for alternative-data signals and systematic rotation rules. Some work for 30 days. Most don't beat SPY over 92 days. That's the finding.

**Methodology and full leaderboard at stockarithm.com.**