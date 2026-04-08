# Relative Strength Momentum

**Idea ID:** `relative-strength-momentum`
**Source:** anthropic / claude-3-haiku-20240307
**Frequency:** monthly

## Thesis
Momentum strategies that rank assets based on recent price performance can capture market trends and outperform passive investing. This model combines relative strength and momentum signals to identify the strongest assets in the universe.

## Universe
- SPY
- QQQ
- IWM
- EFA
- EEM

## Data Sources
- yfinance
- FRED

## Signal Logic
{'relative_strength': 'Calculate the 6-month and 12-month price return for each asset. Rank assets based on the 6-month return.', 'momentum': 'Calculate the 1-month price return for each asset. Rank assets based on the 1-month return.'}

## Entry / Exit
{'entry': 'Buy the top 30% of assets ranked by the combined relative strength and momentum scores.', 'exit': 'Sell assets that fall out of the top 30% on the next rebalance.'}

## Position Sizing
Equal weight the top 30% of assets.

## Risks
Sector concentration, high turnover, and sensitivity to market downturns.

## Implementation Notes
1. Download price data for the universe using yfinance. 2. Calculate the 6-month, 12-month, and 1-month returns for each asset. 3. Rank assets by the combined relative strength and momentum scores. 4. Buy the top 30% and hold for one month.

## Required Keys
- None
