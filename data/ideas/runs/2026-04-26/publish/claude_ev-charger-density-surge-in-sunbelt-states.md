# Ev Charger Density Surge In Sunbelt States

**Idea ID:** `ev-charger-density-surge-in-sunbelt-states`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Rapid expansion of EV charging infrastructure signals accelerating capital deployment and grid stress in high-growth regions, often preceding utility rate pressure and industrial construction demand. Infrastructure buildout drives industrial demand for construction, electrical equipment, and smart grid technology.

## Universe
- XLI

## Data Sources
- OpenChargeMap API for daily EV charger count changes in TX, FL, AZ, NV regions

## Signal Logic
If weekly charger additions exceed 200-unit threshold in any tracked Sunbelt metro, enter long

## Entry / Exit
Entry: If weekly charger additions exceed 200-unit threshold in any tracked Sunbelt metro, enter long Exit: After 3 weeks or if weekly additions drop below 100 units

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use OpenChargeMap API for daily EV charger count changes in TX, FL, AZ, NV regions via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: EV charger deployment accelerates seasonally in Q1 and Q2; regional clusters frequently hit thresholds as utilities and private firms push infrastructure rollout.

## Required Keys
- None
