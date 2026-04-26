# StockArithm Lab Report: April 25, 2026 — Sector Rotation Signals Remain Defensive

The StockArithm paper-trading lab is running 133 active signals across 105 tickers, testing whether economic leading indicators can systematically guide sector rotation. Today's results show a sharp divergence between short-term momentum and full-window performance—and a consensus that remains decidedly bearish.

## The Macro Setup

Sector rotation strategies rest on a simple thesis: leading economic indicators should predict which sectors will outperform. The lab tests this across multiple frameworks—Antonacci dual momentum, Faber momentum rotation, and others—each using different leading signals to time entry and exit across the 11 sectors.

Today, only 2 of 133 algos beat SPY's 4.79% return over the measurement window. That's a 1.5% success rate. The broader picture: 0 algos beat SPY over the rolling 30-day period. This matters because it suggests the current macro regime—whatever leading indicators are signaling—is not favoring sector rotation over broad market exposure.

## Winners and Losers

**Algo Baileymol (Chaos Monger)** leads the force-ranked leaderboard with a 2.28% alpha and 7.06% YTD return. Over the past 30 days, it returned 7.87%, outpacing SPY by 83 basis points. Its Sharpe ratio of 4.84 reflects low volatility relative to gains—a meaningful signal in a sideways market.

**Antonacci Dual Momentum Sector Rotation** ranks second, with 0.50% alpha and 5.29% YTD. It's held steady at rank 2 for the full window and ranks 4th over 30 days, suggesting consistent but modest outperformance.

**Faber Momentum Rotation** illustrates a critical divergence: it ranks 3rd on force (3.85% YTD) but 134th over the past month (down 0.88%). This suggests the signal that worked over 83 days has lost traction recently—a red flag for practitioners relying on momentum confirmation.

At the bottom, **VIX Fear Rotation** is the failure of the day, down 6.7% YTD and ranked 133rd. **Algo Biscotti (Unconditional Loyalty)** shows the inverse divergence: it's down 1.04% YTD (rank 129) but ranks 2nd over 30 days with 7.31% returns. This reversal suggests a recent regime shift favoring its signal logic.

## Sector Consensus: Broad Bearishness

The lab's precomputed sector consensus across all 133 signals shows overwhelming defensive positioning:

- **XLP (Consumer Defensive)**: 33% bullish — the highest conviction, yet still bearish
- **XLK (Technology)**: 32% bullish
- **XLI (Industrials)**: 25% bullish
- **XLY (Consumer Cyclical)**: 23% bullish
- **XLU (Utilities)**: 22% bullish

No sector reaches 50% bullish consensus. This is not a market where leading indicators are signaling broad-based rotation into growth or cyclicals. Instead, the signals are clustering around defensive names—and even there, conviction is muted. The highest bullish reading (XLP at 33%) still carries a composite "bearish" label.

## What This Means

The lab publishes failures alongside wins. Today's data shows that sector rotation frameworks—even those grounded in economic leading indicators—are struggling to outperform in the current regime. Two algos beat SPY; 131 did not. The rolling 30-day leaderboard shows zero outperformers, suggesting recent market structure has shifted against these signals.

The notable divergences (Faber weakening, Biscotti and VIX Term Structure strengthening) hint at a regime transition. Practitioners should watch whether the recent 30-day winners sustain their edge or revert to their full-window rankings.

**Full signal methodology and sector consensus at stockarithm.com.**