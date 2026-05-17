# Open-metoe Heavy Rain Forecast Triggers Agricultural Commodity Bounce

**Idea ID:** `open-metoe-heavy-rain-forecast-triggers-agricultural-commodi`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When forecasts shift to heavy rain (>1.5 inches predicted within 7 days) in the Corn Belt, crop stress eases and commodity prices rebound on favorable moisture outlook. Agricultural commodity prices rise on improved crop conditions; materials and mining stocks often co-move with commodity sentiment.

## Universe
- XLB

## Data Sources
- Open-Meteo weather API 14-day precipitation forecast for US Corn Belt (centroid: Iowa)

## Signal Logic
Open-Meteo forecast updates to >1.5 inches rain within 7 days AND agricultural commodity ETFs (DBC, AGF) rise >1.2% same day

## Entry / Exit
Entry: Open-Meteo forecast updates to >1.5 inches rain within 7 days AND agricultural commodity ETFs (DBC, AGF) rise >1.2% same day Exit: Agricultural ETF closes down >0.5% from entry or 8 calendar days elapse

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Open-Meteo weather API 14-day precipitation forecast for US Corn Belt (centroid: Iowa) via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Weather forecasts update daily; rain forecast swings occur 2–3 times per month during growing season.

## Required Keys
- None
