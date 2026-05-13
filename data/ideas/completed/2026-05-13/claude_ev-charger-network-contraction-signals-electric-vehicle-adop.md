# Ev Charger Network Contraction Signals Electric Vehicle Adoption Slowdown

**Idea ID:** `ev-charger-network-contraction-signals-electric-vehicle-adop`
**Family:** `travel_mobility`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Charger count declines (due to removal or non-maintenance) signal reduced EV demand forecasts and subsidy cliff fears. Net charger count drops 8%+ over 4 weeks trigger EV/tech bearishness. EV charging infrastructure maturity is a leading indicator for EV adoption. Contraction signals weakening demand and policy headwinds for EV manufacturers.

## Universe
- XLK

## Data Sources
- OpenChargeMap weekly charger count snapshot by state/region through openchargemap adapter

## Signal Logic
When net active charger count (OpenChargeMap US total) declines 3% or more over 2 consecutive weeks AND prior month growth was positive

## Entry / Exit
Entry: When net active charger count (OpenChargeMap US total) declines 3% or more over 2 consecutive weeks AND prior month growth was positive Exit: After 12 trading days or when charger count growth returns to positive YoY change

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use OpenChargeMap weekly charger count snapshot by state/region through openchargemap adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Charger network fluctuates seasonally and with funding cycles. Stimulus cliffs, maintenance pauses, and demand shifts produce regular 2-5% weekly swings.

## Required Keys
- None
