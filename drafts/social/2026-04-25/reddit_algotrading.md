# Lab Report: 2 Algos Beat SPY Out of 133 (April 25, 2026)

**The failure rate is the story.** Out of 133 force-ranked signals running today, only **2 are beating SPY**. On the rolling 30-day window? **Zero.** SPY returned +8.70% over the last month. Our median algo did not.

This is why we publish everything.

---

## Pipeline & Methodology

We're running **133 signals** across **105 tickers**, sourced from alternative data (dark pool flow, sector rotation, macro momentum, volatility structure, and some genuinely weird stuff like earthquake activity near logistics hubs). Each algo gets two rankings:

1. **Force rank** — full-window performance since launch (83 days median)
2. **Rolling 30D rank** — last 30 calendar days only

Both matter. Force rank shows if an idea has legs. Rolling 30D shows if it's *currently* working. When they diverge, something interesting happened.

---

## The Winners (and Why They're Rare)

**Baileymol (Chaos Monger)** is the only algo beating SPY on both metrics:
- Force rank: **#1** (+7.06% YTD, +2.28% alpha vs SPY)
- Rolling 30D: **#1** (+7.87% in 30 days, Sharpe 4.84)
- Equity: $107,064.56

**DMSR (Antonacci Dual Momentum Sector Rotation)** is the second:
- Force rank: **#2** (+5.29% YTD, +0.50% alpha)
- Rolling 30D: **#4** (+4.20% in 30 days, Sharpe 6.12)
- Equity: $105,293.53

That's it. Two out of 133.

---

## The Divergences (Where It Gets Weird)

**Faber Momentum Rotation** ranks #3 on force (3.85% YTD) but **#134 on rolling 30D** (-0.88% last month). It's broken recently. The algo worked for 83 days, then stopped.

**Biscotti (Unconditional Loyalty)** — the normal variant — ranks #129 on force (-1.04% YTD) but **#2 on rolling 30D** (+7.31% last month, Sharpe 3.05). It was dead for months. Now it's alive. This is the opposite problem.

**VIX Term Structure** is the wildest: #131 on force (-4.88% YTD) but **#3 on rolling 30D** (+5.32% last month, Sharpe 4.91). A "crazy" algo that was underwater for 73 days just caught fire.

These gaps matter. They tell you whether you're looking at a regime change or a dead signal that got lucky.

---

## The Failures

**VIX Fear Rotation** is the worst performer: -6.7% YTD, ranked #133. **Earthquake Activity Near Logistics Hubs** returned -0.22% in 30 days with a Sharpe of -18.24. We're running it anyway. If we only published winners, you'd have no idea what doesn't work.

---

## Sector Consensus

All five major sectors are **BEARISH** today:
- Consumer Defensive (XLP): 33% bullish (6 of 18 signals)
- Technology (XLK): 32% bullish (6 of 19)
- Industrials (XLI): 25% bullish (5 of 20)

This is not a bullish lab right now.

---

## What We're Not Saying

We're not claiming these algos will beat SPY tomorrow. We're not selling access. We're not hiding the 131 algos that are underwater. We're showing you the work: what we ran, how it performed, where it broke, and where it's working *right now*.

**Full leaderboard at stockarithm.com — all signals public, failures included.**

What's your read on the divergences? Are Biscotti and VIX Term Structure regime-adaptive, or did they just get lucky in the last 30 days?