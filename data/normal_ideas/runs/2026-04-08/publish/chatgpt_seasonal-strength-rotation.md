# Seasonal Strength Rotation

**Idea ID:** `seasonal-strength-rotation`
**Source:** openai / gpt-4.1-mini
**Frequency:** monthly

## Thesis
Certain asset classes exhibit persistent seasonal patterns in returns due to economic cycles, tax policies, and investor behavior. By identifying the strongest performing assets over specific calendar months and rotating into them monthly, the strategy aims to capture predictable seasonal trends while avoiding weaker assets. This approach leverages well-documented seasonality effects in equity sectors and commodities to enhance returns.

## Universe
- SPY
- GLD
- USO
- TLT
- EEM
- VNQ
- XLF
- XLY
- XLP

## Data Sources
- yfinance

## Signal Logic
Calculate average monthly returns for each asset over the past 10 years. For the current month, select the top 3 assets with the highest historical average returns for that month. Rebalance monthly into these assets.

## Entry / Exit
At the start of each month, sell all current holdings and buy equal-weighted positions in the top 3 seasonal performers identified for that month.

## Position Sizing
Equal weight allocation across the selected top 3 assets each month, fully invested with no leverage.

## Risks
Seasonality patterns may break down during structural market changes or black swan events. The model may underperform in trending markets where seasonal effects are overshadowed. Monthly rebalancing incurs transaction costs that can erode returns.

## Implementation Notes
Download 10+ years of daily price data for all universe assets. Aggregate daily returns into monthly returns. Compute average returns per calendar month for each asset. At each month start, rank assets by historical average return for that month and select top 3. Execute trades to equal weight selected assets.

## Required Keys
- None
