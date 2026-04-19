# Weather Windfall

**Idea ID:** `weather-windfall`
**Source:** anthropic / claude-3-haiku-20240307
**Frequency:** daily

## Thesis
Deviations from normal weather patterns can impact various industries and sectors. Weather can drive energy consumption and production levels.

## Universe
- XLE

## Data Sources
- Open-Meteo daily temperature, precipitation, and wind speed data through weather_series adapter

## Signal Logic
If the daily average temperature, precipitation, or wind speed deviates more than 2 standard deviations from the prior 30-day average

## Entry / Exit
Entry: If the daily average temperature, precipitation, or wind speed deviates more than 2 standard deviations from the prior 30-day average Exit: After 3 trading days or once the weather metric returns to within 1 standard deviation of the prior 30-day average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Open-Meteo daily temperature, precipitation, and wind speed data through weather_series adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Weather data exhibits regular daily and weekly patterns, and deviations from typical ranges often occur.

## Required Keys
- None
