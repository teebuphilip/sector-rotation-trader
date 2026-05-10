# Daily Surge In Google Trends Searches For Airline Delay Compensation Signals Travel Sector Stress

**Idea ID:** `daily-surge-in-google-trends-searches-for-airline-delay-comp`
**Family:** `travel_mobility`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Rising searches reflect growing consumer dissatisfaction and operational issues in airlines. Travel sector stocks often suffer when operational disruptions and consumer complaints rise.

## Universe
- XLY

## Data Sources
- Google Trends daily search interest for 'airline delay compensation' via google_trends adapter

## Signal Logic
If daily search volume exceeds 10% above 20-day average

## Entry / Exit
Entry: If daily search volume exceeds 10% above 20-day average Exit: Once daily volume retreats below 3% above 20-day average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends daily search interest for 'airline delay compensation' via google_trends adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Airline operational issues cause frequent daily search spikes.

## Required Keys
- None
