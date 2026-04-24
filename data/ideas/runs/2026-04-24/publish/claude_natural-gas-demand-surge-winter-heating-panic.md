# Natural Gas Demand Surge Winter Heating Panic

**Idea ID:** `natural-gas-demand-surge-winter-heating-panic`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
EIA reports weekly natural gas storage drawdowns >50 Bcf above seasonal norms during cold snaps, driving energy utility demand spikes. Utilities benefit from high demand periods and pass through energy cost recoveries.

## Universe
- XLU

## Data Sources
- EIA natural gas weekly storage and demand via eia_electricity adapter (extended to gas data)

## Signal Logic
If weekly gas storage draw > 50 Bcf above 5-year average for that week, long XLU

## Entry / Exit
Entry: If weekly gas storage draw > 50 Bcf above 5-year average for that week, long XLU Exit: Exit after 8 trading days or if storage normalization resumes

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use EIA natural gas weekly storage and demand via eia_electricity adapter (extended to gas data) via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Winter heating demand triggers multiple storage spikes per season; this fires most weeks November–March and occasionally in shoulder months.

## Required Keys
- None
