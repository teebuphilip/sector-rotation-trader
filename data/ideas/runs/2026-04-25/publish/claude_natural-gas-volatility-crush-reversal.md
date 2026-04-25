# Natural Gas Volatility Crush Reversal

**Idea ID:** `natural-gas-volatility-crush-reversal`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When natural gas volatility drops below 30th percentile and price stabilizes above 50-day MA, it signals completion of selloff and impending recovery momentum, supporting energy sector rotations. Low volatility combined with price support often precedes natural gas recovery rallies and improved energy company cash flows.

## Universe
- XLE

## Data Sources
- Yahoo Finance daily natural gas futures (NG) prices and 20-day historical volatility

## Signal Logic
If 20-day realized volatility of NG futures falls below 25% AND NG closes above 50-day MA on 3 of last 4 trading days

## Entry / Exit
Entry: If 20-day realized volatility of NG futures falls below 25% AND NG closes above 50-day MA on 3 of last 4 trading days Exit: After 10 trading days or if NG volatility spikes above 40%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Yahoo Finance daily natural gas futures (NG) prices and 20-day historical volatility via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Commodity volatility cycles are predictable; natural gas volatility compression periods occur regularly with seasonal demand patterns and inventory management cycles.

## Required Keys
- None
