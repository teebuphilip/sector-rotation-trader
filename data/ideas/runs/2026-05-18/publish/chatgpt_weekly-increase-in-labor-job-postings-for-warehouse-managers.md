# Weekly Increase In Labor Job Postings For Warehouse Managers Signals Industrial Sector Strength

**Idea ID:** `weekly-increase-in-labor-job-postings-for-warehouse-managers`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising warehouse manager postings suggest expanding logistics and industrial operations. Warehouse expansion indicates higher industrial throughput and demand.

## Universe
- XLI

## Data Sources
- Scraped labor job postings for 'warehouse manager' roles

## Signal Logic
If weekly postings rise by over 15% vs prior 6-week average

## Entry / Exit
Entry: If weekly postings rise by over 15% vs prior 6-week average Exit: Exit after 6 weeks or when postings decline by 10% from peak

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Scraped labor job postings for 'warehouse manager' roles via scrape (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Warehouse hiring fluctuates with inventory cycles and seasonal demand.

## Required Keys
- None
