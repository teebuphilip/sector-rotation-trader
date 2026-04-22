# Weekly Surge In Google Trends Search For Job Quitting Signals Labor Market Stress

**Idea ID:** `weekly-surge-in-google-trends-search-for-job-quitting-signal`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
A sudden rise in searches for quitting jobs suggests rising labor market stress and potential wage inflation. Consumer discretionary stocks face margin pressure from rising labor costs.

## Universe
- XLY

## Data Sources
- Google Trends weekly search interest for 'job quitting'

## Signal Logic
If weekly search interest increases by 20% week-over-week

## Entry / Exit
Entry: If weekly search interest increases by 20% week-over-week Exit: After 3 weeks or if interest declines by 10% week-over-week

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'job quitting' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Labor unrest and quitting are common and often spike seasonally or with economic changes.

## Required Keys
- None
