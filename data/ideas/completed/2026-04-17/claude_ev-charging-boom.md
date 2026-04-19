# Ev Charging Boom

**Idea ID:** `ev-charging-boom`
**Source:** anthropic / claude-3-haiku-20240307
**Frequency:** weekly

## Thesis
EV adoption and charging infrastructure growth tend to drive demand for materials, equipment, and utilities needed to support the transition. Basic materials and industrials will benefit from the EV charging buildout.

## Universe
- XLB

## Data Sources
- EV charger count data from OpenChargeMap through openchargemap adapter

## Signal Logic
If the weekly growth rate in total EV chargers exceeds 3%

## Entry / Exit
Entry: If the weekly growth rate in total EV chargers exceeds 3% Exit: After 4 weeks or when the weekly growth rate falls below 2%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use EV charger count data from OpenChargeMap through openchargemap adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Rapid EV adoption and charging infrastructure expansion is an ongoing trend that frequently triggers the signal.

## Required Keys
- None
