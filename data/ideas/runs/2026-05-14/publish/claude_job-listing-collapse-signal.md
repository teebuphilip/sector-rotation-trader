# Job Listing Collapse Signal

**Idea ID:** `job-listing-collapse-signal`
**Family:** `labor_jobs`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Sharp declines in job listings signal employer caution and weakening hiring demand, foreshadowing consumer spending pressure. Falling hiring signals reduced wage growth and employment security; consumer discretionary spending contracts as job anxiety rises.

## Universe
- XLY

## Data Sources
- Indeed or LinkedIn job posting volume (weekly via RSS feed or HTML table scrape of publicly available aggregate counts)

## Signal Logic
If weekly job listing count drops >15% below 8-week moving average

## Entry / Exit
Entry: If weekly job listing count drops >15% below 8-week moving average Exit: After 18 trading days or when listings rebound 10% above entry level

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Indeed or LinkedIn job posting volume (weekly via RSS feed or HTML table scrape of publicly available aggregate counts) via scrape (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 16
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Labor market sentiment shifts drive hiring cycles; seasonal slowdowns (post-holiday, summer lull) produce regular dips in job postings.

## Required Keys
- None
