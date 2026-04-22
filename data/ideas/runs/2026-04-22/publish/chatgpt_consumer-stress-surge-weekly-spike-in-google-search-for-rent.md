# Consumer Stress Surge Weekly Spike In Google Search For Rent Strike And Xli Weakness

**Idea ID:** `consumer-stress-surge-weekly-spike-in-google-search-for-rent`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising consumer stress around housing payments can presage reduced industrial demand due to broader economic caution. Industrial sector performance is sensitive to consumer financial stress signals.

## Universe
- XLI

## Data Sources
- Google Trends weekly for 'rent strike' and Yahoo Finance weekly XLI prices

## Signal Logic
Short XLI when 'rent strike' search interest rises over 20% week-over-week and XLI underperforms SPY

## Entry / Exit
Entry: Short XLI when 'rent strike' search interest rises over 20% week-over-week and XLI underperforms SPY Exit: Cover after 3 weeks or when search interest declines by 10% week-over-week

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly for 'rent strike' and Yahoo Finance weekly XLI prices via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Social stress searches commonly spike in reaction to economic uncertainty.

## Required Keys
- None
