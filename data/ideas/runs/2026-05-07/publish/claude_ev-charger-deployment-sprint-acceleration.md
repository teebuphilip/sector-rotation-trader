# Ev Charger Deployment Sprint Acceleration

**Idea ID:** `ev-charger-deployment-sprint-acceleration`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
EV charger installation rates spike quarterly when federal or state incentive windows open, signaling infrastructure investment demand and energy sector capex momentum. EV charging infrastructure expansion directly correlates with energy transition capex and utility modernization demand.

## Universe
- XLE

## Data Sources
- OpenChargeMap API daily charger count growth across US networks

## Signal Logic
When weekly charger count growth exceeds 3-month rolling average by 40% or more

## Entry / Exit
Entry: When weekly charger count growth exceeds 3-month rolling average by 40% or more Exit: After 10 trading days or when growth falls back to 3-month average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use OpenChargeMap API daily charger count growth across US networks via api (daily).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Charger deployment cycles are predictable and tied to incentive program rollouts; growth surges occur 2-4 times per year.

## Required Keys
- None
