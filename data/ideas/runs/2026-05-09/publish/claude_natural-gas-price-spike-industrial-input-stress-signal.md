# Natural Gas Price Spike Industrial Input Stress Signal

**Idea ID:** `natural-gas-price-spike-industrial-input-stress-signal`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Natural gas price spikes compress margins for chemical, fertilizer, and power generation firms. Sharp intraweek rallies often reverse within 1–2 weeks as supply/demand rebalances. Industrial production and utilities are major gas consumers; price shocks raise input costs and trigger margin compression.

## Universe
- XLI

## Data Sources
- FRED series ID DHHNGSP (Henry Hub Natural Gas Spot Price) through fred_series adapter

## Signal Logic
If natural gas price rises more than 8% in a single week and closes above 5-week high

## Entry / Exit
Entry: If natural gas price rises more than 8% in a single week and closes above 5-week high Exit: After 7 trading days or if price falls below the 5-week moving average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series ID DHHNGSP (Henry Hub Natural Gas Spot Price) through fred_series adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Natural gas is volatile; 8% weekly moves occur 3–4 times per quarter, especially in winter and summer demand spikes.

## Required Keys
- None
