# Lab Report: 266 Signals, 1 Winner. Here's What We're Seeing

**TL;DR:** One algo is beating SPY across both force rank and rolling 30D. The other 265 are not. We're publishing the full failure rate because that's the only honest way to run this.

---

## The Setup

We're running **266 signals** across **105 tickers**, generated from a mix of momentum, sector rotation, alternative data, and chaos experiments. Each signal gets two rankings:

1. **Force rank** — full-window performance (101 days for most, 100 for newer ones)
2. **Rolling 30D** — last 30 calendar days only

Both matter. Force rank shows durability. Rolling 30D shows what's working *right now*. When they diverge, something interesting is happening.

---

## The Failure Rate (Lead With This)

**265 of 266 algos are underperforming SPY.**

SPY returned **8.49% YTD** and **5.60% over the last 30 days**.

- **1 algo beating SPY on force rank:** Quantified Simple Monthly Rotation (+10.5% YTD, +2.0% alpha)
- **1 algo beating SPY on rolling 30D:** Same one (10.5% return in 30D vs SPY's 5.6%)

The rest are negative alpha. Some are *deeply* negative:
- Algo Biscotti (Unconditional Loyalty): -3.17% YTD, -11.66% alpha
- VIX Fear Rotation: -4.04% YTD, -12.53% alpha
- Lumber Momentum: -2.42% 30D return, -8.02% delta to SPY

We're not hiding these. They're on the leaderboard.

---

## Force Rank vs. Rolling 30D: The Divergence Story

Here's where it gets interesting. Three algos show massive rank gaps:

| Algo | Force Rank | 30D Rank | Gap | YTD | 30D Return |
|------|-----------|----------|-----|-----|-----------|
| VIX Fear Rotation | 264 | 2 | 262 | -4.04% | +5.17% |
| VIX Term Structure | 260 | 3 | 257 | -2.31% | +4.75% |
| Algo Biscotti | 262 | 9 | 253 | -2.87% | +2.30% |

These three are *recently* outperforming but have been underwater for months. The question: is this mean reversion, or did they find a signal that just started working?

**Simple Monthly Rotation** shows the opposite pattern — consistent across both rankings. No gap. That's the only one we can point to and say "this held."

---

## What We're Not Claiming

- No alpha is "statistically significant" at 101 days
- One winner out of 266 could be luck
- We have no idea if Simple Monthly will keep working
- The sector consensus is 12–30% bullish across all sectors (very bearish), but that doesn't predict individual signal performance

---

## The Data

**Full leaderboard at stockarithm.com** — all signals public, failures included.

What are you seeing in your own backtests? Are you running force rank + rolling windows, or just one? Curious if the divergences match what you're finding.