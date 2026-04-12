# Social Media Sentiment Spike

**Idea ID:** `social-media-sentiment-spike`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Sudden spikes in positive sentiment on social media platforms around a stock often precede short-term price rallies. By tracking keyword and hashtag sentiment changes on Twitter and Reddit, we can identify early bullish momentum. This signal leverages public sentiment shifts before they fully reflect in price.

## Universe
- AAPL
- TSLA
- AMZN
- MSFT
- NVDA
- NFLX
- GOOGL
- META

## Data Sources
- Twitter API (free tier)
- Pushshift Reddit API
- Finnhub News Sentiment API (free tier)

## Signal Logic
Calculate daily sentiment score for each ticker based on related tweets and Reddit posts using keyword matching. Signal triggers when the daily sentiment score increases by more than 30% compared to the 7-day moving average, with at least 100 posts mentioning the ticker that day.

## Entry / Exit
Buy at market open the day after a sentiment spike signal. Sell when sentiment reverts below the 7-day average or after 5 trading days, whichever comes first.

## Position Sizing
Allocate 2% of portfolio per position, capped at 10 simultaneous positions to diversify risk.

## Risks
False sentiment spikes due to bots or coordinated social campaigns may cause whipsaws. Low volume tickers may generate unreliable sentiment data. Sudden news events not captured in social data can invalidate the signal.

## Implementation Notes
1) Collect tweets and Reddit posts mentioning each ticker daily. 2) Perform simple sentiment analysis using lexicon-based scoring or pretrained models. 3) Compute daily sentiment score and compare against 7-day moving average. 4) Generate signals and track open positions. 5) Implement position sizing and risk controls.

## Required Keys
- Twitter API key
