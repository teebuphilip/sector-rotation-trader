# Leveraged ETF Momentum

**Idea ID:** `leveraged-etf-momentum`
**Source:** anthropic / claude-3-haiku-20240307
**Frequency:** monthly

## Thesis
Leveraged ETF momentum strategies can generate higher returns than regular ETF momentum strategies by capturing the magnified price movements of leveraged ETFs.

## Universe
- SPXL
- SPXS
- TQQQ
- SQQQ
- UPRO
- SPXU
- UDOW
- SDOW

## Data Sources
- yfinance
- FRED

## Signal Logic
Calculate the 12-month total return for a universe of leveraged ETFs. Go long the top performing ETF and short the bottom performing ETF.

## Entry / Exit
Enter long/short positions at the end of each month. Hold positions for one month.

## Position Sizing
Equal weight long and short positions.

## Risks
Leveraged ETFs can experience significant volatility and decay over time. Shorting can also introduce additional risks.

## Implementation Notes
1. Fetch monthly prices for the leveraged ETF universe from yfinance. 2. Calculate the 12-month total return for each ETF. 3. Go long the top performing ETF and short the bottom performing ETF. 4. Rebalance positions at the end of each month.

## Required Keys
- None
