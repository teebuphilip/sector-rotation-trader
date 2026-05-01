# Weekly Google Trends Surge In Electric Vehicle Charging Station Malfunction Signals Short-term Pressure On Clean Energy Sector

**Idea ID:** `weekly-google-trends-surge-in-electric-vehicle-charging-stat`
**Family:** `local_economy_weirdness`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising searches for EV charging station issues highlight infrastructure problems that may temporarily stall EV adoption momentum. Negative EV infrastructure news pressures clean energy-related equities.

## Universe
- XLE

## Data Sources
- Google Trends weekly search interest

## Signal Logic
Enter short XLE when weekly search volume for 'EV charging station malfunction' rises 35% above 10-week average

## Entry / Exit
Entry: Enter short XLE when weekly search volume for 'EV charging station malfunction' rises 35% above 10-week average Exit: Exit after 4 weeks or if volume declines below 10-week average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: EV infrastructure issues frequently appear in weekly news cycles.

## Required Keys
- None
