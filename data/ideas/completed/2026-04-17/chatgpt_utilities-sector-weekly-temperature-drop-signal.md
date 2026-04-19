# Utilities Sector Weekly Temperature Drop Signal

**Idea ID:** `utilities-sector-weekly-temperature-drop-signal`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
A steep weekly temperature decline often drives higher utility demand, boosting utility stock performance. Colder weather increases heating demand, benefiting utilities.

## Universe
- XLU

## Data Sources
- Open-Meteo daily temperature for US regions weighted to XLU holdings

## Signal Logic
If average weekly temperature drops >5°F compared to prior week

## Entry / Exit
Entry: If average weekly temperature drops >5°F compared to prior week Exit: After 2 weeks or 3% price gain

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Open-Meteo daily temperature for US regions weighted to XLU holdings via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 36
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Weather fluctuations causing demand shifts occur regularly through seasons.

## Required Keys
- None
