# Electricity Demand Spike Weather Anomaly

**Idea ID:** `electricity-demand-spike-weather-anomaly`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Daily electricity demand exceeds 30-day average by 15% while temperature is 10+ degrees above seasonal normal, signaling heat stress and utility margin compression. Extreme demand spikes during heat waves reduce utility margins, strain grid capacity, and increase regulatory scrutiny.

## Universe
- XLU

## Data Sources
- EIA electricity demand (total US, daily) through eia_electricity adapter combined with Open-Meteo daily temperature through weather_series adapter

## Signal Logic
If daily electricity demand is 15%+ above 30-day rolling average and daily temp is 10+ degrees above normal for region

## Entry / Exit
Entry: If daily electricity demand is 15%+ above 30-day rolling average and daily temp is 10+ degrees above normal for region Exit: After 5 trading days or when daily demand returns to within 5% of 30-day average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use EIA electricity demand (total US, daily) through eia_electricity adapter combined with Open-Meteo daily temperature through weather_series adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Heat waves and demand spikes occur 4-6 times in summer months; threshold fires multiple times per June-September.

## Required Keys
- None
