# Consumer Staples Sector Weekly Weather Temperature Spike

**Idea ID:** `consumer-staples-sector-weekly-weather-temperature-spike`
**Family:** ``
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
A 10%+ weekly increase in average temperature during colder months correlates with a short-term dip in staples due to reduced heating product demand. Warmer weather reduces demand for certain consumer staples like heating fuels and warm beverages.

## Universe
- XLP

## Data Sources
- Open-Meteo daily temperature averaged weekly for major US metro areas

## Signal Logic
Enter short XLP if weekly average temperature rises >10% compared to prior week in winter months (Nov-Feb)

## Entry / Exit
Entry: Enter short XLP if weekly average temperature rises >10% compared to prior week in winter months (Nov-Feb) Exit: Exit after 3 weeks or if XLP rallies 3%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Open-Meteo daily temperature averaged weekly for major US metro areas via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Weather fluctuations happen regularly and impact staples seasonally.

## Required Keys
- None
