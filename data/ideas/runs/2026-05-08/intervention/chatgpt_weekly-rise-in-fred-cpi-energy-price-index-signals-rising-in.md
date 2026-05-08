# Weekly Rise In Fred Cpi Energy Price Index Signals Rising Input Cost Pressure On Energy Sector

**Idea ID:** `weekly-rise-in-fred-cpi-energy-price-index-signals-rising-in`
**Family:** `macro_input_pressure`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
A fast increase in energy CPI indicates rising costs that typically lead to energy sector margin expansion as prices rise. Energy producers benefit from rising energy prices and input cost pass-through.

## Universe
- XLE

## Data Sources
- FRED CPI Energy Price Index

## Signal Logic
If weekly CPI energy price index rises 1% week-over-week

## Entry / Exit
Entry: If weekly CPI energy price index rises 1% week-over-week Exit: Once growth slows to below 0.25% week-over-week

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED CPI Energy Price Index via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 36
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Energy prices fluctuate regularly due to geopolitical and supply shocks.

## Required Keys
- None
