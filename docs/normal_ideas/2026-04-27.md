# Cross-Asset Momentum Reversion

**Idea ID:** `cross-asset-momentum-reversion`
**Source:** openai / gpt-4.1-mini
**Frequency:** monthly

## Thesis
This model exploits the tendency of strong cross-asset momentum to revert in the short term. By identifying assets with extreme 3-month momentum relative to their 12-month momentum, the strategy anticipates a mean reversion in the next month. This approach combines momentum and reversal effects across multiple asset classes to capture timely entry and exit points.

## Universe
- SPY
- TLT
- GLD
- USO
- EEM
- IEF
- VNQ
- DXY

## Data Sources
- yfinance
- FRED

## Signal Logic
Calculate 3-month and 12-month total returns for each asset monthly. Identify assets where 3-month momentum is in the top 20% but 12-month momentum is below the median, signaling short-term overextension. Conversely, identify assets where 3-month momentum is in the bottom 20% but 12-month momentum is above the median, signaling short-term oversold conditions.

## Entry / Exit
Enter long positions on assets with low 3-month but high 12-month momentum (bottom 20% 3-month, above median 12-month). Enter short positions on assets with high 3-month but low 12-month momentum (top 20% 3-month, below median 12-month). Exit positions after one month or if signals reverse.

## Position Sizing
Allocate equal weights to all long and short positions separately, ensuring net exposure is approximately zero. Limit individual position size to 10% of portfolio to control concentration risk.

## Risks
Prolonged trending markets can cause significant losses as reversions fail to materialize. Asset correlations may spike unexpectedly, reducing diversification benefits. Signal thresholds may generate false positives in volatile periods.

## Implementation Notes
Download monthly adjusted close prices using yfinance. Compute total returns over 3 and 12 months. Rank assets monthly and apply thresholds. Generate long/short signals and track positions with monthly rebalancing. Use FRED data for macro overlays if desired.

## Required Keys
- None
