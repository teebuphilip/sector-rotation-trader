# Ev Charger Expansion Velocity Boom

**Idea ID:** `ev-charger-expansion-velocity-boom`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When weekly EV charger installation rate accelerates above 3% MoM, it signals infrastructure spending surge and green capex confidence, often preceding energy/materials sector rallies. EV charging expansion drives demand for electrical grid upgrades, renewable integration, and industrial construction materials.

## Universe
- XLE

## Data Sources
- OpenChargeMap daily charger counts by state through openchargemap adapter

## Signal Logic
If EV charger count growth rate exceeds 3% week-over-week average for 2 consecutive weeks

## Entry / Exit
Entry: If EV charger count growth rate exceeds 3% week-over-week average for 2 consecutive weeks Exit: After 15 trading days or if growth rate falls below 1.5% for 1 week

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use OpenChargeMap daily charger counts by state through openchargemap adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: EV infrastructure buildout is steady; weekly acceleration spikes occur 4-6 times yearly when government incentives or corporate targets drive deployment waves.

## Required Keys
- None
