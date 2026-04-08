# Reddit Volatility Spike

**Idea ID:** `reddit-volatility-spike`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Sudden spikes in Reddit mentions of a stock combined with a surge in implied volatility can predict short-term price reversals or breakouts. Retail interest often precedes volatility expansions, creating trading opportunities by capturing momentum or mean reversion shortly after the spike.

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
- GOOGL

## Data Sources
- Pushshift Reddit API
- Yahoo Finance (implied volatility data via options prices)
- Alpha Vantage (free stock price and volume data)

## Signal Logic
1) Identify a 100%+ day-over-day increase in Reddit daily mentions of a ticker's cashtag or symbol on r/stocks or r/investing.
2) Confirm that the stock's implied volatility (IV) has increased by at least 10% over the previous trading day.
3) Entry signal triggers if both conditions are met on the same day.
4) Exit signal triggers when IV drops below its 5-day moving average or after 5 trading days, whichever comes first.

## Entry / Exit
Buy at market open the day after the signal triggers. Sell when IV drops below its 5-day moving average or hold for a maximum of 5 trading days to limit risk.

## Position Sizing
Allocate 2% of portfolio capital per trade to limit risk from volatility spikes and avoid overexposure to retail-driven moves.

## Risks
High false positives due to noise in Reddit mentions or IV spikes unrelated to fundamental news. Sudden regulatory actions or market-wide volatility can invalidate signal. Low liquidity stocks may have unreliable IV data.

## Implementation Notes
1) Use Pushshift API to query Reddit submissions and comments mentioning ticker cashtags daily.
2) Use Yahoo Finance or Alpha Vantage to fetch daily options IV and price data.
3) Calculate percentage changes and moving averages.
4) Backtest signal logic on historical data.
5) Automate daily execution with conditional checks.

## Required Keys
- None
