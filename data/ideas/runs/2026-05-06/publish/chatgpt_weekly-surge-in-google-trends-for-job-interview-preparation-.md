# Weekly Surge In Google Trends For Job Interview Preparation Searches

**Idea ID:** `weekly-surge-in-google-trends-for-job-interview-preparation-`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
A notable increase in job interview preparation searches signals rising job market anxiety or new job seekers entering the market, often preceding increased hiring activity. Consumer discretionary benefits from increased employment and confidence in job market growth.

## Universe
- XLY

## Data Sources
- Google Trends weekly search interest

## Signal Logic
If weekly Google Trends interest for 'job interview preparation' rises by more than 15% week-over-week

## Entry / Exit
Entry: If weekly Google Trends interest for 'job interview preparation' rises by more than 15% week-over-week Exit: After 4 weeks or when the trend drops below 5% week-over-week growth

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
- Why It Should Fire Soon: Labor market interest fluctuations frequently occur with monthly hiring cycles and seasonal job search trends.

## Required Keys
- None
