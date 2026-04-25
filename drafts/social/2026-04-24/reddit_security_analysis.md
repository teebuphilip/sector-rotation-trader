# StockArithm Lab Report: April 24, 2026 — Sector Rotation Signals Diverge as Momentum Fades

The StockArithm paper-trading lab is publishing mixed results across 133 active signals today, with a critical divergence emerging between full-window performance and recent 30-day momentum. Only 2 of 133 algos are beating SPY on a force-ranked basis, while the broader sector consensus has shifted decidedly bearish.

## The Macro Setup: Momentum Breakdown

SPY returned 8.7% over the past 30 days. Yet the lab's sector rotation signals—designed to capture leading economic shifts—are showing strain. The consensus across 19 sector-rotation algos now reads heavily defensive: Technology (XLK) is the sole mixed signal at 37% bullish conviction, while Consumer Cyclical (XLY), Utilities (XLU), and Industrials (XLI) all register bearish, with bullish percentages in the low 20s. This pattern suggests the algos are pricing in either economic deceleration or a rotation away from cyclical exposure.

## Winners and Losers: A Tale of Timing

**Algo Baileymol (Chaos Monger)** leads the force-ranked leaderboard with +2.28% alpha and a 30-day return of 7.87%—outpacing SPY by 83 basis points. Over 82 days of live trading, it has grown the paper portfolio to $107,064. The economic thesis underlying this signal remains opaque by design, but its recent outperformance suggests it has captured a tactical edge the broader market has not yet priced.

**Antonacci Dual Momentum Sector Rotation** ranks second with +0.50% alpha and a 5.29% YTD return. This signal explicitly tests whether sector momentum—a leading indicator of relative economic strength—can predict rotation timing. Its 30-day Sharpe of 5.86 indicates consistent risk-adjusted returns, though it trails Baileymol.

The failures are equally instructive. **VIX Fear Rotation** sits at rank 133 with -11.49% alpha and -6.7% YTD, suggesting that volatility-term-structure signals have lagged in this environment. **Algo Biscotti (Unconditional Loyalty)** shows a striking divergence: its normal variant ranks 129th on force (down 20 spots) with -1.04% YTD, yet its 30-day rolling rank is 2nd with +6.68% recent return. This suggests Biscotti's underlying thesis—whatever it tests—has recently aligned with market conditions but has underperformed over the full 82-day window.

## The Divergence Problem

Three algos exhibit notable rank gaps between full-window and rolling 30-day performance:

- **Faber Momentum Rotation**: Force rank 3, but rolling 30D rank 134. It has delivered 3.85% YTD but lost -0.52% in the past month, indicating its momentum thesis has broken down recently.
- **VIX Term Structure**: Force rank 131, but rolling 30D rank 3. Despite -4.88% YTD, it has captured +5.08% in the past 30 days—a sharp reversal.
- **Biscotti**: Force rank 129, rolling 30D rank 2. The gap of 127 positions reflects a recent inflection in its signal's predictive power.

These divergences matter because they reveal whether a signal's economic thesis is cyclical (recently broken) or structural (temporarily out of favor). The lab publishes both outcomes without filtering.

## Sector Consensus: Defensive Tilt

The call of the day flags Technology (XLK) as the highest-conviction bullish sector at 37%, but that still reads as mixed. Consumer Defensive (XLP) at 32% bullish is bearish. The absence of a single bullish sector consensus suggests the algos are hedging or rotating into cash equivalents—a macro posture consistent with economic uncertainty.

**Full signal methodology and sector consensus at stockarithm.com.**