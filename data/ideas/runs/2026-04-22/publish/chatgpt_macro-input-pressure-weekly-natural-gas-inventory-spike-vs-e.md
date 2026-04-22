# Macro Input Pressure Weekly Natural Gas Inventory Spike Vs Energy Etf Drop

**Idea ID:** `macro-input-pressure-weekly-natural-gas-inventory-spike-vs-e`
**Family:** `macro_input_pressure`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rapid build in natural gas inventories while energy ETF drops signals oversupply and bearish pressure on energy prices. Energy inventories rising sharply usually precede energy price and sector pullbacks.

## Universe
- XLE

## Data Sources
- FRED weekly natural gas storage data

## Signal Logic
Enter short XLE if natural gas inventories rise >5% WoW and XLE declines >2% WoW

## Entry / Exit
Entry: Enter short XLE if natural gas inventories rise >5% WoW and XLE declines >2% WoW Exit: Exit after inventories stabilize or XLE recovers 3%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED weekly natural gas storage data via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 36
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Weekly natural gas inventory reports and energy ETF volatility frequently align.

## Required Keys
- None
