# StockArithm Lab Report: 2026-04-30 — One Winner, 150 Losers, and Why That Matters

We're running 151 algorithmic signals across 105 tickers in live paper trading. Today's snapshot is instructive precisely because it's brutal: **one algo is beating SPY on force rank. Zero are beating it on rolling 30-day momentum.** This is the transparency that matters.

## The Numbers

**Force rank (full-window since seed, ~87 days):**
- Baileymol (Chaos Monger) is +6.26% YTD, +0.78% alpha vs. SPY's +5.48%. That's the only winner.
- 150 algos are underwater or trailing. VIX Fear Rotation sits at rank 151, down 12.9% YTD.
- The median algo is losing to the benchmark. This is not a marketing problem; it's a data problem.

**Rolling 30-day (last month only):**
- SPY returned +10.51% in the past 30 days.
- Top rolling performer: Biscotti (Unconditional Loyalty), +4.98% with a 2.28 Sharpe. Still -552 bps behind SPY.
- Bottom three: Google Gusts, Copper Momentum, and a Google Trends / fast-food job openings signal—all flat to slightly negative, all lagging SPY by 106+ bps.
- **Zero algos beat SPY on rolling 30D.** This is the critical fact.

## Why We Report Both Leaderboards

Force rank rewards consistency over 87 days. Rolling 30D captures regime shifts. They diverge sharply here:

- **Biscotti** ranks #148 all-time (YTD: -2.57%) but #1 in the last month (+4.98%). 
- **VIX Term Structure** ranks #149 all-time (YTD: -5.74%) but #3 rolling 30D (+3.89%, 3.08 Sharpe).

This gap signals either mean reversion, data-snooping, or genuine tactical adaptation. We don't know yet. Sample size is 30 days. That's not statistically significant.

## Data Sources & Methodology

Signals draw from:
- FRED macroeconomic feeds
- TSA mobility indices
- FINRA dark pool aggregates
- Uber mobility data
- Google Trends and job opening flows
- VIX term structure
- Sector rotation frameworks (Antonacci, Faber)

Each algo generates a daily signal. We track equity curves, drawdowns, and Sharpe ratios. No survivorship bias—failures stay on the board.

## The Sector Call

Consensus across 151 signals:
- **Technology (XLK):** 38% bullish, MIXED stance
- **Utilities, Consumer Defensive, Cyclical, Industrials:** all BEARISH (15–26% bullish)

This is a weak consensus. The lab is not confident.

## What This Means

One algo beating SPY over 87 days is not an edge. It's noise. The lab's value is not in the returns—it's in the **public failure rate**. We show you what doesn't work. We show you the data sources. We show you the rank divergences. You can audit it.

If you're building quant systems, this is the template: publish losses as loudly as wins. Let the community poke holes. Iterate on methodology, not marketing.

Methodology and full leaderboard at **stockarithm.com**.