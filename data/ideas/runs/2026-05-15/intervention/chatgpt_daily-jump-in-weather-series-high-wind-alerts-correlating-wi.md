# Daily Jump In Weather Series High-wind Alerts Correlating With Energy Utilities Demand Spike

**Idea ID:** `daily-jump-in-weather-series-high-wind-alerts-correlating-wi`
**Family:** `macro_input_pressure`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Increased high-wind days drive energy demand for utilities and grid stability services. Utilities sector benefits from weather-driven demand surges for power and resilience.

## Universe
- XLU

## Data Sources
- Open-Meteo high wind alert data

## Signal Logic
If daily high-wind alert counts exceed 50% above 14-day average

## Entry / Exit
Entry: If daily high-wind alert counts exceed 50% above 14-day average Exit: When alert counts normalize below 10% above average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Open-Meteo high wind alert data via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Weather volatility and wind events frequently fluctuate day-to-day.

## Required Keys
- None
