# Lab Report: 194 Signals, 0 Beating SPY — What We're Learning

**TL;DR:** Today's snapshot shows a complete washout on force rank. Every single algo is underwater vs. SPY YTD. But the rolling 30-day leaderboard tells a different story — and that divergence is the real signal worth examining.

---

## The Setup

We're running **194 signals** across **105 tickers**, pulling from alternative data sources (VIX term structure, commodity momentum, sector rotation mechanics, housing proxies). Each algo gets scored two ways:

1. **Force rank** — full-window cumulative return vs. SPY (95 days running)
2. **Rolling 30D** — recent performance + Sharpe ratio + max drawdown

Both matter. Force rank shows if you've found actual edge. Rolling 30D shows if that edge is *current*.

---

## The Failure Rate (Lead With It)

**0 of 194 algos beating SPY on force rank.**

SPY is up **7.38% YTD**. Our top performer, Baileymol (Chaos Monger), is at **6.41% YTD** — a **-0.97% alpha**. Second place, Simple Monthly Rotation, sits at **6.38%**. By rank 5 (Uber Mobility Index), we're at **2.99%**. By rank 190 (VIX Term Structure), we're at **-2.91%**.

The bottom three are all negative: Biscotti variants and VIX Term Structure ranging from **-3.12% to -10.8%**.

This is the lab working as designed. We publish failures publicly because that's how you find signal vs. noise.

---

## The Divergence That Matters

Here's where it gets interesting. **VIX Term Structure ranks #190 on force rank but #1 on rolling 30D.**

- **Force rank:** -2.91% YTD, rank 190 of 194
- **Rolling 30D:** +7.22% return, +5.12 Sharpe, only -1.7% max drawdown
- **vs. SPY 30D:** SPY returned 10.98%; this algo returned 7.22% (delta: -3.76%)

Same story for VIX Fear Rotation (rank 193 force, rank 4 rolling 30D) and Chaos Rotation Lab (rank 194 force, rank 5 rolling 30D). All three show **189-point rank gaps** between full-window and recent performance.

**Why this matters:** These algos are either (a) recently correcting a long drawdown, (b) capturing a regime shift the full window doesn't reflect, or (c) overfitting to the last 30 days. We can't tell yet. That's the experiment.

---

## Sector Consensus (Weak Signal)

All five major sectors are **BEARISH** today:
- Technology (XLK): 35% bullish signals (12 of 34)
- Consumer Defensive (XLP): 23% bullish (7 of 31)
- Consumer Cyclical (XLY): 18% bullish (8 of 45)
- Utilities (XLU): 14% bullish (5 of 35)
- Industrials (XLI): 14% bullish (5 of 35)

This is consensus weakness, not edge. Worth logging.

---

## What We're Not Claiming

We're not claiming any of these will beat SPY tomorrow. We're not predicting sector rotation. We're showing you the lab notebook: 194 bets, zero winners on the scoreboard that matters (full-window alpha), and a handful of recent outperformers that might be signal or might be noise.

The value is in the transparency. You see the failures. You see the methodology. You can replicate, critique, or steal the ideas.

---

**Full leaderboard at stockarithm.com — all signals public, failures included.**

What's your read on the force-rank vs. rolling-30D split? Are we looking at regime change or overfitting?