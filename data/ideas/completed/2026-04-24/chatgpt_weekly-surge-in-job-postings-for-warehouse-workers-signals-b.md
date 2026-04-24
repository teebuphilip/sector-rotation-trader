# Weekly Surge In Job Postings For Warehouse Workers Signals Bullish Xli

**Idea ID:** `weekly-surge-in-job-postings-for-warehouse-workers-signals-b`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Growing demand for warehouse labor indicates rising industrial activity and goods movement. Increased warehouse hiring presages stronger industrial output and logistics activity.

## Universe
- XLI

## Data Sources
- RSS news feed counts

## Signal Logic
If weekly job postings for 'warehouse worker' exceed 1.5x 8-week average

## Entry / Exit
Entry: If weekly job postings for 'warehouse worker' exceed 1.5x 8-week average Exit: Exit after 3 weeks or if postings drop below 1.1x average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS news feed counts via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 14
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Warehouse labor demand fluctuates seasonally and with supply chain demands, triggering multiple weekly surges.

## Required Keys
- None
