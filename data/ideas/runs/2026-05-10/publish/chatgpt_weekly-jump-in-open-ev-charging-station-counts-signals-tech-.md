# Weekly Jump In Open Ev Charging Station Counts Signals Tech Sector Green Energy Adoption Strength

**Idea ID:** `weekly-jump-in-open-ev-charging-station-counts-signals-tech-`
**Family:** `macro_input_pressure`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising counts of operational EV chargers reflect accelerating green energy infrastructure rollout. Tech sector benefits from EV adoption as a driver of innovation and growth.

## Universe
- XLK

## Data Sources
- OpenChargeMap weekly EV charger count via openchargemap adapter

## Signal Logic
If weekly charger count increases more than 3% week-over-week

## Entry / Exit
Entry: If weekly charger count increases more than 3% week-over-week Exit: When growth falls below 1%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use OpenChargeMap weekly EV charger count via openchargemap adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: EV infrastructure growth is steady with weekly fluctuations.

## Required Keys
- None
