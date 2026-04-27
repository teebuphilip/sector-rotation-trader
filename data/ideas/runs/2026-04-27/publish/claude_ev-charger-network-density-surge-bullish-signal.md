# Ev Charger Network Density Surge Bullish Signal

**Idea ID:** `ev-charger-network-density-surge-bullish-signal`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Rapid weekly increases in public EV charger deployment signal infrastructure capex momentum and green energy transition acceleration, which historically precedes XLK and XLI strength. EV charger buildout drives tech hardware demand and signals bullish macro sentiment on energy transition.

## Universe
- XLK

## Data Sources
- OpenChargeMap API daily charger counts by region

## Signal Logic
If weekly EV charger count growth exceeds 2.5% in any US region and total count crosses prior 52-week percentile 75th, go long XLK.

## Entry / Exit
Entry: If weekly EV charger count growth exceeds 2.5% in any US region and total count crosses prior 52-week percentile 75th, go long XLK. Exit: After 10 trading days or if weekly growth drops below 1%.

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use OpenChargeMap API daily charger counts by region via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Infrastructure expansion is ongoing; charger networks are actively scaling in major US metros.

## Required Keys
- None
