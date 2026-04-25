# Ev Charger Network Density Surge

**Idea ID:** `ev-charger-network-density-surge`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Rapid growth in public EV charger installation signals infrastructure spending acceleration and rising EV adoption confidence, which precedes automotive and energy sector rotation. EV charging infrastructure expansion correlates with energy transition capex cycles and utility modernization demand.

## Universe
- XLE

## Data Sources
- OpenChargeMap API daily charger count snapshots for top 10 US metros

## Signal Logic
If weekly net charger additions across monitored metros exceed 200 units and are 40% above 12-week rolling average

## Entry / Exit
Entry: If weekly net charger additions across monitored metros exceed 200 units and are 40% above 12-week rolling average Exit: After 10 trading days or if weekly charger additions drop below 12-week average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use OpenChargeMap API daily charger count snapshots for top 10 US metros via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Infrastructure deployment cycles are continuous; charger installation surges frequently occur during policy incentive windows and private capex pushes.

## Required Keys
- None
