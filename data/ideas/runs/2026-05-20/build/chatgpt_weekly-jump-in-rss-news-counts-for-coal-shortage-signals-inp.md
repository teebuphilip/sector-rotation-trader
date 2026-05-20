# Weekly Jump In Rss News Counts For Coal Shortage Signals Input Cost Pressure In Materials

**Idea ID:** `weekly-jump-in-rss-news-counts-for-coal-shortage-signals-inp`
**Family:** `macro_input_pressure`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising news volume on coal shortages signals rising commodity input costs for materials companies. Input cost pressure from coal shortages reduces margins for basic materials producers.

## Universe
- XLB

## Data Sources
- RSS news feed counts

## Signal Logic
If weekly RSS news count for 'coal shortage' doubles WoW

## Entry / Exit
Entry: If weekly RSS news count for 'coal shortage' doubles WoW Exit: After 3 weeks or when counts revert below 1.5x baseline

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS news feed counts via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Commodity supply disruptions and related news frequently appear as energy markets fluctuate.

## Required Keys
- None
