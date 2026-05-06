# Daily Spike In Google Trends Searches For Airline Flight Delay Compensation

**Idea ID:** `daily-spike-in-google-trends-searches-for-airline-flight-del`
**Family:** `travel_mobility`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Rising interest in flight delay compensation signals increased travel disruptions and passenger dissatisfaction. Consumer discretionary airline stocks suffer from travel disruptions and negative sentiment.

## Universe
- XLY

## Data Sources
- Google Trends daily search interest

## Signal Logic
If daily searches for 'flight delay compensation' rise more than 25% relative to 7-day average

## Entry / Exit
Entry: If daily searches for 'flight delay compensation' rise more than 25% relative to 7-day average Exit: After 5 trading days or when search volume falls below 10% growth

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
- Why It Should Fire Soon: Airline travel disruptions happen frequently and cause search spikes.

## Required Keys
- None
