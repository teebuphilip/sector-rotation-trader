# StockArithm Lab Report: 2026-05-06 — Zero Algos Beating SPY Over 94 Days

We're publishing today's full leaderboard, and the headline is unambiguous: **0 of 179 force-ranked algorithms are beating SPY year-to-date.** SPY is up 7.71%; our best performer (Baileymol) is at +7.11%. This is the differentiator we promised—we show losses as clearly as wins.

## The Setup

StockArithm runs 179 live paper-trading signals across 105 tickers. We rank them two ways:

1. **Force rank (full-window since seed):** cumulative return from day 1. Baileymol leads at -0.59% alpha vs. SPY. Biscotti (normal variant) trails at -10.68% alpha.
2. **Rolling 30D momentum:** last 30 calendar days only. Here, Quantified Simple Monthly Rotation ranks #1 with +6.59% return (vs. SPY's +11.37% in the same window, still -4.78% delta).

We report both because they answer different questions. Force rank shows durability; rolling 30D shows recent regime fit. They often diverge sharply—see Chaos Rotation Lab: force rank 179, rolling 30D rank 4. That's a 175-position gap. It means the algo has recovered hard in the last month after a brutal 94-day run.

## The Honest Critique

**Sample size:** 94 days of live paper trading is not statistically significant. We cannot claim edge. The confidence interval is enormous. Baileymol's +7.11% could be noise, luck, or regime-specific. We're publishing it anyway because the methodology—not the returns—is the point.

**Spread:** 0% beating SPY across both ranking systems. This is a failure state. It means either:
- The signals are genuinely weak.
- The market regime (strong broad-based rally) favors buy-and-hold over tactical rotation.
- Our alternative-data sources (FRED, TSA, Reddit sentiment, job openings, earthquake activity, Google Trends) are not yet predictive at the portfolio level.

**The "crazy" algos:** We tag 35 signals as experimental. Industrial Sector Weekly Earthquake Activity Correlation Dip returned -0.19% in 30D with a Sharpe of -29.4. Google Gusts: -0.20% return, Sharpe -23.2. These are published failures. They exist to test whether unconventional signals (seismic data, fast-food job openings, Google search velocity) have alpha. So far: no.

## What's Working (Relatively)

In rolling 30D, Simple Monthly Rotation and VIX Term Structure both posted +6.5% returns. Both still underperformed SPY's +11.37% by ~4.8 percentage points. Sharpe ratios are high (4.4+), but that's a function of low volatility in a rising market—not edge.

Sector consensus is weak. Technology (XLK) is the only sector with bullish lean: 37% of our algos bullish, composite "MIXED." Utilities, Consumer Defensive, Consumer Cyclical, and Industrials are all bearish-leaning (14–20% bullish). This divergence from broad SPY strength suggests our signals are either lagging or orthogonal to the current rally.

## The Data

- **Signals generated:** 179
- **Tickers covered:** 105
- **Days running (median):** 94
- **Algos beating SPY (force rank):** 0
- **Algos beating SPY (rolling 30D):** 0

Methodology and full leaderboard at stockarithm.com.