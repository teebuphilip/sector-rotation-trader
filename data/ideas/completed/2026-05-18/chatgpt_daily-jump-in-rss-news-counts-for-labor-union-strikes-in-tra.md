# Daily Jump In Rss News Counts For Labor Union Strikes In Transportation Sector

**Idea ID:** `daily-jump-in-rss-news-counts-for-labor-union-strikes-in-tra`
**Family:** `political_insider_filing`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Spike in strike news increases risk of logistics disruption impacting transportation-related sectors. Strikes reduce freight and industrial output, pressuring industrial stocks.

## Universe
- XLI

## Data Sources
- RSS news feed counts for 'transportation labor strike'

## Signal Logic
If daily RSS count doubles compared to 7-day average

## Entry / Exit
Entry: If daily RSS count doubles compared to 7-day average Exit: Exit after 7 trading days or when count normalizes below 1.5x average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS news feed counts for 'transportation labor strike' via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Labor strikes in transportation often emerge suddenly and get rapid media attention.

## Required Keys
- None
