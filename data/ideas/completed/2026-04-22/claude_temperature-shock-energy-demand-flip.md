# Temperature Shock Energy Demand Flip

**Idea ID:** `temperature-shock-energy-demand-flip`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When temperature deviation from 30-year normal exceeds ±2 standard deviations for 3+ consecutive days, it forces emergency energy demand swings and utility margin pressure. Utilities face volume-price mismatches during extreme weather; margin compression and regulatory backlash pressure utility sector equity returns.

## Universe
- XLU

## Data Sources
- Open-Meteo daily average temperature anomalies for US and Europe through weather_series adapter

## Signal Logic
When daily US temperature anomaly ≥2σ from historical median AND persists for ≥3 consecutive days

## Entry / Exit
Entry: When daily US temperature anomaly ≥2σ from historical median AND persists for ≥3 consecutive days Exit: After 5 trading days or when temperature normalizes to within 1σ

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Open-Meteo daily average temperature anomalies for US and Europe through weather_series adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Seasonal heat waves and cold snaps occur predictably; 2–3 extreme temperature events per month during summer/winter transitions.

## Required Keys
- None
