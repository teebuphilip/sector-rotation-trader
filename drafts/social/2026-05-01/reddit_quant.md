# StockArithm Lab Report: May 1, 2026 — One Winner, 157 Losers

We're running 158 live paper-trading algorithms across 105 tickers. Today's snapshot is brutal and instructive.

## The Spread

**Force rank (full-window since seed):** 1 algo beating SPY. That's Baileymol, up 6.87% YTD vs. SPY's 5.77%. Alpha: +1.1%. The other 157 are underwater relative to the benchmark.

**Rolling 30-day momentum:** 0 algos beating SPY. SPY returned 9.98% in the last month. The top 30D performer—VIX Term Structure—returned 4.68%, a -5.3% delta. Second place, Baileymol (normal variant), returned 4.31%, also lagging.

This is the differentiator: we publish the failures. VIX Fear Rotation is down 6.79% YTD and ranks 158th. Electricity Consumption returned -0.49% over 30 days. These aren't hidden in a footnote.

## Two Ranking Systems, Why Both Matter

**Force rank** accumulates returns since each algo's seed date (88 days for most, 78 for newer entries). It answers: "Which signal has the longest track record of outperformance?" Baileymol's 88-day equity curve sits at $106,870 on a $100k seed.

**Rolling 30D** isolates recent momentum and Sharpe ratio. It catches regime shifts. VIX Term Structure ranks 156th all-time but 1st in the last 30 days—a 155-rank gap. That's a notable divergence worth flagging. Biscotti (normal) and Chaos Rotation Lab show similar patterns: weak YTD, strong recent weeks.

The gap itself is data. It suggests either mean reversion ahead or a genuine regime change. We report both; you decide.

## Data Sources & Sample Size Caveat

Signals derive from FRED macroeconomic data, TSA passenger flows, Reddit sentiment aggregates, job openings (FRED JTSJOR), VIX term structure, sector rotation mechanics, and Google Trends. 88 days of live paper trading is **not statistically significant**. Confidence intervals are wide. Baileymol's 1.1% alpha could evaporate in the next 88 days. The lab is a transparency mechanism, not a prediction engine.

## Sector Consensus

All five major sectors show bearish consensus today. Technology (XLK) is the "least bearish" at 29% bullish signals (10 of 34 algos). Consumer Defensive (XLP) is 17% bullish. This is a crowded short, which historically precedes reversals—or confirms weakness. The data doesn't tell you which.

## What This Means

One algo is beating SPY on a full-window basis. None are beating it on a 30-day basis. The lab is currently a museum of underperformance with occasional pockets of recent strength. That's honest. It's also why we run it: to see whether alternative data (job openings, electricity, Reddit, TSA) can generate alpha, and to publish the answer in real time, win or lose.

Methodology and full leaderboard at stockarithm.com.