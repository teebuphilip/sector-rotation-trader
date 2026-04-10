# Google Trends Surge Momentum

**Idea ID:** `google-trends-surge-momentum`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Sudden surges in Google search interest for a company's brand or product often precede significant price movements as retail and institutional investors react to emerging news or hype. By capturing rapid week-over-week increases in search volume, we can identify stocks with growing public attention that may experience short-term momentum. This signal exploits the crowd's early reaction before broader market pricing.

## Universe
- AAPL
- AMZN
- TSLA
- NFLX
- NVDA
- META
- GOOGL
- MSFT
- DIS
- PFE

## Data Sources
- Google Trends (https://trends.google.com)

## Signal Logic
For each ticker, map it to its primary brand or product keyword. Calculate the week-over-week percentage increase in Google Trends search interest. Generate a buy signal if the search interest increases by more than 50% compared to the previous week, with a minimum baseline interest score of 20 to avoid noise.

## Entry / Exit
Enter (buy) at the next market open after a qualifying Google Trends surge. Exit (sell) after 10 trading days or if the weekly search interest falls below 15, whichever comes first.

## Position Sizing
Allocate 2% of portfolio capital per position, scaling down to 1% if the stock's average daily volume is below 1 million shares to reduce liquidity risk.

## Risks
False positives from unrelated spikes in search interest, e.g., news unrelated to fundamentals; lag in data availability could delay signals; low search volume stocks may give noisy signals; sudden negative news can cause sharp reversals despite search interest surge.

## Implementation Notes
Map each ticker to a Google Trends search term (usually the brand name). Use Google Trends API or web scraping with pytrends to fetch weekly normalized search interest. Calculate percent increase week-over-week. Filter by thresholds and generate signals. Backtest entry and exit rules on historical data. Automate weekly updates and signal generation.

## Required Keys
- None
