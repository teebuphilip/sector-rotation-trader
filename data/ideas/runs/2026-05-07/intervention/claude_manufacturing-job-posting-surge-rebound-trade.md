# Manufacturing Job Posting Surge Rebound Trade

**Idea ID:** `manufacturing-job-posting-surge-rebound-trade`
**Family:** `labor_jobs`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When manufacturing job postings spike 25%+ week-over-week, it signals capital equipment orders and production ramp expectations 4-6 weeks ahead. Manufacturing hiring surges precede earnings beats and capex announcements in industrial and materials sectors.

## Universe
- XLI

## Data Sources
- Indeed.com job posting counts via html_table scrape, manufacturing category weekly

## Signal Logic
When weekly manufacturing job postings exceed prior week by 25% or more

## Entry / Exit
Entry: When weekly manufacturing job postings exceed prior week by 25% or more Exit: After 15 trading days or when postings drop 15% week-over-week

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Indeed.com job posting counts via html_table scrape, manufacturing category weekly via scrape (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Manufacturing job posting volatility is seasonal; 3-4 spikes per year as factories ramp for demand cycles.

## Required Keys
- None
