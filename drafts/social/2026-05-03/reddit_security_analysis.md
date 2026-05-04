# StockArithm Lab Report: May 3, 2026 — Sector Rotation Signals Diverge as Recent Momentum Decouples from Year-to-Date Performance

The StockArithm paper-trading lab is publishing a stark divergence today: algorithms that have underperformed for months are suddenly leading the 30-day leaderboard, while the system's only SPY-beating signal remains isolated at the top of the force-ranked standings.

## The Macro Setup: Sector Consensus Tilts Defensive

Across 167 tracked signals covering 105 tickers, the sector consensus is decidedly cautious. Technology (XLK) is the sole mixed signal at 39% bullish conviction—barely above neutral. Utilities, Consumer Defensive, Industrials, and Consumer Cyclical all register bearish readings, with cyclicals showing the weakest conviction at just 14% bullish. This pattern suggests the lab's signals are pricing in either economic deceleration or a flight to quality that has already begun.

## The Paradox: Recent Winners, Persistent Losers

**Algo Baileymol (Chaos Monger)** stands alone: it is the only algorithm beating SPY year-to-date (+6.87% vs. +5.77%), ranking #1 in force and #1 in the rolling 30-day window with a 4.55% return over the past month. Its 3.03 Sharpe ratio and -5.43% delta to SPY suggest it has been rotating defensively or into uncorrelated assets while the broad market rallied.

But the 30-day leaderboard tells a different story. **VIX Term Structure** (force rank 165, down -5.1% YTD) ranks #2 over the past month with 4.28% returns. **Algo Biscotti (Unconditional Loyalty)** (force rank 164, down -3.13% YTD) ranks #5 with 3.09% returns. Both are down significantly for the year yet outperforming SPY in the last 30 days.

This divergence is the lab's core finding: recent market conditions have favored signals that were wrong for the first three months of 2026. Whether this represents mean reversion, a genuine shift in macro regime, or noise remains an open question—and that uncertainty is why the lab publishes both winners and failures.

## The Failure Case

**VIX Fear Rotation** ranks dead last (167th) with -12.56% alpha and -6.79% YTD returns. It has been consistently wrong in a market that has rewarded either momentum or defensive positioning, but not fear-based rotation. This is the kind of transparent loss the lab documents: a thesis that did not survive contact with realized market behavior.

## What the Signals Are Testing

The sector consensus and recent momentum divergence suggest the lab is testing whether leading economic indicators (embedded in these algorithms' construction) can anticipate sector rotation before it occurs. The bearish readings on defensive sectors and cyclicals, paired with Baileymol's outperformance, imply the signals may be pricing in slower growth ahead—a thesis that would validate if economic data rolls over in the coming weeks.

The recent strength in previously underwater algorithms could indicate either that thesis is wrong, or that the market is finally catching up to what the signals saw three months ago.

**Full signal methodology and sector consensus at stockarithm.com.**