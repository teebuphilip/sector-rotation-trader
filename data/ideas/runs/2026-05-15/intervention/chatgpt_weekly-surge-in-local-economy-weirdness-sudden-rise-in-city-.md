# Weekly Surge In Local Economy Weirdness Sudden Rise In City Building Permit Denials

**Idea ID:** `weekly-surge-in-local-economy-weirdness-sudden-rise-in-city-`
**Family:** `local_economy_weirdness`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
A sharp increase in denied building permits signals local regulatory tightening and construction slowdown. Real estate and construction sectors react negatively to local regulatory hurdles.

## Universe
- XLRE

## Data Sources
- municipal building permit databases

## Signal Logic
If weekly denied permits exceed 40% above 12-week average

## Entry / Exit
Entry: If weekly denied permits exceed 40% above 12-week average Exit: When denial rate normalizes below 15% above average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use municipal building permit databases via scrape (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Local permit denials vary with political cycles and economic shifts causing regular weekly signals.

## Required Keys
- None
