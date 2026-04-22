# Macro Input Pressure Weekly Increase In Producer Price Index For Metals

**Idea ID:** `macro-input-pressure-weekly-increase-in-producer-price-index`
**Family:** `macro_input_pressure`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising input costs for metals pressures manufacturing margins, bearish for industrial materials sector. Higher input prices reduce profitability in materials and industrial sectors.

## Universe
- XLB

## Data Sources
- FRED weekly producer price index for metals

## Signal Logic
Enter short XLB if metal PPI rises >0.5% WoW for 2 weeks

## Entry / Exit
Entry: Enter short XLB if metal PPI rises >0.5% WoW for 2 weeks Exit: Exit after PPI growth slows below 0.2% WoW or after 4 weeks

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED weekly producer price index for metals via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 36
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: PPI data updates weekly and often shows volatile short-term trends.

## Required Keys
- None
