# Daily Spike In Google Trends For Emergency Dental Surgery Signals Healthcare Consumer Stress

**Idea ID:** `daily-spike-in-google-trends-for-emergency-dental-surgery-si`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Rising urgent dental surgery searches indicate heightened healthcare stress and demand. Healthcare sector demand often rises with urgent consumer health issues.

## Universe
- XLV

## Data Sources
- Google Trends daily search interest for 'emergency dental surgery'

## Signal Logic
If daily search interest increases by 30% over prior 7-day average

## Entry / Exit
Entry: If daily search interest increases by 30% over prior 7-day average Exit: Exit after 7 days or when interest falls below 15% increase

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends daily search interest for 'emergency dental surgery' via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Dental emergencies are common and news/social signals often spike.

## Required Keys
- None
