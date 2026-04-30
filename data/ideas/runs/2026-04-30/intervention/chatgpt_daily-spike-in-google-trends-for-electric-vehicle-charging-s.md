# Daily Spike In Google Trends For Electric Vehicle Charging Station Outage Signals Bearish Xlc

**Idea ID:** `daily-spike-in-google-trends-for-electric-vehicle-charging-s`
**Family:** `local_economy_weirdness`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Spikes in EV charging outage searches indicate infrastructure issues pressuring EV-related consumer tech sectors. Charging outages reduce EV attractiveness and dampen tech consumer sentiment.

## Universe
- XLC

## Data Sources
- Google Trends daily searches

## Signal Logic
Enter short XLC if daily search interest for 'electric vehicle charging station outage' rises 40%+ vs 10-day average

## Entry / Exit
Entry: Enter short XLC if daily search interest for 'electric vehicle charging station outage' rises 40%+ vs 10-day average Exit: Exit after 7 trading days or when interest normalizes

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends daily searches via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: EV infrastructure outages cause frequent localized search spikes.

## Required Keys
- None
