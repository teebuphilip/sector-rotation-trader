# StockArithm Lab Report: 2026-04-27 — Two Algos Beat SPY, 131 Did Not

We're 84 days into live paper trading across 133 signals covering 105 tickers. SPY returned +4.97% YTD. Here's what the data shows, unfiltered.

## The Spread

**Force rank (full-window since seed):** 2 of 133 algos beat SPY. That's 1.5%. The median algo is underwater relative to the benchmark.

- **Baileymol** (Chaos Monger): +6.35% YTD, +1.38% alpha
- **DMSR** (Antonacci Dual Momentum Sector Rotation): +5.32% YTD, +0.35% alpha

The rest lag. Faber Momentum Rotation sits at rank 3 with +3.85% YTD (−1.12% alpha). VIX Fear Rotation anchors the leaderboard at −6.84% YTD.

**Rolling 30-day momentum:** Zero algos beat SPY in the last month. SPY returned +13.17% over 30 days. The top rolling performer, Biscotti (normal), returned +8.86% — still −4.3% delta to the benchmark. This is the critical divergence: recent market conditions have been hostile to the signal set.

## The Divergences Worth Naming

Three algos show rank gaps large enough to flag:

1. **Biscotti (normal):** Ranked #129 force rank (−1.01% YTD) but #1 rolling 30D (+8.86%, Sharpe 4.23). A recent momentum spike that hasn't yet moved the full-window needle.

2. **Baileymol (crazy variant):** Ranked #132 force rank (−6.25% YTD) but #3 rolling 30D (+5.38%, Sharpe 3.34). Suggests the variant has found traction in the last month after a rough start.

3. **Faber Momentum Rotation:** Ranked #3 force rank (+3.85% YTD) but #134 rolling 30D (−1.14% last 30 days). A full-window winner that has stalled hard. This is a drawdown signal worth watching.

## Methodology Notes (Preempting the Obvious)

- **Sample size:** 84 days is not statistically significant. Confidence intervals are wide. We're publishing this because the methodology is transparent, not because the results are conclusive.
- **Two ranking systems:** Force rank captures the entire backtest window (seed to now). Rolling 30D captures recent momentum. Both are reported because they answer different questions: "Does this signal work?" vs. "Is it working *now*?"
- **Data sources:** Algos ingest FRED macroeconomic data, TSA travel indices, Reddit sentiment, job openings, FINRA dark pool flows, commodity prices, VIX term structure, sector ETF flows, and technical indicators. No single source dominates; failures are distributed across signal types.
- **Sector consensus:** Technology shows the weakest bearish signal (41% bullish, MIXED). Utilities, Industrials, and Consumer Defensive are heavily bearish (15–26% bullish). This aligns with the broad market rally outpacing defensive rotation.

## What This Means

The lab is publishing losses as loudly as wins. Two algos have edge; 131 do not — at least not yet, and possibly not at all. The rolling 30D leaderboard shows recent momentum is real but insufficient to overcome SPY's strength. Faber's collapse in the last month is a live failure case worth dissecting.

This is not a track record. It's a methodology audit.

**Methodology and full leaderboard at stockarithm.com.**