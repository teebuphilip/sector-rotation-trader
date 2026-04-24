# Weekly Surge In Google Trends Searches For Home Improvement Loan Signals Consumer Stress Lifting Xly

**Idea ID:** `weekly-surge-in-google-trends-searches-for-home-improvement-`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising interest in home improvement loans often signals increased consumer willingness to spend on discretionary housing-related retail items. Increased loan interest suggests consumer confidence in discretionary home-related spending.

## Universe
- XLY

## Data Sources
- Google Trends weekly search interest

## Signal Logic
If weekly search volume for 'home improvement loan' rises by more than 15% week-over-week

## Entry / Exit
Entry: If weekly search volume for 'home improvement loan' rises by more than 15% week-over-week Exit: Exit after 3 weeks or if search volume declines for 2 consecutive weeks

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
- Why It Should Fire Soon: Google Trends weekly data frequently shows >15% spikes in consumer loan interest seasonally and with credit cycles.

## Required Keys
- None
