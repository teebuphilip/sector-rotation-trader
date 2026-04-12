# Reddit Mentions Volatility Spike

**Idea ID:** `reddit-mentions-volatility-spike`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Sudden spikes in the daily mention count of a stock ticker on Reddit's r/wallstreetbets often precede heightened volatility and potential price swings. By tracking the frequency of ticker mentions and combining it with realized volatility measures, traders can identify breakout or breakdown opportunities. This signal aims to capture momentum driven by retail investor attention surges.

## Universe
- AAPL
- TSLA
- GME
- AMC
- MSFT
- NVDA
- AMD
- NFLX
- META
- BABA

## Data Sources
- Pushshift Reddit API (for historical Reddit comments)
- Yahoo Finance (for price and volatility data)

## Signal Logic
1) Calculate the daily count of ticker mentions on r/wallstreetbets.
2) Compute a 5-day moving average of mention counts.
3) Identify days where mention count > 2x the 5-day moving average.
4) Calculate the 10-day realized volatility (standard deviation of log returns).
5) Confirm volatility is above the 30-day average volatility.
Signal triggers when both mention spike and volatility elevation occur simultaneously.

## Entry / Exit
Entry (Buy): On the day a mention spike combined with elevated volatility is detected, buy at close.
Exit (Sell): Exit after 5 trading days or if realized volatility drops below 80% of the 30-day average before 5 days.

## Position Sizing
Allocate 5% of portfolio capital per signal to limit exposure to volatile moves and diversify across multiple triggered tickers if applicable.

## Risks
High false positives from meme-driven noise without sustained price moves; sudden regulatory or news events can disrupt patterns; limited liquidity in smaller tickers can cause slippage; Reddit mention counts can be artificially inflated or spammed.

## Implementation Notes
1) Use Pushshift API to pull daily comment data filtered by ticker keywords from r/wallstreetbets.
2) Aggregate mention counts per ticker per day.
3) Fetch daily OHLC price data from Yahoo Finance to compute volatility and returns.
4) Implement moving average and threshold logic for signal generation.
5) Backtest signal with historical data to validate effectiveness.

## Required Keys
- None
