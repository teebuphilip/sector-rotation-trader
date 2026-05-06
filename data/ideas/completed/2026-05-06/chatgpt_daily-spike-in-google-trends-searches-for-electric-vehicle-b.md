# Daily Spike In Google Trends Searches For Electric Vehicle Battery Replacement

**Idea ID:** `daily-spike-in-google-trends-searches-for-electric-vehicle-b`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
A sudden daily jump in EV battery replacement searches indicates rising repair costs or aging EV fleet stress. Consumer discretionary could be pressured by increased EV maintenance costs.

## Universe
- XLY

## Data Sources
- Google Trends daily search interest

## Signal Logic
If daily searches for 'EV battery replacement' spike over 20% versus 7-day rolling average

## Entry / Exit
Entry: If daily searches for 'EV battery replacement' spike over 20% versus 7-day rolling average Exit: After 7 trading days or when searches normalize

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
- Why It Should Fire Soon: EV battery issues and repair interest periodically spike due to aging vehicles and news cycles.

## Required Keys
- None
