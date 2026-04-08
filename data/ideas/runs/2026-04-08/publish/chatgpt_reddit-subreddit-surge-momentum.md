# Reddit Subreddit Surge Momentum

**Idea ID:** `reddit-subreddit-surge-momentum`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Sudden surges in mentions of a stock ticker within specific finance-related subreddits often precede increased retail investor interest and potential short-term price movements. By tracking the daily percentage increase in mentions, one can capture early momentum shifts driven by the retail crowd before they fully materialize in price.

## Universe
- AAPL
- TSLA
- AMC
- GME
- NVDA
- MSFT
- AMD
- NIO
- PLTR
- NFLX

## Data Sources
- Pushshift Reddit API
- Yahoo Finance for price data

## Signal Logic
Calculate the daily count of mentions of a ticker’s cashtag (e.g., $TSLA) in r/wallstreetbets, r/investing, and r/stocks. Generate a 3-day moving average of mentions. Signal triggers when daily mentions increase by more than 100% compared to the 3-day moving average and the average mentions are above 20 posts per day.

## Entry / Exit
Enter a long position at market open the day after the surge. Exit when mentions fall below the 3-day moving average or after 5 trading days, whichever comes first.

## Position Sizing
Allocate 5% of portfolio per signal, max 3 concurrent positions. Reduce size by 50% if market volatility (VIX) is above 25.

## Risks
High noise and false positives due to meme stock hype. Mentions may spike without price follow-through. Risk of sudden short squeezes or dumps. Data latency and API rate limits may delay signals.

## Implementation Notes
Use Pushshift API to collect daily subreddit comments filtered by cashtag mentions. Aggregate counts per ticker and compute moving averages. Combine with Yahoo Finance price data to backtest. Automate daily data pulls and signal generation with scheduled scripts.

## Required Keys
- None
