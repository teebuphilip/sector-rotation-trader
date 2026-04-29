# Weekly Fred Series Jump In Producer Price Index Signals Bearish Basic Materials

**Idea ID:** `weekly-fred-series-jump-in-producer-price-index-signals-bear`
**Family:** `macro_input_pressure`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
A sudden increase in PPI signals rising input costs that compress margins for basic materials companies. Higher input costs reduce profitability in commodity and materials sectors.

## Universe
- XLB

## Data Sources
- FRED Producer Price Index (PPI) weekly derived

## Signal Logic
Enter short on XLB if weekly PPI rises by more than 0.7% week-over-week

## Entry / Exit
Entry: Enter short on XLB if weekly PPI rises by more than 0.7% week-over-week Exit: Exit after 4 weeks or when PPI growth slows below 0.2% weekly

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED Producer Price Index (PPI) weekly derived via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 36
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: PPI data often has periodic jumps reflecting commodity price shocks.

## Required Keys
- None
