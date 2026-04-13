# Sector Rotation with Momentum and Value Filter

**Idea ID:** `sector-rotation-momentum-value`
**Source:** openai / gpt-4.1-mini
**Frequency:** monthly

## Thesis
This model rotates investments among US equity sectors based on a combination of momentum and value signals. It selects sectors exhibiting strong 3-month price momentum but only invests if the sector's price-to-earnings (P/E) ratio is below the median, aiming to avoid overvalued sectors. This hybrid approach balances trend-following with valuation discipline to improve risk-adjusted returns.

## Universe
- XLY
- XLP
- XLE
- XLF
- XLV
- XLI
- XLB
- XLRE
- XLK
- XLU

## Data Sources
- yfinance (sector ETFs price data)
- yfinance (sector ETFs fundamental data including P/E)
- FRED (optional macroeconomic indicators for risk management)

## Signal Logic
Calculate 3-month total return momentum for each sector ETF. Calculate the current P/E ratio from fundamental data. Select sectors with momentum in the top quartile and P/E below the median of all sectors.

## Entry / Exit
Enter long positions in up to 3 sectors meeting the momentum and value criteria at the monthly rebalance date. Exit sectors if they fall below the momentum or value threshold at the next rebalance.

## Position Sizing
Allocate equal weight to each selected sector, dividing capital equally among up to 3 sectors. If fewer than 3 sectors qualify, allocate equally among those.

## Risks
Periods where momentum and value signals conflict may lead to missed opportunities. Overreliance on P/E ratio can be misleading during earnings recessions or structural sector changes. Sector ETFs may have tracking errors and liquidity constraints.

## Implementation Notes
Use yfinance to download monthly adjusted close prices and calculate 3-month returns for each sector ETF. Extract P/E ratios from yfinance fundamentals or estimate from earnings data. At each monthly rebalance, filter sectors by momentum and P/E criteria, then allocate equally. Track positions and update monthly.

## Required Keys
- None
