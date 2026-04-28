# Utility Grid Strain Heat Wave Demand Spike

**Idea ID:** `utility-grid-strain-heat-wave-demand-spike`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When regional max temperatures exceed 95°F for 3+ consecutive days AND EIA electricity demand rises above its 30-day rolling average by >2%, grid strain intensifies and utilities face margin compression. Utilities see margin compression during demand spikes without proportional rate relief; operating costs rise faster than revenue.

## Universe
- XLU

## Data Sources
- Open-Meteo daily temperature anomalies and FRED electricity load series (API EIA_ELECTRICITY_DEMAND)

## Signal Logic
Max temp >95°F for 3 consecutive days AND EIA demand >102% of 30-day rolling mean

## Entry / Exit
Entry: Max temp >95°F for 3 consecutive days AND EIA demand >102% of 30-day rolling mean Exit: Temperature falls below 90°F or EIA demand normalizes below 100.5% of rolling mean, or after 10 trading days

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Open-Meteo daily temperature anomalies and FRED electricity load series (API EIA_ELECTRICITY_DEMAND) via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Summer heat waves occur reliably; electricity demand data updates daily. Signal fires multiple times annually during June–September.

## Required Keys
- None
