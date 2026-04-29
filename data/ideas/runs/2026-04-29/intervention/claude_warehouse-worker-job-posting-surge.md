# Warehouse Worker Job Posting Surge

**Idea ID:** `warehouse-worker-job-posting-surge`
**Family:** `labor_jobs`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Sudden spikes in warehouse job postings signal supply chain operators are ramping hiring ahead of expected demand; this precedes retail sales strength by 3-6 weeks. Warehouse hiring surge indicates businesses expect strong consumer demand in coming weeks.

## Universe
- XLY

## Data Sources
- Indeed.com job posting weekly counts for 'warehouse worker' via html_table scrape adapter

## Signal Logic
If weekly warehouse worker postings spike 40%+ above 8-week rolling average

## Entry / Exit
Entry: If weekly warehouse worker postings spike 40%+ above 8-week rolling average Exit: After 5 weeks or when postings revert to mean

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Indeed.com job posting weekly counts for 'warehouse worker' via html_table scrape adapter via scrape (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Warehouse hiring surges occur ahead of peak seasons (holiday, summer) and demand shocks; typically 2-3 spikes per year, each lasting 4-6 weeks.

## Required Keys
- None
