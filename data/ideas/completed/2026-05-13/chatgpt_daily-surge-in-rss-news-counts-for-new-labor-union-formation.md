# Daily Surge In Rss News Counts For New Labor Union Formations Signals Labor Market Pressure On Industrial Sector

**Idea ID:** `daily-surge-in-rss-news-counts-for-new-labor-union-formation`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Rising news volume on new labor union formations signals growing worker organization activity that can pressure wages and output. Unionization drives labor cost increases and operational disruptions.

## Universe
- XLI

## Data Sources
- RSS news feed counts

## Signal Logic
If daily RSS counts for 'new labor union' news rise 30% day-over-day

## Entry / Exit
Entry: If daily RSS counts for 'new labor union' news rise 30% day-over-day Exit: After 7 trading days or when counts fall 20% from peak

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS news feed counts via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Union news spikes during contract negotiation periods and labor activism cycles.

## Required Keys
- None
