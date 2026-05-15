# Daily Spike In Google Trends For Emergency Roadside Assistance Searches Signals Consumer Stress

**Idea ID:** `daily-spike-in-google-trends-for-emergency-roadside-assistan`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Sudden increases in searches for roadside help show rising consumer vehicle distress, impacting discretionary spending. Consumer discretionary purchases often decline when vehicle repair stress spikes.

## Universe
- XLY

## Data Sources
- Google Trends daily search interest for emergency roadside assistance

## Signal Logic
If daily search volume jumps 25% above prior 7-day average

## Entry / Exit
Entry: If daily search volume jumps 25% above prior 7-day average Exit: When volume declines below 10% above baseline

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends daily search interest for emergency roadside assistance via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Vehicle emergencies and breakdowns cause frequent short-term spikes in searches.

## Required Keys
- None
