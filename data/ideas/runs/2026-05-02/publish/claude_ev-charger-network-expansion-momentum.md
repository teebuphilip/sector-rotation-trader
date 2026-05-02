# Ev Charger Network Expansion Momentum

**Idea ID:** `ev-charger-network-expansion-momentum`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Rapid growth in public EV charging infrastructure signals increased capex and demand for electric vehicle adoption, indicating macro tailwinds for industrials and materials. EV charger buildout requires metals, electrical infrastructure, and industrial construction—direct XLI exposure.

## Universe
- XLI

## Data Sources
- OpenChargeMap API daily charger count by region

## Signal Logic
If weekly net new chargers added exceeds 1500 units (7-day rolling average) above the prior month's median

## Entry / Exit
Entry: If weekly net new chargers added exceeds 1500 units (7-day rolling average) above the prior month's median Exit: After 10 trading days or when weekly charger additions drop below 1200 units

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use OpenChargeMap API daily charger count by region via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Regional charger buildout fluctuates seasonally and by policy; multiple regions typically add >1500 chargers per week during growth cycles.

## Required Keys
- None
