# Weekly Decline In Laborjobs Google Trends Searches For Temporary Staffing Signals Bearish Xlf

**Idea ID:** `weekly-decline-in-laborjobs-google-trends-searches-for-tempo`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Falling interest in temporary staffing signals labor market slowdown, pressuring financial stocks sensitive to credit risk. Weaker labor demand increases default risk and reduces financial sector optimism.

## Universe
- XLF

## Data Sources
- Google Trends weekly search interest for 'temporary staffing'

## Signal Logic
If weekly search interest declines more than 15% week-over-week

## Entry / Exit
Entry: If weekly search interest declines more than 15% week-over-week Exit: After 4 weeks or if interest recovers above baseline

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'temporary staffing' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Labor market interest fluctuates with economic cycles and hiring trends.

## Required Keys
- None
