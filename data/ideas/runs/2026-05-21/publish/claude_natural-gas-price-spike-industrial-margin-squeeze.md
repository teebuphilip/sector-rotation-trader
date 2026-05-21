# Natural Gas Price Spike Industrial Margin Squeeze

**Idea ID:** `natural-gas-price-spike-industrial-margin-squeeze`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Natural gas prices spike >12% week-over-week, squeezing input costs for chemicals, fertilizer, and manufacturing. Industrial production relies on cheap energy input; sharp gas spikes compress margins and forward guidance.

## Universe
- XLI

## Data Sources
- FRED series DHHNGSP (Henry Hub Natural Gas Spot Price) daily via fred_series adapter

## Signal Logic
If DHHNGSP closes >12% above its 5-day MA and volume is above median

## Entry / Exit
Entry: If DHHNGSP closes >12% above its 5-day MA and volume is above median Exit: After 7 trading days or when DHHNGSP mean reverts within 5% of 5-day MA

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series DHHNGSP (Henry Hub Natural Gas Spot Price) daily via fred_series adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Natural gas is volatile; 12% weekly swings occur 6-10 times per year on weather and supply shocks.

## Required Keys
- None
