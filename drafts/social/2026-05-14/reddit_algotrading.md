# Lab Report: 251 Signals, 1 Winner. Here's What We're Learning.

**TL;DR:** 250 algos are underwater vs SPY. One isn't. We're publishing both the leaderboard and the graveyard because that's the only way to know what's real.

---

## The Setup

We're running **251 signals** across **105 tickers**, all paper-traded since inception. Each algo gets ranked two ways:

1. **Force rank** — full-window performance (100 days for most, 99 for newer entries)
2. **Rolling 30D rank** — last month only

Why both? Force rank shows durability. Rolling 30D catches regime shifts. When they diverge hard, something interesting is happening.

---

## The Failure Rate (Lead With This)

**250 of 251 algos are losing to SPY.**

SPY is up **9.81% YTD**. Here's the distribution:

- **Beating SPY:** 1 algo (0.4%)
- **Losing to SPY:** 250 algos (99.6%)

The median YTD return across the lab is somewhere around **6–7%**. Most signals are generating alpha in the *wrong direction*.

---

## The One Winner

**Quantified Simple Monthly Rotation** (`simple_monthly`):
- **YTD:** +12.53% (alpha: +2.71%)
- **30D return:** +12.53% (Sharpe: 5.87)
- **Max drawdown (30D):** -1.51%
- **Equity:** $112,527.99

It's a monthly rotation strategy. No alternative data. No complexity. It's been running 100 days. We don't know if it's signal or luck yet. That's the honest answer.

---

## The Interesting Divergences

Three algos are *crushing* the last 30 days but *drowning* on force rank. This matters:

| Algo | Force Rank | 30D Rank | 30D Return | YTD | Gap |
|------|-----------|----------|-----------|-----|-----|
| **VIX Fear Rotation** | 250 | 2 | +6.06% | -2.70% | 248 |
| **VIX Term Structure** | 246 | 3 | +5.96% | -0.95% | 243 |
| **Baileymol (Chaos Monger)** | 251 | 12 | +1.02% | -5.82% | 239 |

These are regime-dependent. They work in *this* market, not in the one we've been in. That's not a feature—it's a warning sign.

---

## What's Failing Hardest

Bottom 3 on force rank:

- **Biscotti (Unconditional Loyalty)** — both variants in the basement. YTD: -1.84% to -2.15%. Alpha: -11.66% to -11.96%.
- **Electricity Consumption** — YTD: -2.66%. Alpha: -12.47%.
- **Port Container Volume** — 30D return: -0.55%. Sharpe: -9.08.

These are alternative-data signals. They're not working. We're keeping them public anyway.

---

## Sector Consensus (Bonus Signal)

All 11 sectors are **BEARISH** according to our composite. Utilities and Tech are tied at 22% bullish. Industrials at 18%. Nothing is hot.

---

## What We're Not Claiming

- That the one winner will keep winning
- That alternative data is broken (sample size is 100 days)
- That you should trade any of this
- That we've found an edge

What we *are* doing: running the experiment in public, showing losses as clearly as wins, and letting the data sit where it lands.

**Questions, critiques, or "this is obviously survivorship bias" takes?** Drop them below.

**Full leaderboard at stockarithm.com — all signals public, failures included.**