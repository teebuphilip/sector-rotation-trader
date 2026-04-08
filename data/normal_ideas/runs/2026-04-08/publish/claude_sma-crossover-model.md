# Simple Moving Average Crossover Model

**Idea ID:** `sma-crossover-model`
**Source:** anthropic / claude-3-haiku-20240307
**Frequency:** daily

## Thesis
The simple moving average crossover model is a classic trend-following strategy that aims to capture sustained market movements by generating buy and sell signals based on the relationship between a short-term and a long-term moving average.

## Universe
- SPY
- QQQ
- IWM

## Data Sources
- yfinance

## Signal Logic
Generate a buy signal when the short-term (e.g., 50-day) moving average crosses above the long-term (e.g., 200-day) moving average. Generate a sell signal when the short-term moving average crosses below the long-term moving average.

## Entry / Exit
Buy when the buy signal is generated, sell when the sell signal is generated.

## Position Sizing
Equal-weight all positions in the portfolio.

## Risks
The model may generate false signals during periods of sideways market movement, leading to whipsaws and reduced performance. It is also sensitive to the choice of moving average windows.

## Implementation Notes
1. Calculate the 50-day and 200-day simple moving averages for each asset in the universe. 2. Compare the moving averages to generate buy and sell signals. 3. Implement position sizing and rebalancing logic.

## Required Keys
- None
