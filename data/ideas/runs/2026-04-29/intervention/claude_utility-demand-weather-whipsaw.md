# Utility Demand Weather Whipsaw

**Idea ID:** `utility-demand-weather-whipsaw`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Sudden swings in seasonal temperature create rapid demand shocks for electricity and natural gas, forcing utility operators to adjust generation and buying patterns within hours. Utilities rally on unexpected demand spikes that increase margin and utilization rates.

## Universe
- XLU

## Data Sources
- Open-Meteo daily temperature and heating/cooling degree days via weather_series adapter

## Signal Logic
If 7-day rolling average temperature change exceeds ±8°F from prior week and XLU volume spikes 30% above 20-day average

## Entry / Exit
Entry: If 7-day rolling average temperature change exceeds ±8°F from prior week and XLU volume spikes 30% above 20-day average Exit: After 8 trading days or when temperature stabilizes within 5°F of seasonal norm

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Open-Meteo daily temperature and heating/cooling degree days via weather_series adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Weather volatility occurs weekly in most regions; temperature swings of 8+ degrees happen multiple times per season.

## Required Keys
- None
