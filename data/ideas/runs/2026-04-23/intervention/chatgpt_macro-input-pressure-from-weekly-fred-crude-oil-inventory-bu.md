# Macro Input Pressure From Weekly Fred Crude Oil Inventory Builds Signals Bearish Xle

**Idea ID:** `macro-input-pressure-from-weekly-fred-crude-oil-inventory-bu`
**Family:** `macro_input_pressure`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising crude oil inventories generally depress energy prices, pressuring energy sector stocks. Inventory builds often forecast weaker oil prices and energy company earnings.

## Universe
- XLE

## Data Sources
- FRED weekly crude oil inventory levels

## Signal Logic
Enter short XLE when crude inventories rise 5%+ over prior 2 weeks

## Entry / Exit
Entry: Enter short XLE when crude inventories rise 5%+ over prior 2 weeks Exit: Exit after 3 weeks or when inventories decline 3%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED weekly crude oil inventory levels via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 36
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Weekly crude inventories frequently change due to refinery cycles and geopolitical events.

## Required Keys
- None
