# Weekly Surge In Google Trends Searches For Small Business Layoff Signals Labor Market Weakness And Discretionary Caution

**Idea ID:** `weekly-surge-in-google-trends-searches-for-small-business-la`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Increased layoff searches at small businesses often indicate early labor market softness. Discretionary spending weakens as small business layoffs rise, reducing consumer income.

## Universe
- XLY

## Data Sources
- Google Trends weekly search interest for 'small business layoff' via google_trends adapter

## Signal Logic
If weekly search volume rises more than 12% week-over-week

## Entry / Exit
Entry: If weekly search volume rises more than 12% week-over-week Exit: When weekly change falls below 5%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'small business layoff' via google_trends adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Small business layoffs fluctuate with economic cycles, causing weekly search interest shifts.

## Required Keys
- None
