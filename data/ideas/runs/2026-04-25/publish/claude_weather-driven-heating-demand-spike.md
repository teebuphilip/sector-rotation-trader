# Weather-driven Heating Demand Spike

**Idea ID:** `weather-driven-heating-demand-spike`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Unexpected cold snaps drive heating fuel demand and natural gas consumption, creating short-term energy sector outperformance and utility cash flow tailwinds. Demand spikes for heating directly increase utility revenues and natural gas futures, supporting utility sector valuations.

## Universe
- XLU

## Data Sources
- Open-Meteo daily temperature data for US heating degree days across 5 regional hubs

## Signal Logic
If heating degree days exceed 65th percentile of trailing 30-day average and weekly volume on XLU rises 30% above baseline

## Entry / Exit
Entry: If heating degree days exceed 65th percentile of trailing 30-day average and weekly volume on XLU rises 30% above baseline Exit: After 7 trading days or if temperatures normalize and heating degree days fall below 45th percentile

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Open-Meteo daily temperature data for US heating degree days across 5 regional hubs via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Seasonal temperature volatility is guaranteed; heating demand spikes occur multiple times per winter and shoulder seasons.

## Required Keys
- None
