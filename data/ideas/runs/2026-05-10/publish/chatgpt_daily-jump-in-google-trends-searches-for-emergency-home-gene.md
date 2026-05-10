# Daily Jump In Google Trends Searches For Emergency Home Generator Repair Signals Consumer Stress Benefiting Staples Sector

**Idea ID:** `daily-jump-in-google-trends-searches-for-emergency-home-gene`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Spike in emergency generator repair searches during power outages signals consumer stress and demand for essentials. Consumer staples often benefit when essential home services and repairs surge.

## Universe
- XLP

## Data Sources
- Google Trends daily search interest for 'emergency home generator repair' via google_trends adapter

## Signal Logic
If daily search volume spikes 15% above 30-day average

## Entry / Exit
Entry: If daily search volume spikes 15% above 30-day average Exit: Once search volume falls below 5% above 30-day average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends daily search interest for 'emergency home generator repair' via google_trends adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Power outage-related search spikes occur frequently in varying weather conditions.

## Required Keys
- None
