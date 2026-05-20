# Daily Surge In Google Trends For Electric Vehicle Charging Station Outage Signals Green Tech Stress

**Idea ID:** `daily-surge-in-google-trends-for-electric-vehicle-charging-s`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Spikes in EV charger outage searches indicate infrastructure issues creating stress in green tech adoption. Charging infrastructure problems can slow electric vehicle adoption impacting clean tech sectors.

## Universe
- XLC

## Data Sources
- Google Trends daily search interest

## Signal Logic
If daily Google Trends for 'electric vehicle charging station outage' rises 60% vs 7-day average

## Entry / Exit
Entry: If daily Google Trends for 'electric vehicle charging station outage' rises 60% vs 7-day average Exit: After 5 trading days or if trend falls below 25% above baseline

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends daily search interest via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Infrastructure outages and EV charger issues appear frequently in news and consumer searches.

## Required Keys
- None
