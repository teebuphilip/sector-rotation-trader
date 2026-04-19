# Utility Power Grid Stress

**Idea ID:** `utility-power-grid-stress`
**Source:** anthropic / claude-3-haiku-20240307
**Frequency:** weekly

## Thesis
Spikes in electricity demand can strain the power grid and drive increased investment in utility infrastructure. Utilities will benefit from the need to upgrade and expand the power grid.

## Universe
- XLU

## Data Sources
- EIA electricity demand data through eia_electricity adapter

## Signal Logic
If the weekly change in electricity demand exceeds 5% above the prior 4-week average

## Entry / Exit
Entry: If the weekly change in electricity demand exceeds 5% above the prior 4-week average Exit: After 2 weeks or when the weekly change falls below 2% above the prior 4-week average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use EIA electricity demand data through eia_electricity adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Seasonal changes in electricity demand and extreme weather events can frequently trigger this signal.

## Required Keys
- None
