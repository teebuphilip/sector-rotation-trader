# Lab Report: 292 Signals, 3 Winners, 289 Losers (as of 2026-05-19)

We're running 292 alternative-data signals across 105 tickers. Today's snapshot: **1% beat SPY on force rank. 99% didn't.** That's the starting point.

## The Pipeline

Each signal gets two scorecards:

1. **Force Rank** — full-window performance since launch (up to 103 days running). Ranks all 292 algos by total return vs. SPY.
2. **Rolling 30D** — last 30 calendar days only. Captures recent regime shifts and momentum reversals.

Both matter. Force rank shows durability. Rolling 30D shows if you're catching the current market. They often disagree wildly — that's where the interesting failures live.

## Today's Leaderboard (Force Rank)

**Winners (beating SPY):**
- **Quantified Simple Monthly Rotation** — +8.6% YTD, +0.91% alpha. Rank #1. Equity: $108,603.
- **Algo Baileymol (Chaos Monger)** — +8.23% YTD, +0.54% alpha. Jumped from rank 278 to rank 2 in one period. Rank change: +276.
- **Faber Momentum Rotation** — +7.76% YTD, +0.07% alpha. Rank #3. Steady.

**Losers (289 algos):**
- **Antonacci Dual Momentum Sector Rotation** — +6.06% YTD, but -1.64% alpha. Still positive, still losing to SPY's +7.69%.
- **Copper Momentum** — -3.5% YTD, -11.19% alpha. Equity: $96,504.
- **VIX Fear Rotation** — -5.15% YTD, -12.84% alpha. Equity: $94,850.

SPY returned +7.69% in the same window.

## The Divergence Problem

Here's where it gets messy. **VIX Fear Rotation** ranks #290 on force rank (down -12.84% alpha) but #3 on rolling 30D (+2.8% in the last month, +0.007% vs SPY). Rank gap: 287 positions.

Same story with **VIX Term Structure** (force rank 287, rolling 30D rank 4) and **Algo Biscotti** (force rank 282, rolling 30D rank 8).

These aren't glitches. They're signals that got crushed early, then caught a recent wave. The question: is that mean reversion or regime change? We don't know yet. That's why we publish both.

## Sector Consensus (All Bearish)

Across 48 signals covering Utilities (XLU), only 25% are bullish. Tech (XLK): 20% bullish. Industrials (XLI): 19%. The lab is consensus-bearish across all major sectors.

## What We're Not Claiming

- No alpha is "statistically significant" at 103 days.
- Baileymol's +276 rank jump is noise, not a strategy.
- VIX signals beating SPY in 30D doesn't mean they'll keep doing it.
- We have no idea why Copper Momentum is down 11%.

## What We're Showing

289 public failures. Three public wins. The math is brutal. If you're building algos, this is what the distribution looks like.

**Full leaderboard at stockarithm.com — all signals public, failures included.**

What's your read on the Baileymol jump? Rebalance artifact or real edge?