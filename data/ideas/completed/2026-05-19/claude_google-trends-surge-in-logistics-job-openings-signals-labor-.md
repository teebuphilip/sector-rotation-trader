# Google Trends Surge In Logistics Job Openings Signals Labor Shortage In Freight

**Idea ID:** `google-trends-surge-in-logistics-job-openings-signals-labor-`
**Family:** `labor_jobs`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Weekly spikes in job search interest for logistics roles correlate with labor shortages and wage inflation pressure; signals upcoming freight cost increases. Labor shortage signals compress margins for transportation and warehousing-dependent industrials.

## Universe
- XLI

## Data Sources
- Google Trends weekly search volume for 'warehouse job' OR 'truck driver jobs' through google_trends adapter

## Signal Logic
When weekly search volume exceeds 75th percentile of 52-week range for logistics job keywords

## Entry / Exit
Entry: When weekly search volume exceeds 75th percentile of 52-week range for logistics job keywords Exit: When search volume falls below 60th percentile for 2 consecutive weeks or after 14 days

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search volume for 'warehouse job' OR 'truck driver jobs' through google_trends adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Seasonal labor demand in logistics peaks predictably; search spikes occur weekly during peak hiring seasons (Q4, spring).

## Required Keys
- None
