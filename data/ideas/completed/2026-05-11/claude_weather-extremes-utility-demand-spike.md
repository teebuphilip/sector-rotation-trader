# Weather Extremes Utility Demand Spike

**Idea ID:** `weather-extremes-utility-demand-spike`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When 10+ major metros log temperatures >95F or <5F for 3+ consecutive days, heating/cooling demand surges, driving utility revenue and grid pressure signals. Extreme temperatures increase electricity and natural gas demand, boosting regulated utility earnings and pricing power.

## Universe
- XLU

## Data Sources
- Open-Meteo daily temperature and wind speed for 50 US cities via weather_series adapter

## Signal Logic
If 10+ metros hit temperature extreme (>95F or <5F) for 3+ consecutive days

## Entry / Exit
Entry: If 10+ metros hit temperature extreme (>95F or <5F) for 3+ consecutive days Exit: After 12 trading days or when temps normalize for 2+ days

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Open-Meteo daily temperature and wind speed for 50 US cities via weather_series adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Seasonal extremes are predictable; this fires 2-3x per quarter in summer and winter across US regions.

## Required Keys
- None
