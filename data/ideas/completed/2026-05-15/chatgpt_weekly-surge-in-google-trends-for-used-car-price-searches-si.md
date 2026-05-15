# Weekly Surge In Google Trends For Used Car Price Searches Signaling Consumer Cost Pressure

**Idea ID:** `weekly-surge-in-google-trends-for-used-car-price-searches-si`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising interest in used car prices reflects consumer cost pressures and substitution away from new vehicles. Discretionary auto spending often slows when consumer stress pushes toward used cars.

## Universe
- XLY

## Data Sources
- Google Trends weekly search interest for used car prices

## Signal Logic
If weekly search volume rises 20% above 6-week average

## Entry / Exit
Entry: If weekly search volume rises 20% above 6-week average Exit: When volume falls below 5% above average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for used car prices via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Used car price interest fluctuates regularly with market conditions and news.

## Required Keys
- None
