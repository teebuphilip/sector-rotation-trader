# Weekly Fred Series Spike In Producer Price Index Ppi Input Costs Signals Bearish Materials Sector

**Idea ID:** `weekly-fred-series-spike-in-producer-price-index-ppi-input-c`
**Family:** `macro_input_pressure`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
A sharp weekly rise in PPI input costs signals rising inflationary pressures on raw materials, squeezing margins in materials companies. Higher input costs reduce profitability for materials producers and pressure the sector.

## Universe
- XLB

## Data Sources
- FRED Producer Price Index (PPI) data

## Signal Logic
If weekly PPI input index rises by more than 1% vs prior week

## Entry / Exit
Entry: If weekly PPI input index rises by more than 1% vs prior week Exit: After 4 weeks or when PPI input index growth slows below 0.3%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED Producer Price Index (PPI) data via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 36
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: PPI input measures frequently spike during commodity price volatility periods.

## Required Keys
- None
