# StockArithm Lab Report: 2026-04-25 — Two Algos Beat SPY, 131 Did Not

We're running 133 live paper-trading signals across 105 tickers. Today's snapshot: **2 algos are beating SPY on force rank (full-window since seed). Zero are beating SPY on the rolling 30-day window.** This is the state of the lab. We publish it because the failures matter as much as the wins.

## The Numbers

**Force Rank (Full Window, ~83 days live):**
- Baileymol (Chaos Monger): +7.06% YTD, +2.28% alpha vs. SPY (4.79%). Equity: $107,064.
- Antonacci Dual Momentum Sector Rotation (DMSR): +5.29% YTD, +0.50% alpha. Equity: $105,293.
- 131 others underperforming SPY.

**Rolling 30-Day Window (SPY returned 8.70% in the last month):**
- Baileymol leads at +7.87% (30D), Sharpe 4.84, max drawdown –1.8%.
- Biscotti (normal variant) ranks #2 at +7.31% (30D), Sharpe 3.05, max drawdown –2.5%.
- VIX Term Structure ranks #3 at +5.32% (30D), Sharpe 4.91, despite being ranked 131st on force rank.
- **All 134 rolling 30D algos underperformed SPY's 8.70% in the last month.**

This is not a bug report. This is the data.

## Why Two Ranking Systems?

Force rank captures consistency over the full sample (83 days is not statistically significant—we acknowledge this directly). Rolling 30D captures recent momentum and regime sensitivity. They diverge sharply:

- **Faber Momentum Rotation**: Force rank #3 (3.85% YTD), but rolling 30D rank #134 (–0.88% last month). The algo worked early; it's broken now.
- **VIX Term Structure**: Force rank #131 (–4.88% YTD), but rolling 30D rank #3 (+5.32% last month). Recent edge, no durability signal yet.
- **Biscotti (normal)**: Force rank #129 (–1.04% YTD), rolling 30D rank #2 (+7.31% last month). Sharp recent reversal.

These divergences are the lab's real output. They flag regime changes and overfitting.

## Data Sources & Methodology

Signals draw from FRED macroeconomic data, TSA passenger flows, Reddit sentiment, job openings, sector ETF technicals, VIX term structure, dark pool volume (FINRA), and alternative data (earthquake activity near logistics hubs, electricity consumption). Each algo is a hypothesis. Some are labeled "crazy"—they test exotic correlations. Most fail.

## The Honest Critique

- **Sample size**: 83 days is noise. Two algos beating SPY over this window could be luck.
- **Survivorship**: We don't hide dead algos; they stay on the board with their losses.
- **Sector consensus**: 18 signals on Consumer Defensive (XLP) are 33% bullish (6 of 18). All major sectors show bearish consensus. This is a crowded short.
- **Drawdown risk**: Baileymol's max 30D drawdown is –1.8%. DMSR's is –1.2%. These are small, but the sample is small.

The lab's differentiator is not performance. It's transparency. We show you the failures—VIX Fear Rotation at –6.7% YTD, Biscotti (crazy variant) at –2.51% YTD, earthquake-activity signals returning –0.22% in 30 days. This is what a real signal lab looks like: mostly wrong, occasionally interesting.

**Methodology and full leaderboard at stockarithm.com.**