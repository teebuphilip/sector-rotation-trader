# Reddit Mentions Volatility Spike

**Idea ID:** `reddit-mentions-volatility-spike`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Sudden spikes in daily Reddit mentions of a stock ticker often precede short-term volatility bursts. By monitoring mentions on popular subreddits like r/WallStreetBets and r/stocks, we can detect unusual social interest that may drive price swings. This signal aims to capitalize on volatility expansion following social media hype or panic.

## Universe
- AAPL
- TSLA
- GME
- AMC
- MSFT
- NVDA
- AMD
- NFLX

## Data Sources
- Pushshift Reddit API
- Yahoo Finance (for price and volatility data)

## Signal Logic
Calculate the 7-day moving average of daily Reddit mentions of a ticker. If today's mentions exceed 3 times the 7-day average, and the stock's 14-day historical volatility is below its 30-day average, signal a volatility spike incoming.

## Entry / Exit
Entry (Buy a straddle or volatility ETF): When signal_logic triggers. Exit: When volatility returns above its 30-day average or after 5 trading days, whichever comes first.

## Position Sizing
Allocate 5% of portfolio per signal, scaling down linearly if multiple signals overlap to keep total exposure below 20%.

## Risks
High false positives if Reddit chatter is unrelated to fundamentals. Risk of sudden news events invalidating the pattern. Volatility may not increase despite chatter, causing losses in options or volatility products.

## Implementation Notes
1) Use Pushshift API to scrape daily Reddit comment counts mentioning ticker symbols in target subreddits. 2) Calculate moving averages and volatility using Yahoo Finance daily price data. 3) Implement logic to trigger and track open positions. 4) Automate daily signal generation and position management.

## Required Keys
- None
