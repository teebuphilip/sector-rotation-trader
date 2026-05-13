# StockArithm Lab Report: 2026-05-12 — One Winner, 222 Losers

We're running 223 live paper-trading signals across 105 tickers. Today's snapshot: **1 algo is beating SPY. The other 222 are not.** This is the lab working as designed.

## The Numbers

**Force rank (full-window since seed, ~98 days):**
- Quantified Simple Monthly Rotation: +9.83% YTD, +1.49% alpha vs. SPY's +8.35%. Equity: $109,832.
- Baileymol (Chaos Monger): +7.72% YTD, -0.62% alpha. Jumped 213 ranks in one period—a volatility spike, not a signal.
- Bottom tier: Biscotti (normal variant) at -2.67% YTD, -11.01% alpha. Electricity Consumption at -2.39% YTD, -10.74% alpha.

**Rolling 30-day momentum (last month only):**
- Simple Monthly Rotation leads again: +9.83% in 30D, Sharpe 4.74, max drawdown -1.51%.
- VIX Term Structure ranks #2 despite force-rank position 218—a 216-rank gap. +6.25% in 30D, Sharpe 4.59.
- VIX Fear Rotation: #3 rolling, force rank 222. +4.88% in 30D, Sharpe 3.78.

SPY returned +7.59% over the same 30 days.

## Why We Report Both Rankings

Force rank captures consistency over the full backtest window. Rolling 30D captures recent momentum. They diverge sharply for volatility-based strategies (VIX Term Structure, VIX Fear Rotation) and chaos-driven algos (Baileymol). This divergence is *data*, not noise. It tells you which signals are regime-dependent and which are stable.

## The Honest Critique

**Sample size:** 98 days is not statistically significant. One algo beating SPY over three months could be luck. The lab knows this. We publish it anyway because the methodology—not the returns—is the point.

**Survivorship bias:** We're showing you live paper trades. Dead algos don't appear here. That's a limitation you should assume.

**Data sources:** Signals draw from FRED (macro), TSA (mobility), Reddit sentiment, job openings, port container volume, Google Trends, VIX term structure, and sector rotation mechanics. No proprietary black box. Reproducible.

**Spread:** 1 of 223 beating SPY force-rank. 1 of 224 rolling 30D. The distribution is heavily left-skewed. Most algos underperform. That's the baseline you're competing against.

## Today's Signals

**Signal of the day:** Simple Monthly Rotation (force rank #1, rolling 30D #1). Ranked highest on recent momentum.

**Failure of the day:** Baileymol (Chaos Rotation Lab). Force rank 223, YTD -6.12%, rolling 30D rank 11. The rank gap suggests recent recovery, but the full-window picture is clear: this signal is not working.

**Sector consensus:** All major sectors show bearish composite signals. Technology (XLK) is "least bearish" at 26% bullish algos (9 of 34). Utilities, Materials, and Consumer Defensive all at 18%.

## The Point

StockArithm publishes failures publicly. Biscotti is down 11%. Electricity Consumption is down 10.74%. These aren't hidden in a drawer. The lab's differentiator is transparency: you see the full leaderboard, the data sources, the rank divergences, and the algos that are losing money.

Methodology and full leaderboard at stockarithm.com.