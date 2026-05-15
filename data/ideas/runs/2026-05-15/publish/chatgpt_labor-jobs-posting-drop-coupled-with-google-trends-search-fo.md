# Labor Jobs Posting Drop Coupled With Google Trends Search For Job Layoffs

**Idea ID:** `labor-jobs-posting-drop-coupled-with-google-trends-search-fo`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
A simultaneous decline in job postings and spike in layoff-related searches signals deteriorating labor demand. Financial sector often reacts negatively to weakening labor markets due to credit risk concerns.

## Universe
- XLF

## Data Sources
- Google Trends weekly search interest for layoffs; job board postings data

## Signal Logic
If weekly job postings drop 10% and layoff search volume rises 20% vs prior week

## Entry / Exit
Entry: If weekly job postings drop 10% and layoff search volume rises 20% vs prior week Exit: When either metric reverses by 10%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for layoffs; job board postings data via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Labor market fluctuations and layoff news frequently occur with weekly cadence.

## Required Keys
- None
