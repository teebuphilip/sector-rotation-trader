# Weekly Surge In Google Trends For Car Rental Pickup Delays Signals Travel Disruption

**Idea ID:** `weekly-surge-in-google-trends-for-car-rental-pickup-delays-s`
**Family:** `travel_mobility`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
A sudden rise in searches related to car rental pickup delays indicates travel disruption and potential consumer frustration. Travel disruption tends to reduce discretionary travel spending impacting consumer discretionary sector ETFs.

## Universe
- XLY

## Data Sources
- Google Trends weekly car rental pickup delay searches

## Signal Logic
Entry when weekly Google Trends car rental delay search index rises 20% above 4-week average

## Entry / Exit
Entry: Entry when weekly Google Trends car rental delay search index rises 20% above 4-week average Exit: Exit when index returns within 5% of 4-week average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly car rental pickup delay searches via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Travel disruptions and rental delays frequently spike seasonally or due to weather/events.

## Required Keys
- None
