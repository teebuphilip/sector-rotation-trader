# StockArithm Lab Report: May 6, 2026 — When Recent Wins Hide Longer Losses

We're running 179 signals across 105 tickers. SPY is up 11.4% over the last 30 days. None of our algos are beating it. That's the headline.

## What We're Measuring

Most of these signals use sector rotation logic — they watch economic data (unemployment, credit spreads, yield curves, mobility indices) and rotate between sectors based on momentum or mean reversion. A few are "crazy" signals that test alternative data: earthquake activity, Google Trends job openings, VIX term structure. All of them are live, all of them are public, and we show losses as clearly as wins.

## The Divergence Problem

Here's what's interesting: **some signals are crushing it in the last 30 days but failing over the full window.**

**Quantified Simple Monthly Rotation** (Algo simple_monthly) is ranked #1 on the 30-day leaderboard with +6.6% return and a Sharpe of 4.44. But it's still -1.12% vs. SPY year-to-date. It's up $6,591 from the starting $100k, but SPY is up $7,710.

**VIX Term Structure** is even wilder: ranked #2 over 30 days (+6.5%, Sharpe 4.46), but it's down -2.84% YTD. The signal measures volatility curve shape as a rotation trigger. It worked recently. It hasn't worked overall.

**Chaos Rotation Lab** (a Baileymol variant) is ranked #4 in the last month (+4.2%) but ranks dead last (#179) over the full 94-day window (-5.59% YTD). A 175-rank gap.

## The Failures

**Algo Biscotti** (both normal and crazy variants) is down ~10.7% vs. SPY's +7.7%. It's been running 93–94 days and hasn't found a signal that works.

Three "crazy" signals at the bottom are essentially noise: earthquake correlation dips, Google Trends fast-food job openings, and generic Google search volume. They're down 0.18–0.20% in 30 days. Not catastrophic, but not signal either.

## Sector Consensus

The lab's 35 signals are split on Technology (XLK): 37% bullish, 63% bearish or neutral. Everything else is bearish — Utilities, Consumer Defensive, Consumer Cyclical, and Industrials all show 14–20% bullish conviction.

## The Real Question

Recent performance ≠ edge. Biscotti looked fine until it didn't. Simple Monthly Rotation is hot now. Will it hold? We'll know in 30 days.

Everything is public at stockarithm.com.