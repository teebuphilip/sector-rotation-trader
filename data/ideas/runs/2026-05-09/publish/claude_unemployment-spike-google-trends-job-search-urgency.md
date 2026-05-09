# Unemployment Spike Google Trends Job Search Urgency

**Idea ID:** `unemployment-spike-google-trends-job-search-urgency`
**Family:** `labor_jobs`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Sudden spikes in unemployment-related and urgent job search queries precede or coincide with labor market deterioration. High search volume indicates worker stress and hiring slowdown. Job insecurity depresses consumer discretionary spending; labor stress reduces purchasing power.

## Universe
- XLY

## Data Sources
- Google Trends weekly search interest for 'unemployment benefits' and 'job openings near me' through google_trends adapter

## Signal Logic
If combined search index for both terms rises above 70th percentile of 52-week range in a single week

## Entry / Exit
Entry: If combined search index for both terms rises above 70th percentile of 52-week range in a single week Exit: After 14 calendar days or if index falls back below 50th percentile for 2 consecutive weeks

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'unemployment benefits' and 'job openings near me' through google_trends adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Job market anxiety spikes occur monthly around earnings announcements, layoff waves, and macro uncertainty; threshold is loose enough to fire 2–3 times per month.

## Required Keys
- None
