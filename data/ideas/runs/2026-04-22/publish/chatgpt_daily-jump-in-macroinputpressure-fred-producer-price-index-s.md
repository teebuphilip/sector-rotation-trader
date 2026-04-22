# Daily Jump In Macroinputpressure Fred Producer Price Index Surge Signals Inflation Pressure

**Idea ID:** `daily-jump-in-macroinputpressure-fred-producer-price-index-s`
**Family:** `macro_input_pressure`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
A sudden producer price index increase signals rising input costs that may pressure earnings and valuations. Financials can be hurt by inflation-driven economic uncertainty and rate volatility.

## Universe
- XLF

## Data Sources
- FRED daily producer price index

## Signal Logic
Entry when daily PPI rises more than 0.3% compared to prior day

## Entry / Exit
Entry: Entry when daily PPI rises more than 0.3% compared to prior day Exit: Exit after 7 trading days or once PPI growth slows below 0.1%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED daily producer price index via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 36
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Daily PPI data exhibits frequent upward volatility due to supply shocks.

## Required Keys
- None
