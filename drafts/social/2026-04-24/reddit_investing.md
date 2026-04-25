# StockArithm Lab Report: April 24, 2026 — When Recent Wins Hide Year-Long Losses

We're running 133 signals across 105 tickers. Two are beating SPY. Zero beat it over the last 30 days. Here's what the data shows.

## The Leaderboard Tells Two Stories

**Baileymol (Chaos Monger)** is the standout right now: +7.06% YTD, +2.28% alpha vs. SPY's +4.79%. Over the last 30 days it's up 7.87% with a Sharpe of 4.38. That's the signal of the day.

**Antonacci Dual Momentum Sector Rotation** sits #2 overall with +5.29% YTD and +0.5% alpha. Steadier—Sharpe of 5.86 over 30 days.

But here's the catch: **Faber Momentum Rotation** ranks #3 for the full window (+3.85% YTD) yet ranks dead last (134th) in the rolling 30-day window. It's down 0.52% in the last month. That's a 131-rank gap. Something shifted.

## The Failures Are Real

**VIX Fear Rotation** is the failure of the day: -6.7% YTD, -11.49% alpha. Lowest rank across all 133 signals.

**Biscotti (Unconditional Loyalty)** — both the normal and "crazy" variants — are underwater YTD (-1.04% and -2.51%) despite Biscotti normal ranking #2 in the last 30 days (+6.68%). It's been running 82 days and lost money overall.

**VIX Term Structure** is another divergence: ranked 131st full-window (-4.88% YTD) but #3 in the last 30 days (+5.08%). The recent bounce doesn't erase the damage.

## What the Signals Measure

These aren't black-box models. They're sector rotation triggers based on economic data:

- **Baileymol & Biscotti**: Momentum-based sector rotation
- **DMSR**: Dual momentum across sectors (Antonacci framework)
- **Faber**: Momentum rotation with trend filters
- **VIX variants**: Volatility structure and fear gauges
- **Retail Sales Momentum, Electricity Consumption**: Alternative data feeding sector calls

## Sector Consensus (Mixed)

The lab's 19 signals are most bullish on **Technology (XLK)** at 37% bullish. Everything else is bearish: Consumer Defensive 32%, Consumer Cyclical 22%, Utilities 21%, Industrials 18%.

## The Real Story

Two algos beat SPY. Zero beat it in 30 days. Baileymol is hot *right now*, but Biscotti and VIX Term Structure show that recent wins can mask longer-term underperformance. Faber's collapse in the last month is a red flag worth watching.

The lab publishes all of this—wins, losses, and the gaps between them—because that's how you actually learn what works.

Everything is public at stockarithm.com.