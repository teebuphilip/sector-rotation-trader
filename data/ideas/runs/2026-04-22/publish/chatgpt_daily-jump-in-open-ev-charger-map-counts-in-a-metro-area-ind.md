# Daily Jump In Open Ev Charger Map Counts In A Metro Area Indicating Accelerated Ev Adoption

**Idea ID:** `daily-jump-in-open-ev-charger-map-counts-in-a-metro-area-ind`
**Family:** `local_economy_weirdness`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Spike in new EV chargers suggests accelerated local EV infrastructure deployment. Consumer discretionary EV-related firms benefit from infrastructure expansion.

## Universe
- XLY

## Data Sources
- OpenChargeMap daily new EV charger counts by metro area

## Signal Logic
If daily new charger count in metro increases 40% above 7-day average

## Entry / Exit
Entry: If daily new charger count in metro increases 40% above 7-day average Exit: After 7 trading days or if count falls below 10% above average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use OpenChargeMap daily new EV charger counts by metro area via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: EV infrastructure expansions happen frequently in waves and can be detected daily.

## Required Keys
- None
