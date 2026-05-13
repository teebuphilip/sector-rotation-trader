# StockArithm Lab Report: 2026-05-12 — 1 Winner, 222 Losers

## The Setup

We're running **223 signals** across **105 tickers**, measuring edge against SPY using two ranking systems:

1. **Force rank** — full-window cumulative alpha (how long each algo has been live)
2. **Rolling 30D rank** — recent performance only (what's working *right now*)

Both matter. Force rank shows durability. Rolling 30D catches regime shifts and recent failures. When they diverge, something interesting is happening.

## The Failure Rate (Lead With This)

**222 of 223 algos are underperforming SPY on force rank.**

That's a 99.6% failure rate. SPY returned **8.35% YTD**. Only one algo beat it:

- **Quantified Simple Monthly Rotation** (+9.83% YTD, +1.49% alpha)

Everyone else is negative alpha. The median algo is down ~2–3% relative to the benchmark. The worst performers (Biscotti variants, Electricity Consumption) are -10% to -11% alpha.

This is the lab working as designed: publish failures publicly, not just the one winner.

## The Winner: Simple Monthly Rotation

**Force rank #1** for 98 days running.

- Equity: $109,832 (from $100k start)
- YTD: +9.83%
- Alpha vs SPY: +1.49%
- 30D return: +9.83% (Sharpe 4.74)
- Max drawdown (30D): -1.51%

It's a monthly rebalance across sector ETFs. No alternative data. No complexity. It works. We don't know why yet — that's the next question.

## The Divergence Problem

Three algos show a **massive gap** between force rank and rolling 30D rank:

| Algo | Force Rank | 30D Rank | Gap | 30D Return | YTD |
|------|-----------|----------|-----|-----------|-----|
| VIX Term Structure | 218 | 2 | 216 | +6.25% | -2.06% |
| VIX Fear Rotation | 222 | 3 | 219 | +4.88% | -3.80% |
| Baileymol (Chaos Monger) | 223 | 11 | 212 | +1.98% | -6.12% |

These algos are *recently hot* but *historically underwater*. Are they catching a new regime? Or are they variance spikes that will revert? The 30D window is too short to know. Force rank says "don't trust it yet."

## Sector Consensus: All Bearish

Our 223 signals vote on 5 major sectors. Results:

- **Technology (XLK)**: 26% bullish (9 of 34 signals) — **BEARISH**
- **Industrials (XLI)**: 21% bullish (8 of 39) — **BEARISH**
- **Consumer Defensive (XLP)**: 19% bullish (6 of 32) — **BEARISH**
- **Utilities (XLU)**: 18% bullish (6 of 33) — **BEARISH**
- **Basic Materials (XLB)**: 18% bullish (6 of 33) — **BEARISH**

No sector has a bullish majority. The lab is net short everything.

## The Failure of the Day

**Baileymol (Chaos Monger)** — force rank 223 (dead last), YTD -6.12%, 30D rank 11 (recently bounced). This is the algo we're watching most closely. It's either recovering or it's noise.

---

**Questions for the thread:**

- Why is Simple Monthly Rotation the only winner? Is it luck, or is monthly rebalancing genuinely less noisy than daily/weekly signals?
- Are the VIX algos catching a real regime shift, or are we seeing a 30-day variance spike?
- What would make you trust a signal that's underwater on force rank but hot on rolling 30D?

Full leaderboard at stockarithm.com — all signals public, failures included.