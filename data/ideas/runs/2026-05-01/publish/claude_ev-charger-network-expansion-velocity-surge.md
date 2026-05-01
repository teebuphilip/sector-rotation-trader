# Ev Charger Network Expansion Velocity Surge

**Idea ID:** `ev-charger-network-expansion-velocity-surge`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Rapid week-over-week increases in public EV charger installations signal acceleration in green infrastructure capex, indicating bullish macro stimulus or corporate EV investment push. Industrial sector benefits from infrastructure spending and EV supply chain acceleration.

## Universe
- XLI

## Data Sources
- OpenChargeMap API daily charger count by region through openchargemap adapter

## Signal Logic
If weekly charger count increase exceeds 3% week-over-week and 7-day moving average is positive

## Entry / Exit
Entry: If weekly charger count increase exceeds 3% week-over-week and 7-day moving average is positive Exit: After 10 trading days or if weekly growth falls below 1%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use OpenChargeMap API daily charger count by region through openchargemap adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: EV charger networks expand consistently; 3% weekly growth occurs multiple times per quarter in most regions.

## Required Keys
- None
