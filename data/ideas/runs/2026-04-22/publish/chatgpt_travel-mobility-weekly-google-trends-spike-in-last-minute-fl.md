# Travel Mobility Weekly Google Trends Spike In Last Minute Flights Searches

**Idea ID:** `travel-mobility-weekly-google-trends-spike-in-last-minute-fl`
**Family:** `travel_mobility`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Spike in last minute flight searches signals near-term surge in travel bookings, bullish for travel sector. Increased last-minute travel interest often precedes upward travel spending and discretionary sector strength.

## Universe
- XLY

## Data Sources
- Google Trends weekly search interest for 'last minute flights'

## Signal Logic
Enter long XLY if last minute flight searches increase >25% WoW for 2 weeks

## Entry / Exit
Entry: Enter long XLY if last minute flight searches increase >25% WoW for 2 weeks Exit: Exit after searches drop below 10% WoW increase or after 5 weeks

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'last minute flights' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Travel interest surges seasonally and due to event-driven travel needs are common.

## Required Keys
- None
