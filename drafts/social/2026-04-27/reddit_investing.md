# StockArithm Lab Report: When Recent Wins Hide Full-Window Losses

We're running 133 signals across 105 tickers, and today's results show something interesting: **the last 30 days look nothing like the last 84 days.**

## The Split Personality Problem

**Baileymol (Chaos Monger)** is ranked #1 overall—up 1.38% alpha, beating SPY by 1.38 percentage points. But zoom out to the full 84-day window and it's down 6.25% YTD. Meanwhile, **Biscotti (Unconditional Loyalty)** is ranked #129 on force (down 1.01% YTD), yet it's the #1 performer in the last 30 days with +8.86% returns and a 4.23 Sharpe ratio.

This is the lab publishing what actually happens: signals that look broken long-term can catch fire short-term, and vice versa.

## What's Working (Last 30 Days)

- **Biscotti (normal)**: +8.86% vs. SPY's +13.17% (still -4.3% delta, but best risk-adjusted)
- **Baileymol (normal)**: +7.17% with a 4.4 Sharpe
- **DMSR** (Antonacci Dual Momentum Sector Rotation): +4.39% with the highest Sharpe at 7.05

## What's Failing

- **VIX Fear Rotation**: -11.81% alpha, ranked dead last (#133)
- **VIX Term Structure**: -10.6% alpha, -5.63% YTD
- **Electricity Consumption** and **Copper Momentum**: both negative returns over 30 days

Only **2 of 133 signals** are beating SPY on the full window. Over 30 days, **zero algos beat SPY**—the market is up 13.17%, and our best performers are lagging.

## Sector Consensus

The lab's 22 signals on sector rotation show **Technology (XLK) as the only mixed signal** (41% bullish). Everything else is bearish: Consumer Cyclical at 32%, Utilities at 17%, Industrials at 15%.

## The Real Story

This is what transparent experimentation looks like. We're not hiding the Biscotti and Baileymol failures. We're showing that momentum-based sector rotation works in some windows and fails in others. The lab doesn't know which is predictive yet—that's the point.

Everything is public at stockarithm.com.