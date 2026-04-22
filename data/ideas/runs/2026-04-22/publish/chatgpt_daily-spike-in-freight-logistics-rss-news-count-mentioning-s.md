# Daily Spike In Freight Logistics Rss News Count Mentioning Supply Chain Disruption

**Idea ID:** `daily-spike-in-freight-logistics-rss-news-count-mentioning-s`
**Family:** `freight_logistics`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Sudden surge in supply chain disruption news indicates growing logistics bottlenecks. Logistics bottlenecks pressure industrial and transportation companies.

## Universe
- XLI

## Data Sources
- RSS feed counts for freight logistics news mentioning 'supply chain disruption'

## Signal Logic
If daily news count spikes 50% above 7-day average

## Entry / Exit
Entry: If daily news count spikes 50% above 7-day average Exit: After 5 trading days or news count normalizes below 10% over 7-day average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS feed counts for freight logistics news mentioning 'supply chain disruption' via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Daily news flow about supply chain issues is volatile and frequently spikes.

## Required Keys
- None
