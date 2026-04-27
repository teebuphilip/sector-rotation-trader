# Regional Extreme Weather Google Trend Spike Insurance Play

**Idea ID:** `regional-extreme-weather-google-trend-spike-insurance-play`
**Family:** `local_economy_weirdness`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Spikes in weather-related Google searches combined with actual extreme weather data signal consumer anxiety and property damage claims, driving insurance underwriting margins. Severe weather increases insurance claims and premiums; financial sector (especially insurers) benefits from claim inflation and repricing.

## Universe
- XLF

## Data Sources
- Google Trends weekly searches for 'flooding', 'hurricane prep', 'power outage' + Open-Meteo daily extreme weather events

## Signal Logic
If Google Trends weekly search interest for weather disaster keywords exceeds prior 52-week median by 50% AND Open-Meteo detects severe weather in 3+ US states, go long XLF.

## Entry / Exit
Entry: If Google Trends weekly search interest for weather disaster keywords exceeds prior 52-week median by 50% AND Open-Meteo detects severe weather in 3+ US states, go long XLF. Exit: After 8 trading days or if search interest normalizes.

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly searches for 'flooding', 'hurricane prep', 'power outage' + Open-Meteo daily extreme weather events via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Extreme weather events and searches spike seasonally; multiple triggers fire monthly across US regions.

## Required Keys
- None
