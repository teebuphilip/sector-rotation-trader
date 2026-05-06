# Weekly Google Trends Surge In Searches For Truck Driver Shortage

**Idea ID:** `weekly-google-trends-surge-in-searches-for-truck-driver-shor`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
A surge in searches for truck driver shortage highlights labor supply constraints in freight logistics impacting delivery timelines. Industrial sector under pressure due to labor shortages affecting shipping and production.

## Universe
- XLI

## Data Sources
- Google Trends weekly search interest

## Signal Logic
If weekly searches for 'truck driver shortage' increase over 20% week-over-week

## Entry / Exit
Entry: If weekly searches for 'truck driver shortage' increase over 20% week-over-week Exit: After 3 weeks or when growth subsides below 8%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Labor shortages in trucking are persistent and show cyclical interest spikes.

## Required Keys
- None
