# Weekly Rise In Fred Data For Producer Price Index Energy Component Signals Inflation Pressure On Energy Sector

**Idea ID:** `weekly-rise-in-fred-data-for-producer-price-index-energy-com`
**Family:** `macro_input_pressure`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Increasing PPI for energy signals rising input costs that often translate into higher energy sector revenues and volatility. Higher producer prices support energy firm earnings and valuations.

## Universe
- XLE

## Data Sources
- FRED Producer Price Index: Energy

## Signal Logic
If weekly PPI energy index rises >0.3% week-over-week

## Entry / Exit
Entry: If weekly PPI energy index rises >0.3% week-over-week Exit: After 4 weeks or when growth slows below 0.1% weekly

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED Producer Price Index: Energy via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 36
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Energy input prices fluctuate with commodity markets and seasonal demand.

## Required Keys
- None
