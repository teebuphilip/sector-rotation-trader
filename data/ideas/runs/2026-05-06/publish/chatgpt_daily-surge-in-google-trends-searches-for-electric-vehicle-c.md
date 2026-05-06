# Daily Surge In Google Trends Searches For Electric Vehicle Charging Station Outages

**Idea ID:** `daily-surge-in-google-trends-searches-for-electric-vehicle-c`
**Family:** `local_economy_weirdness`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Increased searches on EV charging outages indicate infrastructure issues affecting green energy adoption. Energy sector stocks linked to renewables may face short-term pressure from infrastructure concerns.

## Universe
- XLE

## Data Sources
- Google Trends daily search interest

## Signal Logic
If daily search volume for 'EV charging outage' spikes over 25% vs 7-day average

## Entry / Exit
Entry: If daily search volume for 'EV charging outage' spikes over 25% vs 7-day average Exit: After 5 trading days or when search volume declines

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends daily search interest via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: EV infrastructure issues are emerging and cause frequent consumer queries.

## Required Keys
- None
