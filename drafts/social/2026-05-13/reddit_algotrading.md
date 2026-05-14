# Lab Report: 234 Signals, 1 Beating SPY. Here's What Broke.

We're running 234 alternative-data signals across 105 tickers. Today's snapshot: **233 are underwater vs. SPY**. One is not. This is the post about the 233.

## The Setup

Each signal gets a force rank (full-window performance since inception) and a rolling 30D rank (last month only). We measure alpha as algo return minus SPY return. SPY is up 8.95% YTD. Most of our lab is not.

- **Total signals:** 234
- **Beating SPY (force rank):** 1
- **Beating SPY (rolling 30D):** 1
- **Days running:** 99 (most algos)
- **Data sources:** Uber mobility, VIX term structure, electricity consumption, port container volume, Google Trends, retail sales, liquor store foot traffic, and others

The one winner: **Quantified Simple Monthly Rotation** (+10.87% YTD, +1.91% alpha). It's a rotation strategy. It works. Everything else doesn't, at least not yet.

## Why Force Rank vs. Rolling 30D Matter

**Force rank** tells you if an idea has edge over 99 days. **Rolling 30D** tells you if it's waking up now.

Three algos show the divergence clearly:

- **VIX Term Structure:** Force rank 229 (dead), rolling 30D rank 2 (+6.80% last month, +4.90 Sharpe). It was broken. It's not anymore.
- **VIX Fear Rotation:** Force rank 233 (worse), rolling 30D rank 3 (+5.43% last month, +4.13 Sharpe). Same story.
- **Baileymol (Chaos Monger):** Force rank 234 (worst), rolling 30D rank 11 (+1.87% last month). Ranked dead last all-time. Ranked 11th this month. This is either mean reversion or noise. We'll find out.

The gap matters because it separates "this idea is broken" from "this idea is broken *right now*." The VIX signals suggest regime change. Baileymol suggests we got lucky.

## The Failures (Lead With These)

Bottom three by force rank:

1. **Algo Biscotti (Unconditional Loyalty)** — two variants, both negative. -1.79% and -2.09% YTD. -10.74% and -11.05% alpha. Running 98–99 days.
2. **Electricity Consumption** — -2.63% YTD, -11.58% alpha. 98 days.
3. **Port Container Volume** — -0.52% last month, -8.71% vs. SPY. Ranked 232 of 235 rolling 30D.

These aren't edge. These are noise with a data feed.

## The One That Works

**Quantified Simple Monthly Rotation:**
- YTD: +10.87%
- Last 30D: +10.87% (Sharpe 5.21)
- Max drawdown (30D): -1.51%
- Equity: $110,866.71 (from $100k start)

It's a sector rotation model. No alternative data. No machine learning. It rebalances monthly. It beats SPY by 1.91% alpha. That's the control. Everything else is measured against it.

## Sector Consensus (All Bearish)

Our 42 signals covering Industrials (XLI) are 29% bullish. That's the *highest* conviction in the lab. Everything else is lower:
- Technology (XLK): 20% bullish
- Consumer Cyclical (XLY): 13% bullish
- Basic Materials (XLB): 16% bullish

The lab is net bearish across all sectors. This is not a prediction. This is what the signals are saying.

---

**Full leaderboard at stockarithm.com — all signals public, failures included.**

What's your read on the VIX divergence? Are we seeing regime shift or overfitting to the last 30 days?