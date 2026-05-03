# Lab Report: 158 Signals, 1 Winner, 0 in the Last 30 Days

We're running 158 alternative-data signals across 105 tickers. Today's snapshot: **157 are underwater vs. SPY**. One algo is beating the benchmark on force rank. Zero are beating it on the rolling 30-day window.

This is the experiment. This is what we publish.

## The Setup

**Force rank** = full-window cumulative return since launch (88 days for most signals). **Rolling 30D** = last month only, with Sharpe and max drawdown. Both matter because they answer different questions: *Does this signal work at all?* vs. *Is it working right now?*

SPY returned **+5.77%** force rank and **+9.98%** rolling 30D. Our median signal is trailing both.

## The One Winner

**Algo Baileymol (Chaos Monger)** is the only force-rank outperformer:
- **+6.87% YTD** vs. SPY's +5.77% (alpha: +1.1%)
- Equity: $106,870 (started $100k)
- 88 days running
- Ranked #150 two days ago; jumped to #1 on force rank

On rolling 30D, Baileymol sits at #2 with **+4.31%** (vs. SPY's +9.98%), so the recent window is lagging. That's the divergence we're tracking.

## The Divergence Problem

Three algos show the same pattern: crushing the last 30 days, drowning on full-window:

| Algo | Force Rank | 30D Rank | 30D Return | YTD Return | Rank Gap |
|------|-----------|----------|-----------|-----------|----------|
| VIX Term Structure | 156 | 1 | +4.68% | -5.1% | 155 |
| Baileymol (Chaos) | 157 | 5 | +2.37% | -5.98% | 152 |
| Biscotti | 155 | 4 | +2.67% | -3.13% | 151 |

These three are recent recoveries. They got hammered early, then found a signal that works *now*. That's not a win yet—it's a hypothesis. We're watching.

## The Failures

**VIX Fear Rotation** is the failure of the day: **-6.79% YTD**, ranked dead last (#158). **Electricity Consumption** and **Google Gusts** are also underwater, returning negative on the 30D window while SPY rallied 10%.

We publish these. They're part of the lab.

## Sector Consensus

All five major sectors are bearish according to our signal composite:
- **Technology (XLK)**: 29% bullish (10 of 34 signals)
- **Consumer Cyclical (XLY)**: 23% bullish
- **Basic Materials (XLB)**: 19% bullish

This is not a prediction. It's a count of what the algos are saying. The market is up; the signals are hedged or short.

## What We're Asking

- Why is Baileymol suddenly working? Is it regime-dependent?
- Are the 30D leaders (VIX Term Structure, DMSR) mean-reverting back to their YTD losses, or have they found real edge?
- Why is sector consensus so bearish while SPY rallies?

**Full leaderboard at stockarithm.com — all signals public, failures included.**

What's your read on the divergence? Are you seeing similar regime shifts in your own backtests?