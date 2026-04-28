# Lab Report: 2026-04-27 — Two Algos Beat SPY, 131 Did Not

## The Setup

We're running **133 signals** across **105 tickers**, all paper-traded from inception. Each algo gets ranked two ways:

1. **Force rank** — full-window cumulative alpha vs SPY
2. **Rolling 30D rank** — last 30 days only, Sharpe-adjusted

Why both? Force rank shows if you've found something durable. Rolling 30D catches regime shifts and recent edge. They often disagree. That disagreement is where the lab gets interesting.

## The Failure Rate (Lead With This)

**131 of 133 algos are underwater vs SPY on force rank.** That's a 98.5% failure rate over the full window.

On rolling 30D? **Zero algos beat SPY.** All 134 rolling-window entries are negative delta to the benchmark. SPY returned +13.17% in the last 30 days. The best rolling performer (Algo Biscotti, normal variant) returned +8.86% — still -4.3% behind.

This is the differentiator: we publish the graveyard.

## The Two Winners (Force Rank)

**Algo Baileymol (Chaos Monger)** — +1.38% alpha, +6.35% YTD
- 84 days running
- Equity: $106,345.64
- Rank jump: 132 → 1 (massive rerank this period)

**Antonacci Dual Momentum Sector Rotation (DMSR)** — +0.35% alpha, +5.32% YTD
- 84 days running
- Equity: $105,324.84
- Held rank #2 (stable)

Both beat SPY's +4.97% YTD. Both are thin margins. Both could evaporate in the next 30 days.

## The Divergence Problem

Three algos show the rank-gap issue clearly:

**Faber Momentum Rotation**: Force rank #3 (3.85% YTD), but rolling 30D rank #134 (down -1.14% last month). Full-window edge doesn't predict recent performance.

**Algo Biscotti (normal)**: Force rank #129 (-1.01% YTD), but rolling 30D rank #1 (+8.86% last month, Sharpe 4.23). Recent momentum is real, but the full window is a drag.

**Chaos Rotation Lab (Baileymol variant)**: Force rank #132 (-6.25% YTD), rolling 30D rank #3 (+5.38% last month). Same algo, two different stories depending on window.

This is why we show both. One number lies.

## Sector Consensus

Signals are split. Technology (XLK) is the only sector with mixed sentiment (41% bullish, 9 of 22 algos). Everything else is bearish:
- Consumer Cyclical: 32% bullish
- Utilities: 17% bullish
- Industrials: 15% bullish

No conviction anywhere.

## The Failure of the Day

**VIX Fear Rotation** — Force rank #133, -11.81% alpha, -6.84% YTD. Lowest performer on the board. It's been running 74 days and losing.

## What We're Not Claiming

We're not claiming these algos will keep working. Baileymol's 131-rank jump in one period is a red flag for overfitting or luck. DMSR's stability is good, but 0.35% alpha is noise-adjacent. The rolling 30D winners are all negative to SPY — they're just less negative.

We're sharing the experiment because the skeptics are right to be skeptical. Most of these fail. The ones that don't are worth studying.

---

**Full leaderboard at stockarithm.com — all signals public, failures included.**

What's your read on the force/rolling divergence? Are you tracking this differently?