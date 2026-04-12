# Reddit Subreddit Mention Spike

**Idea ID:** `reddit-subreddit-mention-spike`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Sudden spikes in mentions of a ticker symbol within relevant Reddit subreddits can indicate growing retail interest or emerging news before traditional sources react. By tracking daily mention counts and identifying abnormal surges, one can capture early momentum shifts driven by social sentiment. This signal aims to exploit short-term price moves triggered by viral retail investor activity.

## Universe
- TSLA
- AAPL
- GME
- AMC
- NVDA
- MSFT
- AMD

## Data Sources
- Pushshift Reddit API (https://pushshift.io/)
- Yahoo Finance (for price data)

## Signal Logic
Calculate the daily mention count of a ticker symbol (e.g., $TSLA) in selected finance-related subreddits (e.g., r/stocks, r/investing, r/wallstreetbets). Define a baseline as the 14-day moving average of mentions. Generate a signal when today's mention count exceeds the baseline by at least 150%. Confirm price is above its 20-day moving average.

## Entry / Exit
Entry (Buy): When mention count spike condition is met and price > 20-day SMA. Exit (Sell): When mention counts revert below the 14-day moving average or price falls below the 20-day SMA.

## Position Sizing
Allocate 5% of portfolio per position to limit exposure to volatile social-driven moves.

## Risks
High noise and false positives from spam or bot activity. Sudden spikes may not translate to price moves. Price reversals can be sudden and sharp. Limited to well-discussed tickers with sufficient Reddit volume.

## Implementation Notes
1) Use Pushshift API to query daily Reddit submissions and comments mentioning ticker symbols in target subreddits. 2) Compute daily mention counts and moving averages. 3) Pull daily price data from Yahoo Finance. 4) Apply signal logic to generate buy/sell triggers. 5) Backtest on historical data to validate.

## Required Keys
- None
