# Ev Charger Network Expansion Acceleration

**Idea ID:** `ev-charger-network-expansion-acceleration`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Rapid week-over-week growth in publicly available EV charging locations signals infrastructure investment momentum and policy acceleration, typically preceding EV sales surges. Industrial manufacturing and installation of charging infrastructure drives equipment, construction, and logistics demand.

## Universe
- XLI

## Data Sources
- OpenChargeMap API daily charger location counts by state/region

## Signal Logic
If weekly net new charger locations exceed 200-unit threshold above trailing 4-week average

## Entry / Exit
Entry: If weekly net new charger locations exceed 200-unit threshold above trailing 4-week average Exit: Exit after 10 trading days or if growth falls below 150-unit weekly pace

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use OpenChargeMap API daily charger location counts by state/region via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: EV infrastructure deployment is steady and continuous; weekly threshold breaches occur multiple times per quarter.

## Required Keys
- None
