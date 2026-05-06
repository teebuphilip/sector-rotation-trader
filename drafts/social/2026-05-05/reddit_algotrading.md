# Lab Report: 179 Signals, 1 Winner, 0 in Rolling 30D — What's Breaking

**TL;DR:** We're running 179 algos across 105 tickers. Today, **178 are underwater vs. SPY**. One signal (Baileymol) beat the market on force rank. Zero beat it in the last 30 days. This is the lab working as designed — publishing the failures loudly.

---

## The Pipeline

**Signal count:** 179 algos  
**Data sources:** Alternative data (mobility indices, liquor store traffic, copper momentum, VIX term structure, sector rotation models)  
**Measurement:** Force rank (full window) + rolling 30D Sharpe/return split  
**Benchmark:** SPY, +6.23% YTD through today  
**Coverage:** 105 tickers across standard and "crazy" algo types

We measure edge two ways because they tell different stories. Force rank shows long-term consistency. Rolling 30D catches regime shifts and recent momentum. When they diverge wildly, something interesting is happening.

---

## The Failure Rate (Lead With This)

**Force rank:** 1 of 179 beating SPY  
**Rolling 30D:** 0 of 180 beating SPY in the last month

SPY returned **+9.84%** in the past 30 days. Our top rolling performer (Baileymol, normal variant) returned **+6.15%** — a **-3.69% delta**. Second place (VIX Term Structure) hit **+4.82%**, down **-5.02%** vs. the benchmark.

This is not a bug. This is the market environment. When SPY runs hard, mean-reversion and sector rotation strategies get hammered. Our "crazy" algos (alternative data plays) are bleeding worse than the systematic ones.

---

## The One Winner & The Divergences

**Baileymol (Chaos Monger)** is the only force-rank winner:
- **Alpha:** +1.38% (vs. SPY's +6.23%)
- **YTD:** +7.62%
- **Equity:** $107,615.88 (started at $100k)
- **Days running:** 93

But here's the catch: it's **not** winning in the last 30 days. It's winning on the full window because it had a strong run earlier. That's why we publish both metrics.

**Notable divergence:** VIX Term Structure ranks **#177 on force rank** but **#2 on rolling 30D**. It's been dead money for 93 days (YTD: -4.38%), but it's suddenly working. Rank gap: 175 positions. This matters for traders deciding whether to trust recent performance or historical edge.

---

## What's Failing Loudest

**VIX Fear Rotation** (force rank #179):
- **Alpha:** -12.31%
- **YTD:** -6.07%
- **Rolling 30D rank:** #7 (yes, it's actually positive in the last month at +1.86%)

**Biscotti variants** (both normal and crazy types):
- **Normal:** -9.27% alpha, -3.03% YTD
- **Crazy:** -8.96% alpha, -2.73% YTD

These aren't edge. These are noise. We're keeping them live because the lab's job is to show what doesn't work, not hide it.

---

## Sector Consensus (Weak Signal)

Across 34 signals covering Technology (XLK), only **41% are bullish** — a MIXED stance. Everything else is bearish: Consumer Defensive (22%), Utilities (18%), Consumer Cyclical (16%), Industrials (14%). This is a defensive market, and our algos are struggling to adapt.

---

## What We're Asking

- Why is the rolling 30D leaderboard completely inverted from force rank? Is this a regime shift or just noise?
- Are the "crazy" algos (alternative data) fundamentally broken, or are they just out of phase?
- Should we weight Sharpe differently when max drawdown is near-zero but returns are flat?

**Full leaderboard at stockarithm.com — all signals public, failures included.**