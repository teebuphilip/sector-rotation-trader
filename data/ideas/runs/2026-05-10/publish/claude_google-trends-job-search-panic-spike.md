# Google Trends Job Search Panic Spike

**Idea ID:** `google-trends-job-search-panic-spike`
**Family:** `labor_jobs`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Sharp spikes in job-search-related Google searches signal layoff fears or employment anxiety, causing consumer spending pullbacks and volatility in discretionary sectors. Job search anxiety correlates with consumer confidence collapse and discretionary spending cuts.

## Universe
- XLY

## Data Sources
- Google Trends weekly search interest for 'how to write a resume' and 'interview tips,' normalized to baseline

## Signal Logic
If either 'resume' or 'interview tips' search volume jumps >40% week-over-week above 12-week moving average, short discretionary

## Entry / Exit
Entry: If either 'resume' or 'interview tips' search volume jumps >40% week-over-week above 12-week moving average, short discretionary Exit: Exit after 10 trading days or if search interest returns to <110% of 12-week MA

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'how to write a resume' and 'interview tips,' normalized to baseline via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Job-search Google Trends spike above 40% threshold 3–5 times per quarter due to weekly earnings seasons, layoff news cycles, and seasonal hiring patterns.

## Required Keys
- None
