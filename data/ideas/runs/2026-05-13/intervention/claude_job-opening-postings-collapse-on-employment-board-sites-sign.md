# Job Opening Postings Collapse On Employment Board Sites Signals Labor Market Cracking

**Idea ID:** `job-opening-postings-collapse-on-employment-board-sites-sign`
**Family:** `labor_jobs`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Tech and consumer-facing job postings spike and crash in advance of earnings disappointments. A 12%+ week-over-week drop in open positions signals hiring pullback and upcoming layoffs. Job posting declines precede consumer discretionary weakness as hiring freezes reduce wage growth and job security confidence.

## Universe
- XLY

## Data Sources
- Indeed, ZipRecruiter, and Glassdoor job posting counts via rss_count or html_table weekly snapshot

## Signal Logic
When aggregate weekly job postings (tech + retail + hospitality) decline 12% or more from prior week

## Entry / Exit
Entry: When aggregate weekly job postings (tech + retail + hospitality) decline 12% or more from prior week Exit: After 7 trading days or when postings stabilize for 2 consecutive weeks above entry threshold

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Indeed, ZipRecruiter, and Glassdoor job posting counts via rss_count or html_table weekly snapshot via scrape (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Job posting boards are highly volatile and responsive to economic cycles. Hiring cycles turn multiple times annually, producing 10-15%+ swings regularly.

## Required Keys
- None
