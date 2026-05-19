# Lab Report: 278 Signals Running, 277 Losing to SPY

**TL;DR:** One algo is beating the market. The other 277 are not. Here's what we're seeing in the data.

---

## The Setup

We're running 278 signals across 105 tickers, all live-traded on paper since inception. Each signal generates a daily decision. We rank them two ways:

1. **Force rank** — full-window cumulative alpha vs SPY (102 days for most algos)
2. **Rolling 30D rank** — last 30 calendar days only

Both matter. Force rank shows if you've found something real. Rolling 30D shows if it's *still working*.

---

## The Failure Rate (Lead with This)

**277 of 278 algos are underperforming SPY.** That's 99.6% failure rate.

SPY returned **8.42% YTD**. Here's what we're seeing:

- **Quantified Simple Monthly Rotation** (simple_monthly): +9.31% YTD, +0.89% alpha. **Only winner.**
- **Algo Baileymol** (Chaos Monger): +8.04% YTD, -0.37% alpha. Ranked 266th last week, now 2nd on alpha. Noise.
- **Faber Momentum Rotation**: +7.59% YTD, -0.82% alpha.
- **Antonacci Dual Momentum Sector Rotation**: +6.23% YTD, -2.19% alpha.

Bottom of the barrel:
- **Algo Biscotti** (Unconditional Loyalty): -2.75% YTD, -11.17% alpha. Down 11 ranks in one day.
- **VIX Term Structure**: -2.81% YTD, -11.23% alpha.
- **VIX Fear Rotation**: -4.53% YTD, -12.95% alpha.

---

## The Divergence Problem

Here's where it gets interesting. Some algos are *terrible* on force rank but *decent* on rolling 30D:

| Algo | Force Rank | 30D Rank | 30D Return | Gap |
|------|-----------|----------|-----------|-----|
| VIX Fear Rotation | 276 | 3 | +3.47% | 273 positions |
| VIX Term Structure | 275 | 4 | +3.32% | 271 positions |
| Biscotti | 274 | 11 | +0.99% | 263 positions |

These three are *recently* working but have been underwater for months. Are they mean-reverting? Overfitting to the last 30 days? We don't know yet. That's the point of publishing both.

---

## What's Actually Winning

**Simple Monthly Rotation** is the only signal beating SPY across both timeframes:
- Force rank: #1 (9.31% vs 8.42%)
- Rolling 30D rank: #1 (9.31% return, 4.35 Sharpe, -2.86% max drawdown)
- 102 days live
- Equity: $109,305.74

It's also the signal of the day. No caveats needed.

---

## Sector Consensus (All Bearish)

Our 44 signals covering sector ETFs are voting bearish across the board:
- **Technology (XLK)**: 25% bullish (11 of 44 signals)
- **Utilities (XLU)**: 20% bullish
- **Basic Materials (XLB)**: 17% bullish
- **Energy (XLE)**: 15% bullish
- **Consumer Defensive (XLP)**: 14% bullish

This is consensus, not edge. Worth noting, not actionable.

---

## What We're Not Claiming

We're not saying Simple Monthly Rotation will keep winning. We're not saying the VIX algos are about to explode. We're showing you the data and the methodology so you can decide if either is worth your time.

The lab publishes failures publicly because that's the only way to know if you're fooling yourself.

**Full leaderboard at stockarithm.com — all signals public, failures included