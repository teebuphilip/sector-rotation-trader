# Rss Roar

**Idea ID:** `rss-roar`
**Source:** anthropic / claude-3-haiku-20240307
**Frequency:** daily

## Thesis
Spikes in industry-related news and media coverage can signal shifting investor sentiment and market volatility. Financial sector often experiences heightened volatility during periods of increased news and media attention.

## Universe
- XLF

## Data Sources
- RSS feed counts for key industry news terms through rss_count adapter

## Signal Logic
If the daily RSS feed count for a major industry term increases more than 20% above the prior 7-day average

## Entry / Exit
Entry: If the daily RSS feed count for a major industry term increases more than 20% above the prior 7-day average Exit: After 2 trading days or once the RSS count falls back to the prior 7-day average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS feed counts for key industry news terms through rss_count adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: RSS feed activity often exhibits regular daily and weekly patterns, with deviations from typical ranges.

## Required Keys
- None
