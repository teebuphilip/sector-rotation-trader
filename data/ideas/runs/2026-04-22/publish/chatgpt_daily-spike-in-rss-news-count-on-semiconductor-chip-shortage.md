# Daily Spike In Rss News Count On Semiconductor Chip Shortages With Bearish Xlk Reaction

**Idea ID:** `daily-spike-in-rss-news-count-on-semiconductor-chip-shortage`
**Family:** `attention_sentiment`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Sudden news surges on chip shortages often precede tech sector share price pressure. Chip shortage news weighs on technology stocks.

## Universe
- XLK

## Data Sources
- RSS daily news count for 'chip shortage' and Yahoo Finance daily XLK prices

## Signal Logic
Short XLK when daily RSS news count for 'chip shortage' doubles day-over-day and XLK underperforms SPY

## Entry / Exit
Entry: Short XLK when daily RSS news count for 'chip shortage' doubles day-over-day and XLK underperforms SPY Exit: Cover after 5 trading days or when news count normalizes

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS daily news count for 'chip shortage' and Yahoo Finance daily XLK prices via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Chip shortage news spikes frequently with industry developments.

## Required Keys
- None
