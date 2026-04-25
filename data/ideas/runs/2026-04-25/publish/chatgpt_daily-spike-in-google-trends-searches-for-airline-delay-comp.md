# Daily Spike In Google Trends Searches For Airline Delay Compensation Signals Bearish Xly

**Idea ID:** `daily-spike-in-google-trends-searches-for-airline-delay-comp`
**Family:** `travel_mobility`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Increased consumer searches for delay compensation indicate rising travel disruption and dissatisfaction. Consumer travel disappointment suggests airline revenue and service issues.

## Universe
- XLY

## Data Sources
- Google Trends daily search interest for 'airline delay compensation'

## Signal Logic
Enter short XLY when daily search volume spikes 25% above 7-day average

## Entry / Exit
Entry: Enter short XLY when daily search volume spikes 25% above 7-day average Exit: Exit after 7 days or when search volume normalizes

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends daily search interest for 'airline delay compensation' via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Travel disruptions and compensation claims surge frequently due to weather and operational issues.

## Required Keys
- None
