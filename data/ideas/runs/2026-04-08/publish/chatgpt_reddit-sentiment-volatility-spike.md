# Reddit Sentiment Volatility Spike

**Idea ID:** `reddit-sentiment-volatility-spike`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Sudden spikes in sentiment volatility on Reddit's r/investing subreddit often precede short-term price reversals in popular stocks discussed there. Tracking the daily variance in sentiment scores can reveal overreactions or panic moments where mean reversion trading can be profitable. By capturing these sentiment swings, traders can enter contrarian positions ahead of price corrections.

## Universe
- AAPL
- TSLA
- AMZN
- MSFT
- GME
- NVDA

## Data Sources
- Pushshift Reddit API (https://pushshift.io/)
- Yahoo Finance (historical price data)

## Signal Logic
1) Collect all posts and comments mentioning tickers in the universe on r/investing daily. 2) Compute daily sentiment scores per ticker using a simple lexicon-based sentiment analyzer. 3) Calculate daily volatility as the standard deviation of sentiment scores over a rolling 3-day window. 4) Signal triggers when sentiment volatility spikes above the 90th percentile of its historical distribution for that ticker.

## Entry / Exit
Entry: Buy if volatility spike occurs and the average sentiment score that day is negative (contrarian long). Sell if volatility spike occurs and average sentiment is positive (contrarian short). Exit positions when sentiment volatility drops below the 50th percentile or after 5 trading days.

## Position Sizing
Allocate 5% of portfolio per position, max 20% total exposure. Reduce size by half if average daily volume is below 1 million shares.

## Risks
Sentiment analysis errors, low Reddit mention volume causing noisy signals, stocks with high natural volatility may trigger false signals, sudden fundamental changes not reflected in social sentiment.

## Implementation Notes
1) Use Pushshift API to pull daily r/investing posts/comments mentioning each ticker. 2) Preprocess text and apply lexicon-based sentiment analysis (e.g., VADER). 3) Calculate rolling standard deviation of sentiment scores. 4) Compare against historical percentiles to identify spikes. 5) Backtest signals against Yahoo Finance price data for entry/exit logic.

## Required Keys
- None
