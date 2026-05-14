# StockArithm Lab Report: 99 Days In, 1 Algo Beating SPY

We're running 234 live paper-trading signals across 105 tickers. After 99 days, exactly **one algorithm is beating SPY**. That's the story. Let's be precise about what that means and what it doesn't.

## The Numbers

**Quantified Simple Monthly Rotation** (force rank #1) is up 10.87% YTD while SPY sits at 8.95%—a 1.91% alpha spread. Over 99 days, that's real outperformance on paper. It's also a sample size that statisticians will (correctly) dismiss as noise. We're not claiming edge. We're publishing the methodology so you can audit it.

The other 233 algos are underwater relative to the benchmark. **Baileymol** (Chaos Monger) ranks 234th on force rank, down 6.22% YTD. **Biscotti** variants and the Electricity Consumption signal are all negative double digits. We publish those failures because they're data.

## Two Ranking Systems, One Honest Picture

We report both **force rank** (full-window cumulative return since seed) and **rolling 30-day momentum** because they tell different stories:

- **Force rank** rewards consistency over 99 days. Simple Monthly Rotation owns the top spot.
- **Rolling 30D** isolates recent signal strength. VIX Term Structure (rank 2, rolling 30D) returned 6.8% in the last month but sits at force rank 229 overall. That's a 227-rank gap—a real divergence worth noting.

The 30-day Sharpe ratios are high (Simple Monthly: 5.2), but again: 30 days is a month. Max drawdown on Simple Monthly was -1.5% in the rolling window. That's not stress-tested.

## What's Actually Beating SPY

One algo. Out of 235 rolling 30D signals, one is beating the benchmark. SPY returned 8.19% in the last 30 days. Simple Monthly Rotation returned 10.87%. Everything else is lagging.

The "crazy" category algos (alternative data: Uber Mobility, VIX structures, Retail Sales Momentum, Reddit sentiment, FRED macros, TSA traffic, job openings) show interesting recent momentum—VIX Fear Rotation is rank 3 on rolling 30D—but they're all negative on full-window YTD. That's the honest read: alternative data is noisy at 99-day horizons.

## The Obvious Critique (We'll Say It First)

N=99 days is not statistically significant. One algo beating SPY in a 234-algo pool is not evidence of alpha—it's expected variance. We're not claiming predictive power. We're publishing live paper trades, methodology, and data sources (FRED, TSA, Reddit, job openings, VIX term structure, Google Trends, port container volume, liquor store foot traffic) so the quant community can replicate, stress-test, and break these signals.

The sector consensus today is bearish across all five major sectors (Industrials 29% bullish, Tech 20%, Consumer Cyclical 13%). That's a data point, not a forecast.

## Why This Matters

The lab's differentiator isn't returns. It's transparency. We show losses as clearly as wins. Biscotti is down 2%. Electricity Consumption is down 2.6%. These stay live and ranked. That's the opposite of survivorship bias.

**Methodology and full leaderboard at stockarithm.com.**