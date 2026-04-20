# Moving Average Crossover Extended

**Idea ID:** `moving-average-crossover-extended`
**Source:** anthropic / claude-3-haiku-20240307
**Frequency:** daily

## Thesis
The moving average crossover strategy is a well-established trend-following approach that can be extended to improve performance and diversification by incorporating additional signals and asset classes.

## Universe
- SPY
- QQQ
- TLT
- GLD
- DBC

## Data Sources
- Yahoo Finance
- FRED

## Signal Logic
Generate buy and sell signals based on the crossover of short-term (e.g., 50-day) and long-term (e.g., 200-day) simple moving averages. Include additional signals from macroeconomic indicators (e.g., yield curve, VIX) and momentum factors.

## Entry / Exit
Enter a long position when the short-term moving average crosses above the long-term moving average. Exit the position when the short-term moving average crosses below the long-term moving average.

## Position Sizing
Allocate equal weights to each position, with the total portfolio exposure capped at 100%.

## Risks
Potential whipsaws during range-bound markets, drawdowns during sharp market reversals, and the need to carefully select the moving average windows and additional signals to avoid overfitting.

## Implementation Notes
1. Fetch daily price data for the selected assets using yfinance. 2. Calculate the short-term and long-term moving averages for each asset. 3. Generate buy and sell signals based on the crossover of the moving averages and the additional signals. 4. Rebalance the portfolio accordingly, ensuring the total exposure does not exceed 100%.

## Required Keys
- None
