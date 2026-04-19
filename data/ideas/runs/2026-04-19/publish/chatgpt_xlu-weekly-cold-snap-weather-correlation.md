# Xlu Weekly Cold Snap Weather Correlation

**Idea ID:** `xlu-weekly-cold-snap-weather-correlation`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Significant weekly temperature drops often increase utility demand, lifting XLU prices. Utilities benefit from cold weather-driven energy consumption spikes.

## Universe
- XLU

## Data Sources
- Open-Meteo daily temperature data aggregated weekly for US Northeast

## Signal Logic
Enter long if weekly average temperature falls by more than 5°F compared to prior week

## Entry / Exit
Entry: Enter long if weekly average temperature falls by more than 5°F compared to prior week Exit: Exit after 2 weeks or if temperature stabilizes

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Open-Meteo daily temperature data aggregated weekly for US Northeast via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Cold snaps in the Northeast recur each season, providing timely signals.

## Required Keys
- None
