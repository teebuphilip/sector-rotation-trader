# Weekly Google Trends Spike For Urgent Job Resignation Searches Signals Labor Market Stress

**Idea ID:** `weekly-google-trends-spike-for-urgent-job-resignation-search`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Increasing urgency in job resignation searches implies rising employee stress and labor churn. High turnover and labor stress can disrupt retail and consumer discretionary operations.

## Universe
- XLY

## Data Sources
- Google Trends weekly urgent job resignation related searches

## Signal Logic
Entry when weekly urgent resignation searches rise 15% over 3-week average

## Entry / Exit
Entry: Entry when weekly urgent resignation searches rise 15% over 3-week average Exit: Exit when searches revert to within 5% of 3-week average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly urgent job resignation related searches via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Labor market stress and turnover spikes often respond to wage negotiations, inflation, or sector-specific shocks.

## Required Keys
- None
