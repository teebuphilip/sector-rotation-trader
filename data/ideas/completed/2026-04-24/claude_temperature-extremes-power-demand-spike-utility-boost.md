# Temperature Extremes Power Demand Spike Utility Boost

**Idea ID:** `temperature-extremes-power-demand-spike-utility-boost`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Daily high temperatures exceed 95°F or fall below 0°F for 3+ consecutive days in major population centers, spiking HVAC load and electricity demand. Extreme weather drives peak demand periods and higher utility margins.

## Universe
- XLU

## Data Sources
- Open-Meteo daily temperatures (highs/lows) for major US metro areas via weather_series adapter

## Signal Logic
If 3+ consecutive days of extreme temps (>95F or <0F) in cities covering >50M people, long XLU

## Entry / Exit
Entry: If 3+ consecutive days of extreme temps (>95F or <0F) in cities covering >50M people, long XLU Exit: Exit after 7 trading days or when temperatures return to normal range

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Open-Meteo daily temperatures (highs/lows) for major US metro areas via weather_series adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Temperature extremes occur throughout the year (summer heat and winter cold waves); multi-day stretches trigger 5–8 times annually.

## Required Keys
- None
