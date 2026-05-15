# StockArithm Lab Report: 2026-05-14 — One Algo Beating SPY Across 251 Signals

We're running 251 algorithmic signals across 105 tickers in live paper trading. Today's headline: exactly **one** is beating SPY on a force-ranked (full-window) basis. That's the reality we publish.

## The Numbers

**Quantified Simple Monthly Rotation** leads the leaderboard with +12.53% YTD versus SPY's +9.81%, generating +2.71% alpha over 100 days of live trading. It's also #1 on the rolling 30-day momentum rank with a 5.87 Sharpe ratio and +12.53% return in the last month alone—outpacing SPY by 4.79 percentage points.

The remaining 250 algos are underwater relative to the benchmark. **Baileymol (Chaos Monger)** sits at rank 251 (force-ranked) with -1.74% alpha and -5.82% YTD, though it's climbed to rank 12 on the 30-day leaderboard (+1.02% recent return). **Biscotti (Unconditional Loyalty)** and **Electricity Consumption** round out the bottom, both down ~12% alpha from SPY.

## Why We Report Both Ranking Systems

We publish two leaderboards because they answer different questions:

1. **Force rank** (full-window since seed): Which signals have actually worked over the entire live period? This is the honest test. Only 1 of 251 passes.

2. **Rolling 30-day momentum**: Which signals are working *right now*? This captures regime shifts. **VIX Fear Rotation** (rank 250 force, rank 2 rolling) and **VIX Term Structure** (rank 246 force, rank 3 rolling) show dramatic recent strength despite year-to-date underperformance—a 248 and 243-rank gap respectively. This divergence matters for practitioners, but it's also a red flag: small sample sizes can flip rankings violently.

## The Honest Critique

**Sample size is the elephant in the room.** 100 days of paper trading is not statistically significant. One algo beating 250 others could reflect luck, overfitting to recent market conditions, or genuine edge—we cannot distinguish yet. The rolling 30-day Sharpe ratios (5.87 for the leader) look exceptional, but 30 days is a single regime. Drawdowns are shallow (max -1.5% for the leader), which is either discipline or insufficient stress.

**Data sources:** The lab ingests FRED macroeconomic data, TSA mobility indices, Reddit sentiment, job openings, VIX term structure, port container volume, retail sales, and sector ETF signals. Each signal is a hypothesis about market microstructure or macro regime. Most are failing.

## Sector Consensus

Across all 251 algos, sector consensus is uniformly bearish. Utilities (XLU) shows the highest bullish percentage at 22% (8 of 37 signals), but that's still a 2:1 bearish lean. Technology, Industrials, and Consumer Defensive all cluster at 15–18% bullish. This is not a contrarian signal—it's consensus pessimism.

## The Point

StockArithm publishes failures alongside wins. One algo beating 250 is not a marketing story; it's a methodology. We're testing whether alternative data and systematic rotation can generate alpha, and the current answer is: almost never, with one exception we're still validating.

Methodology and full leaderboard at **stockarithm.com**.