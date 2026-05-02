# Eia Natural Gas Storage Build Momentum Divergence

**Idea ID:** `eia-natural-gas-storage-build-momentum-divergence`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When weekly gas storage builds accelerate >20% faster than the prior 4-week rolling average (suggesting oversupply), natural gas prices compress, hurting energy producer margins—bearish energy. Rapid storage accumulation signals weak demand or oversupply, driving down nat gas prices and producer revenue.

## Universe
- XLE

## Data Sources
- EIA Weekly Natural Gas Inventory Data (via FRED or EIA API)

## Signal Logic
If weekly storage build exceeds 4-week rolling average by >20% AND prior 2 weeks showed accelerating builds

## Entry / Exit
Entry: If weekly storage build exceeds 4-week rolling average by >20% AND prior 2 weeks showed accelerating builds Exit: After 10 trading days or when weekly build rate normalizes below 4-week mean

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use EIA Weekly Natural Gas Inventory Data (via FRED or EIA API) via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Seasonal gas storage cycles and weather-driven demand shifts trigger build acceleration signals 8-12 times per year.

## Required Keys
- None
