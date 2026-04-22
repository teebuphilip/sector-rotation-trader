# Weekly Increase In Google Trends Searches For Job Hiring Bonus Indicating Labor Tightness

**Idea ID:** `weekly-increase-in-google-trends-searches-for-job-hiring-bon`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising searches for hiring bonuses signal labor shortages and rising recruitment costs. Higher labor costs pressure consumer discretionary margins.

## Universe
- XLY

## Data Sources
- Google Trends weekly search interest for 'job hiring bonus'

## Signal Logic
If weekly search interest rises 20% week-over-week

## Entry / Exit
Entry: If weekly search interest rises 20% week-over-week Exit: After 4 weeks or interest falls below 10% gain

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'job hiring bonus' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Labor tightness and related searches are frequent and seasonal.

## Required Keys
- None
