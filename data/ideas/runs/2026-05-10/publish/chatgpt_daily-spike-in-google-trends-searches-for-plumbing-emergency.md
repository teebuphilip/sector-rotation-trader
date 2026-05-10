# Daily Spike In Google Trends Searches For Plumbing Emergency Signals Consumer Stress Benefiting Industrial Sector

**Idea ID:** `daily-spike-in-google-trends-searches-for-plumbing-emergency`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Spikes in plumbing emergency searches indicate consumer stress and increased demand for home repair services. Industrial sector including building materials and services often benefits from home repair demand.

## Universe
- XLI

## Data Sources
- Google Trends daily search interest for 'plumbing emergency' via google_trends adapter

## Signal Logic
If daily search volume exceeds 12% above 20-day average

## Entry / Exit
Entry: If daily search volume exceeds 12% above 20-day average Exit: When daily volume falls below 5% above 20-day average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends daily search interest for 'plumbing emergency' via google_trends adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Home repair emergencies are common and cause frequent search spikes.

## Required Keys
- None
