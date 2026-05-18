# Daily Jump In Google Trends For Emergency Hvac Repair Signals Consumer Home Repair Stress

**Idea ID:** `daily-jump-in-google-trends-for-emergency-hvac-repair-signal`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Spikes in emergency HVAC repair searches indicate urgent consumer home repair needs impacting discretionary spending. Home repair demand benefits consumer discretionary sector companies.

## Universe
- XLY

## Data Sources
- Google Trends daily search interest for 'emergency HVAC repair'

## Signal Logic
If daily searches increase by over 30% vs prior 7-day average

## Entry / Exit
Entry: If daily searches increase by over 30% vs prior 7-day average Exit: Exit after 7 trading days or when searches fall below 15% increase

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends daily search interest for 'emergency HVAC repair' via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: HVAC failures occur seasonally and cause immediate consumer concern.

## Required Keys
- None
