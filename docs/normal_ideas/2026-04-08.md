# Seasonal Strength Rotation

**Idea ID:** `seasonal-strength-rotation`
**Source:** openai / gpt-4.1-mini
**Frequency:** monthly

## Thesis
This model exploits well-documented seasonal patterns in equity sectors by rotating monthly into the sector ETFs with the strongest historical performance during the current month. By leveraging seasonality, it aims to capture persistent calendar-driven return anomalies while reducing exposure to weak sectors. The approach combines momentum with seasonal timing to improve risk-adjusted returns.

## Universe
- XLF
- XLK
- XLE
- XLV
- XLY
- XLP
- XLB
- XLU
- XLRE

## Data Sources
- yfinance

## Signal Logic
At the beginning of each month, calculate the average monthly return for each sector ETF over the past 10 years for the current calendar month. Rank sectors by their average seasonal return for that month. Select the top 2 sectors with the highest historical average returns for that month.

## Entry / Exit
Enter long positions in the top 2 ranked sector ETFs at the first trading day of the month. Exit all positions at the end of the month before the next month's rebalancing.

## Position Sizing
Allocate equal weights (50% each) to the two selected sector ETFs. Use full capital allocation without leverage.

## Risks
Seasonal patterns may weaken or disappear during structural market changes or regime shifts. The model may underperform during months with high market volatility or when sector rotations are driven by non-seasonal macro events. Limited diversification by focusing on only two sectors increases idiosyncratic risk.

## Implementation Notes
Download monthly adjusted close prices for each sector ETF for at least 10 years. Calculate monthly returns and average returns for each calendar month by sector. At each month start, rank sectors by their historical seasonal average and select top 2. Implement monthly rebalancing to enter/exit positions accordingly.

## Required Keys
- None
