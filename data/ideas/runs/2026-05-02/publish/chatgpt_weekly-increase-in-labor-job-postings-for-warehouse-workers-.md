# Weekly Increase In Labor Job Postings For Warehouse Workers Signals Freight Logistics Sector Momentum

**Idea ID:** `weekly-increase-in-labor-job-postings-for-warehouse-workers-`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising warehouse job postings reflect growing demand in freight logistics and supply chain activity. Higher warehouse labor demand indicates stronger freight and logistics activity supporting industrial growth.

## Universe
- XLI

## Data Sources
- Indeed job postings weekly counts

## Signal Logic
If warehouse job postings rise 10% week-over-week

## Entry / Exit
Entry: If warehouse job postings rise 10% week-over-week Exit: After 3 weeks or if postings decline 5% week-over-week

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Indeed job postings weekly counts via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Warehouse labor demand fluctuates frequently with supply chain cycles and inventory restocking.

## Required Keys
- None
