# Eia Electricity Demand Shock Rebound Spread

**Idea ID:** `eia-electricity-demand-shock-rebound-spread`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Sharp week-over-week drops in electricity demand (>8%) often indicate demand shock or recession fears, which revert quickly as underlying activity resumes or weather normalizes. Demand collapses are often temporary; utilities rebound as demand normalizes, and utility stocks offer defensive stability.

## Universe
- XLU

## Data Sources
- EIA weekly electricity demand (net generation MWh) through eia_electricity adapter, tracked regionally

## Signal Logic
If weekly electricity demand drops >8% from prior week, long XLU

## Entry / Exit
Entry: If weekly electricity demand drops >8% from prior week, long XLU Exit: After 7 trading days or if demand recovers >4%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use EIA weekly electricity demand (net generation MWh) through eia_electricity adapter, tracked regionally via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Seasonal demand swings, weather volatility, and demand shocks produce >8% weekly moves 3–5 times annually.

## Required Keys
- None
