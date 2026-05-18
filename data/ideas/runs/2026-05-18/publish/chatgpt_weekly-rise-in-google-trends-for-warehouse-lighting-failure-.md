# Weekly Rise In Google Trends For Warehouse Lighting Failure Signals Industrial Maintenance Cycle

**Idea ID:** `weekly-rise-in-google-trends-for-warehouse-lighting-failure-`
**Family:** `local_economy_weirdness`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Increased search interest suggests ramping maintenance activity in warehouse facilities. Maintenance and repair activity correlates with industrial sector health.

## Universe
- XLI

## Data Sources
- Google Trends weekly search interest for 'warehouse lighting failure'

## Signal Logic
If weekly searches rise 20% above 4-week average

## Entry / Exit
Entry: If weekly searches rise 20% above 4-week average Exit: Exit after 5 weeks or when searches fall below 10% increase

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'warehouse lighting failure' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Industrial maintenance queries spike with seasonal and operational cycles.

## Required Keys
- None
