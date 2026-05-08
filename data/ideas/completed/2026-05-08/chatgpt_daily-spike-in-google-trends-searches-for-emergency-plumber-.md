# Daily Spike In Google Trends Searches For Emergency Plumber Signals Consumer Home Repair Stress

**Idea ID:** `daily-spike-in-google-trends-searches-for-emergency-plumber-`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Sudden rise in emergency plumbing searches points to acute household repair needs raising discretionary spending. Home repair demand boosts discretionary retail and services related to household maintenance.

## Universe
- XLY

## Data Sources
- Google Trends daily search interest

## Signal Logic
If daily searches exceed prior 7-day average by 30%

## Entry / Exit
Entry: If daily searches exceed prior 7-day average by 30% Exit: When daily searches drop below 10% above 7-day average

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
- Why It Should Fire Soon: Home repair urgencies frequently spike with weather changes or infrastructure aging.

## Required Keys
- None
