# Daily Jump In Fred Series For Crude Oil Rig Count Signals Energy Sector Momentum Shift

**Idea ID:** `daily-jump-in-fred-series-for-crude-oil-rig-count-signals-en`
**Family:** `macro_input_pressure`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Increases in active rig count signal rising production activity and often precede energy sector price momentum. Energy sector benefits from increased drilling activity and future supply expectations.

## Universe
- XLE

## Data Sources
- FRED weekly crude oil rig count

## Signal Logic
Enter long XLE when weekly rig count rises 5%+ over previous week

## Entry / Exit
Entry: Enter long XLE when weekly rig count rises 5%+ over previous week Exit: Exit after 4 weeks or when rig counts retreat 3% below entry level

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED weekly crude oil rig count via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Rig count changes occur frequently with drilling activity cycles.

## Required Keys
- None
