# Weather Disruption Ripple Effects

**Idea ID:** `weather-disruption-ripple-effects`
**Source:** anthropic / claude-3-haiku-20240307
**Frequency:** daily

## Thesis
Extreme weather events can disrupt supply chains, energy production, and transportation, creating volatility across multiple sectors. Energy sector benefits from increased demand and infrastructure investment during weather disruptions.

## Universe
- XLE

## Data Sources
- Daily weather data from Open-Meteo through weather_series adapter

## Signal Logic
If the daily maximum wind speed at a major transportation hub exceeds 40 mph or the daily maximum temperature deviates more than 10 degrees from normal

## Entry / Exit
Entry: If the daily maximum wind speed at a major transportation hub exceeds 40 mph or the daily maximum temperature deviates more than 10 degrees from normal Exit: After 7 trading days or when weather conditions return to normal

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Daily weather data from Open-Meteo through weather_series adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Extreme weather events are common occurrences that frequently impact economic activity and market conditions.

## Required Keys
- None
