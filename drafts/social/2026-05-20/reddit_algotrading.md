# Lab Report: 323 Signals, 1 Winner. Here's What We're Learning.

**TL;DR:** 99.7% of our force-ranked algos are underperforming SPY. One is not. The gap between force rank and rolling 30D performance is where the interesting failures live.

---

## The Setup

We're running 323 signals across 105 tickers. Each algo gets scored two ways:

1. **Force rank** — full-window cumulative return vs. SPY (108 days running for most)
2. **Rolling 30D rank** — last 30 days only, with Sharpe ratio and max drawdown

Why both? Force rank shows if you found actual edge. Rolling 30D shows if that edge is *still working*. They almost never agree.

---

## The Failure Rate (Lead With This)

**322 of 323 algos are losing to SPY on force rank.**

SPY is up 8.8% YTD. Here's the distribution:

- **Beating SPY (force rank):** 1 algo
- **Beating SPY (rolling 30D):** 2 algos
- **Underwater YTD:** 319 algos

The single winner is **Quantified Simple Monthly Rotation** (+11.05% YTD, +2.25% alpha). It's a monthly rebalance across sectors. No alternative data. No complexity. It's been running 108 days.

Everything else is either flat or red.

---

## The Interesting Divergence

Here's where it gets weird: **VIX Fear Rotation** is ranked #321 on force rank (down -3.44% YTD) but #2 on rolling 30D (+4.65% in the last month, +0.065 delta vs. SPY).

Same story for **VIX Term Structure** (#316 force, #3 rolling 30D) and **Algo Biscotti** (#314 force, #9 rolling 30D).

**What this means:** These algos were garbage for 78 days, then something clicked in the last 30. Either:
- They found real edge that just started working
- They're curve-fit to recent market conditions and will blow up
- We're seeing noise

We don't know yet. That's the point of publishing failures.

---

## The Data Sources

We're testing signals built on:
- Sector rotation (momentum, dual momentum)
- Alternative data (Uber mobility, port container volume, freight rail carloads, retail sales)
- Volatility structure (VIX term structure, VIX fear rotation)
- Commodity momentum (copper, lumber)

The commodity and freight signals are getting destroyed. Copper Momentum is -11.3% alpha. Port Container Volume is -11.63%. These aren't edge—they're noise.

---

## What We're Not Claiming

- That Simple Monthly Rotation will keep winning (108 days is not a track record)
- That the VIX signals have found anything real (one month of outperformance is luck until proven otherwise)
- That alternative data is worthless (it might be; we're testing it)

We're sharing the lab notebook. The failures are public because that's how you find signal in the noise.

---

**Full leaderboard at stockarithm.com — all signals public, failures included.**

What's your read on the force rank / rolling 30D split? Are we looking at regime change or overfitting?