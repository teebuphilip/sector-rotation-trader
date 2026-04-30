# StockArithm Lab Report: When Recent Wins Hide Full-Window Losses

We're running 144 signals across 105 tickers, and today's results show something interesting: **the best performers over the last 30 days are some of the worst performers year-to-date.** That's the kind of divergence worth examining.

## The Winners (This Month)

**Algo Biscotti** is crushing it on the 30-day leaderboard—up 7.24% versus SPY's 12.6% gain. That's still -5.36% alpha, but the Sharpe ratio is 3.2, meaning it's doing it with lower volatility. Problem: year-to-date, Biscotti is down 2.49%.

**Baileymol** (Chaos Monger) ranks #1 overall with 1.28% alpha and 5.72% YTD. It's also #2 on the 30-day board at +6.54%. This one's actually working both timeframes.

**DMSR** (Antonacci Dual Momentum Sector Rotation) sits #2 overall with 1.13% alpha. It measures sector momentum and relative strength—economic data as rotation triggers. Up 5.57% YTD, +4.64% last 30 days.

## The Failures (Full Window)

**VIX Term Structure** is down 10.7% alpha, sitting at rank 142. **VIX Fear Rotation** is the worst performer at -12.36% alpha, down 7.92% YTD. These volatility-based signals aren't working.

**Biscotti (Crazy variant)** and **Faber Momentum Rotation** show the divergence problem clearly. Faber ranks #3 overall but #143 on the 30-day board—it's been dead money for a month despite solid YTD returns.

## What the Lab Publishes

Only **2 of 144** signals are beating SPY on the full-window force rank. Over the rolling 30 days? **Zero algos beat SPY**—they're all underperforming, though some with better risk-adjusted returns.

The sector consensus is uniformly bearish: Technology (32% bullish), Consumer Defensive (26%), Consumer Cyclical (24%). No sector shows conviction.

## The Real Question

When a signal works for 30 days but fails for 86 days, is it signal or noise? That's what the lab is designed to answer—by publishing both wins and losses publicly, without spin.

Everything is public at stockarithm.com.