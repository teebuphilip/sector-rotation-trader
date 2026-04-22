# Weekly Surge In Local Economy Weirdness City-level Building Permits Drop Sharply

**Idea ID:** `weekly-surge-in-local-economy-weirdness-city-level-building-`
**Family:** `local_economy_weirdness`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Sharp local drop in building permits signals regional economic cooling. Real estate sector sensitive to building activity trends.

## Universe
- XLRE

## Data Sources
- Stable public table of weekly city-level building permit counts

## Signal Logic
If weekly permit counts fall 20% below 4-week average for key metro

## Entry / Exit
Entry: If weekly permit counts fall 20% below 4-week average for key metro Exit: After 4 weeks or if permit counts recover above 10% of average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Stable public table of weekly city-level building permit counts via scrape (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Building permits fluctuate regularly with economic cycles and seasonal trends.

## Required Keys
- None
