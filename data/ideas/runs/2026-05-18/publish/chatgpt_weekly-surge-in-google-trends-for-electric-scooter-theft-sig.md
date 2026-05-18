# Weekly Surge In Google Trends For Electric Scooter Theft Signals Consumer Discretionary Stress

**Idea ID:** `weekly-surge-in-google-trends-for-electric-scooter-theft-sig`
**Family:** `local_economy_weirdness`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising theft-related searches imply increased consumer mobility gear stress or urban crime impact on discretionary spending. Discretionary spending may slow due to increased theft risk and replacement costs.

## Universe
- XLY

## Data Sources
- Google Trends weekly search interest for 'electric scooter theft'

## Signal Logic
If weekly searches increase by more than 25% over prior 5-week average

## Entry / Exit
Entry: If weekly searches increase by more than 25% over prior 5-week average Exit: Exit after 3 weeks or when search interest drops below 10% increase

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'electric scooter theft' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 15
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Urban theft concerns fluctuate with season and local economic conditions.

## Required Keys
- None
