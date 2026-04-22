# Weekly Spike In Laborjobs Job Postings For Warehouse Roles Predicts Industrial Strength

**Idea ID:** `weekly-spike-in-laborjobs-job-postings-for-warehouse-roles-p`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Increasing warehouse job postings reflect rising demand for logistics capacity supporting industrial activity. Industrial sector benefits from expanding warehouse and logistics employment.

## Universe
- XLI

## Data Sources
- Labor job postings for warehouse roles from labor_jobs adapter

## Signal Logic
Entry when warehouse job postings increase by more than 10% over prior 2 weeks

## Entry / Exit
Entry: Entry when warehouse job postings increase by more than 10% over prior 2 weeks Exit: Exit when postings decline 5% or after 6 weeks

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Labor job postings for warehouse roles from labor_jobs adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Warehouse job postings fluctuate weekly with logistics demand cycles.

## Required Keys
- None
