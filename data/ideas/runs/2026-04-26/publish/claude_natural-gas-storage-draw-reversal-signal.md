# Natural Gas Storage Draw Reversal Signal

**Idea ID:** `natural-gas-storage-draw-reversal-signal`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Unexpected reversal from net storage draws to net builds signals demand destruction or supply shock, triggering rapid utility and commodity sector repricing. Reversal in gas storage trends signals weakening energy demand, refinery utilization pressure, and margin compression.

## Universe
- XLE

## Data Sources
- FRED series IMNRNSA (US EIA natural gas storage) weekly readings

## Signal Logic
If 4-week moving average of storage draws flips from negative to positive, short XLE

## Entry / Exit
Entry: If 4-week moving average of storage draws flips from negative to positive, short XLE Exit: After 4 weeks or if 4-week MA reverses back negative

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series IMNRNSA (US EIA natural gas storage) weekly readings via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Storage injection/withdrawal cycles flip seasonally and during demand shocks; reversals occur multiple times annually in response to weather and economic cycles.

## Required Keys
- None
