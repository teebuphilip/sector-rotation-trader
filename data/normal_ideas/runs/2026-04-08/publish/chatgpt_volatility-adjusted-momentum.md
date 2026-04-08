# Volatility Adjusted Momentum

**Idea ID:** `volatility-adjusted-momentum`
**Source:** openai / gpt-4.1-mini
**Frequency:** monthly

## Thesis
This model combines traditional momentum with volatility scaling to improve risk-adjusted returns. By adjusting momentum signals based on recent volatility, the strategy aims to reduce exposure during turbulent periods and increase exposure when momentum is strong and volatility is low. This approach seeks to capture momentum premiums while controlling for drawdowns in volatile markets.

## Universe
- SPY
- EFA
- EEM
- TLT
- GLD
- IEF
- VNQ
- DBC
- QQQ
- IWM

## Data Sources
- yfinance

## Signal Logic
Calculate 12-month price momentum (price return over the past 252 trading days excluding the last month). Calculate the annualized 20-day rolling volatility of daily returns. Adjust momentum by dividing raw momentum by volatility. Select assets with adjusted momentum above the median of the universe.

## Entry / Exit
Entry: Buy top 30% of assets ranked by volatility-adjusted momentum at the start of each month. Exit: Sell assets that fall below the median adjusted momentum on monthly rebalancing.

## Position Sizing
Equal weight positions among selected assets. If no assets meet criteria, hold cash (0% exposure).

## Risks
Momentum crashes during sudden market reversals; volatility estimates may lag and cause delayed adjustments; periods of uniformly high volatility may reduce signal effectiveness; liquidity constraints in less liquid ETFs.

## Implementation Notes
1. Download daily price data for universe from yfinance. 2. Compute daily returns and rolling 20-day volatility. 3. Calculate 12-month momentum excluding the last month. 4. Compute adjusted momentum = momentum / volatility. 5. Rank assets monthly and select top 30%. 6. Rebalance monthly with equal weights. 7. Track portfolio returns and turnover.

## Required Keys
- None
