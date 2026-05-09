# Lab Report: 202 Signals Running, 1 Beating SPY (Force Rank)

We're running 202 algorithmic signals across 105 tickers. One is beating SPY on a force-ranked basis. That's the starting point.

## The Pipeline

Each signal generates a daily trade recommendation. We measure two things:

1. **Force Rank** — cumulative return from day 1 (96 days running for most). This is the long-term scoreboard.
2. **Rolling 30D** — last 30 calendar days of returns, Sharpe ratio, max drawdown. This catches recent regime shifts.

Both matter. Force rank tells you if an idea has legs. Rolling 30D tells you if it's working *now*.

## The Failure Rate (Lead with This)

**201 of 202 signals are underperforming SPY on force rank.** SPY is up 8.27% YTD. Here's what's not:

- **Quantified Simple Monthly Rotation** (+10.03% YTD, +1.77% alpha) — the only one beating SPY force-ranked
- **Baileymol** (+7.54% YTD, -0.72% alpha) — ranked #202 overall, down 192 spots from last week
- **Faber Momentum Rotation** (+5.01% YTD, -3.25% alpha)
- **Antonacci Dual Momentum Sector Rotation** (+4.66% YTD, -3.61% alpha)

At the bottom: **Biscotti** (-3.94% YTD, -12.21% alpha), **VIX Fear Rotation** (-3.2% YTD, -11.46% alpha), **Electricity Consumption** (-2.02% YTD, -10.29% alpha).

## The Divergence Problem

Here's where it gets interesting. Three signals show massive rank gaps between force rank and rolling 30D:

| Algo | Force Rank | 30D Rank | Gap | 30D Return |
|------|-----------|----------|-----|-----------|
| VIX Fear Rotation | 199 | 3 | 196 | +4.60% |
| VIX Term Structure | 197 | 2 | 195 | +7.61% |
| Baileymol | 202 | 10 | 192 | +1.75% |

**VIX Fear Rotation** is ranked #3 in the last month (+4.60%, Sharpe 3.38) but #199 all-time (-3.2% YTD). That's not recovery—that's a regime flip. The signal was wrong for 66 days, right for 30.

**Simple Monthly Rotation** (the winner) is #1 on both metrics: +10.03% force rank, +10.03% rolling 30D, Sharpe 5.15. No divergence. Consistent.

## What We're Not Claiming

We're not saying any of these will beat SPY next month. We're not ranking them by Sharpe ratio alone (that's how you overfit to noise). We're publishing the failures because that's the only way to know if the lab is honest.

## The Sector Read

Consensus across 202 signals on sector rotation:
- **Technology (XLK)**: 41% bullish — the only mixed signal
- **Consumer Defensive, Utilities, Materials, Industrials**: all bearish (14–19% bullish)

That's not a strong conviction call. It's a weak consensus.

---

**Full leaderboard at stockarithm.com — all signals public, failures included.**

What's your read on the VIX signals' 30D pop? Regime change or mean reversion trap?