# Daily Spike In Local Weather Heatwave Signals Bullish Utilities

**Idea ID:** `daily-spike-in-local-weather-heatwave-signals-bullish-utilit`
**Family:** `local_economy_weirdness`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Sudden heatwaves increase electricity demand for cooling, boosting utility sector revenues. Heat spikes drive higher power consumption and utility billing.

## Universe
- XLU

## Data Sources
- Open-Meteo daily temperature data

## Signal Logic
Enter long on XLU if daily max temperature exceeds 95°F and is 10°F above 7-day average

## Entry / Exit
Entry: Enter long on XLU if daily max temperature exceeds 95°F and is 10°F above 7-day average Exit: Exit after 5 trading days or if temperatures normalize

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Open-Meteo daily temperature data via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Heatwaves are seasonal and frequently occur with sudden spikes.

## Required Keys
- None
