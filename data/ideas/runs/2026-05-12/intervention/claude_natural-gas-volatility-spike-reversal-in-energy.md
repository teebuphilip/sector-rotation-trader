# Natural Gas Volatility Spike Reversal In Energy

**Idea ID:** `natural-gas-volatility-spike-reversal-in-energy`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When 20-day rolling volatility of natural gas prices spikes above 2-year 95th percentile, mean reversion in energy equities often follows as supply shocks resolve. Extreme gas price volatility signals supply disruption; reversal attracts energy sector value buyers and reduces hedge costs.

## Universe
- XLE

## Data Sources
- FRED series DHHNGSP (Henry Hub natural gas spot price) daily closes for volatility calc

## Signal Logic
If 20-day rolling vol of DHHNGSP > 95th percentile over 2 years and XLE closes up >1% following a down day

## Entry / Exit
Entry: If 20-day rolling vol of DHHNGSP > 95th percentile over 2 years and XLE closes up >1% following a down day Exit: After 8 trading days or when 20-day vol falls below 80th percentile

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series DHHNGSP (Henry Hub natural gas spot price) daily closes for volatility calc via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Seasonal geopolitical and weather shocks drive gas price spikes multiple times per quarter.

## Required Keys
- None
