# Daily Spike In Weather-series Wind Speed Variability Signals Bullish Utilities Sector

**Idea ID:** `daily-spike-in-weather-series-wind-speed-variability-signals`
**Family:** `macro_input_pressure`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Sudden increases in wind speed variability forecast higher wind energy generation, benefiting utilities with renewable portfolios. More wind energy generation reduces costs and boosts renewable utility earnings.

## Universe
- XLU

## Data Sources
- Open-Meteo daily weather wind speed data

## Signal Logic
If daily wind speed variance exceeds 120% of 10-day rolling average

## Entry / Exit
Entry: If daily wind speed variance exceeds 120% of 10-day rolling average Exit: After 5 trading days or when variance drops below 110% of average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Open-Meteo daily weather wind speed data via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Wind speed variability fluctuates daily due to weather patterns.

## Required Keys
- None
