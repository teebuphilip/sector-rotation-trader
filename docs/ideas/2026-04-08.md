# Reddit Subreddit Sentiment Spike

**Idea ID:** `reddit-subreddit-sentiment-spike`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Sudden spikes in positive sentiment and activity within finance-related subreddits often precede short-term price moves in related stocks or ETFs. By monitoring sentiment and volume of posts/comments on targeted subreddits, this signal aims to capture early retail enthusiasm shifts that may drive momentum.

## Universe
- SPY
- GME
- AMC
- AAPL
- TSLA
- MSFT

## Data Sources
- Reddit API (r/wallstreetbets, r/stocks, r/investing)
- Free sentiment analysis libraries (e.g., VADER, TextBlob)
- Yahoo Finance (for price data)

## Signal Logic
Calculate daily post and comment volume on selected subreddits. Compute average sentiment scores for all posts/comments each day. Trigger signal when daily volume exceeds 150% of 7-day average AND average sentiment is above 0.3 (on a -1 to 1 scale).

## Entry / Exit
Entry: Buy at next market open when signal triggers. Exit: Sell when daily sentiment drops below 0 or volume falls below 80% of 7-day average.

## Position Sizing
Allocate 5% of portfolio per triggered asset. Limit total exposure to 20% to diversify across signals.

## Risks
High noise and false positives due to hype cycles. Sentiment may be manipulated or delayed. Stocks may be illiquid or volatile. Correlation between subreddit sentiment and price may weaken over time.

## Implementation Notes
Use Reddit API to collect daily post and comment counts and text from target subreddits. Apply sentiment analysis on text data. Aggregate sentiment and volume metrics daily. Compare with rolling averages to detect spikes. Integrate with price data to execute trades based on signals.

## Required Keys
- None
