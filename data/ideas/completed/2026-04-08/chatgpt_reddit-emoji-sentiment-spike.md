# Reddit Emoji Sentiment Spike

**Idea ID:** `reddit-emoji-sentiment-spike`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Sudden spikes in positive or negative emoji usage in subreddit comment streams can indicate rapid shifts in retail trader sentiment before price moves. By tracking the frequency of bullish emojis (e.g., 🚀, 💎, 🦍) versus bearish emojis (e.g., 🐻, 💀, 🔻) in comments mentioning stocks, one can generate early trading signals. These sentiment surges often precede volatility and directional moves in the underlying assets.

## Universe
- AAPL
- TSLA
- AMD
- GME
- AMC
- NVDA
- MSFT
- NFLX

## Data Sources
- Reddit API (public endpoints)
- Yahoo Finance (for price and volume data)

## Signal Logic
For each stock ticker mentioned in r/wallstreetbets and r/stocks comments daily, calculate the ratio of bullish to bearish emojis. Generate a buy signal if the bullish emoji ratio increases by more than 150% day-over-day and the total mention volume increases by at least 50%. Generate a sell signal if the bearish emoji ratio increases by more than 150% under the same volume conditions.

## Entry / Exit
Entry: Buy at next market open after bullish emoji ratio spike. Exit: Sell at next market open after bearish emoji ratio spike or after 5 trading days, whichever comes first.

## Position Sizing
Allocate 2% of portfolio per position to limit exposure to false positives given noisy sentiment data.

## Risks
Emoji usage can be noisy and sarcastic, leading to false signals. Sudden spikes may be driven by bots or coordinated campaigns. Low liquidity stocks may experience exaggerated moves unrelated to fundamentals. Timing mismatch between sentiment spikes and price moves can cause losses.

## Implementation Notes
1) Use Reddit API to fetch daily comments from target subreddits. 2) Parse comments for ticker mentions and emojis. 3) Calculate daily bullish/bearish emoji ratios per ticker. 4) Compare ratios day-over-day and filter by mention volume thresholds. 5) Generate signals and backtest with historical price data from Yahoo Finance.

## Required Keys
- None
