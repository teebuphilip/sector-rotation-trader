# Insider Trading Signals

**Idea ID:** `insider-trading-signals`
**Source:** anthropic / claude-3-haiku-20240307
**Frequency:** daily

## Thesis
Insiders at publicly traded companies often buy or sell their company's stock before major announcements. By tracking and analyzing these insider transactions, we can potentially identify trading signals to profit from before the wider market reacts.

## Universe
Russell 3000 index

## Data Sources
- SEC Insider Transactions (https://www.sec.gov/edgar/searchedgar/companysearch.html)

## Signal Logic
Monitor SEC filings for insider buy/sell transactions. Look for large transactions (e.g. over $100,000) by C-level executives or directors. Generate buy signal when insiders are buying, sell signal when insiders are selling.

## Entry / Exit
Buy when insider buying threshold is met, sell when insider selling threshold is met.

## Position Sizing
Size positions based on transaction size and confidence in signal. Larger transactions by senior insiders warrant larger position sizes.

## Risks
Insider transactions may not always predict future stock price movements. Insider trading laws and regulations must be carefully followed.

## Implementation Notes
Scrape SEC filings to extract insider transaction data. Analyze transaction size, insider role, and timing relative to upcoming events. Backtest signal logic and optimize position sizing.

## Required Keys
- None
