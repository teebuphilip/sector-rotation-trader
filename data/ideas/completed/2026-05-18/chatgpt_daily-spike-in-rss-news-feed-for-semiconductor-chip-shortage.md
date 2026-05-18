# Daily Spike In Rss News Feed For Semiconductor Chip Shortage Signals Tech Sector Volatility

**Idea ID:** `daily-spike-in-rss-news-feed-for-semiconductor-chip-shortage`
**Family:** `attention_sentiment`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Sudden surge in news about chip shortages often triggers tech stock volatility and rotation. Chip shortages disrupt technology production and supply chains, pressuring tech stocks.

## Universe
- XLK

## Data Sources
- RSS news feed counts for 'semiconductor chip shortage'

## Signal Logic
If daily RSS count for chip shortage news doubles compared to 7-day average

## Entry / Exit
Entry: If daily RSS count for chip shortage news doubles compared to 7-day average Exit: Exit after 7 trading days or when count normalizes below 1.5x average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS news feed counts for 'semiconductor chip shortage' via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Chip supply issues are frequently in the news and fluctuate with supply chain events.

## Required Keys
- None
