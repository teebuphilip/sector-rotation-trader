# Fintech Disruption Wave

**Idea ID:** `fintech-disruption-wave`
**Source:** anthropic / claude-3-haiku-20240307
**Frequency:** daily

## Thesis
Surges in FinTech news coverage often precede shifts in consumer and institutional adoption of financial technology. Financial sector will benefit from the growth of financial technology and digital services.

## Universe
- XLF

## Data Sources
- RSS feed counts for FinTech news articles through rss_count adapter

## Signal Logic
If the daily FinTech news article count exceeds the prior 7-day average by 30%

## Entry / Exit
Entry: If the daily FinTech news article count exceeds the prior 7-day average by 30% Exit: After 10 trading days or when the daily news count falls below 10% above the prior 7-day average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS feed counts for FinTech news articles through rss_count adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: The FinTech industry experiences rapid evolution and innovation that frequently generates spikes in media coverage.

## Required Keys
- None
