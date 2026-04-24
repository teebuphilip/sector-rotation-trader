# Daily Spike In Rss News Counts Around Labor Union Contract Negotiation Signals Bearish Xlf

**Idea ID:** `daily-spike-in-rss-news-counts-around-labor-union-contract-n`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Heightened news flow about union contract talks often precedes labor disruptions affecting financial sector clients. Financial institutions face risk from client operational disruptions and wage inflation.

## Universe
- XLF

## Data Sources
- RSS news feed counts

## Signal Logic
If daily RSS count for 'labor union contract negotiation' exceeds 3x 20-day average

## Entry / Exit
Entry: If daily RSS count for 'labor union contract negotiation' exceeds 3x 20-day average Exit: Exit after 7 trading days or when RSS count drops below 1.5x average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS news feed counts via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 15
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Union negotiation news regularly spikes as contracts approach expiration dates.

## Required Keys
- None
