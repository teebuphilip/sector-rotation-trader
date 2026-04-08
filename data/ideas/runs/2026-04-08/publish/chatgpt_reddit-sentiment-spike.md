# Reddit Sentiment Spike

**Idea ID:** `reddit-sentiment-spike`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Sudden spikes in positive sentiment towards specific stocks on Reddit communities like r/stocks or r/investing often precede short-term price movements as retail trader interest surges. By tracking the daily sentiment score changes, one can detect emerging momentum before widespread recognition. This can provide early entry signals for momentum-driven trades.

## Universe
- AAPL
- TSLA
- AMD
- MSFT
- NVDA
- AMZN
- GOOGL
- META
- NFLX
- BABA

## Data Sources
- Pushshift Reddit API
- Reddit public posts and comments

## Signal Logic
Calculate daily sentiment score for each stock ticker mentioned on Reddit using simple polarity analysis. Identify tickers with an increase in sentiment score exceeding 40% compared to the previous day and mention volume above 50 posts/comments.

## Entry / Exit
Entry: Buy at next market open when sentiment spike is confirmed. Exit: Sell when sentiment score drops below 80% of spike day's peak or after 5 trading days, whichever is earlier.

## Position Sizing
Allocate 2% of portfolio per position, limit to 5 concurrent positions to manage risk.

## Risks
Sentiment spikes may be driven by hype, misinformation, or short-term noise leading to false signals. Sudden market-wide events can override signals. Low liquidity stocks may have exaggerated sentiment effects.

## Implementation Notes
1) Use Pushshift API to collect daily Reddit posts/comments mentioning tickers. 2) Perform sentiment analysis using a lexicon-based approach (e.g., VADER). 3) Calculate daily sentiment score and volume per ticker. 4) Identify spikes per signal logic. 5) Generate trade signals and track exit conditions.

## Required Keys
- None
