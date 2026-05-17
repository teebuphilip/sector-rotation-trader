# Google Trends Spike In Recession Proof Job Searches Signals Labor Market Anxiety

**Idea ID:** `google-trends-spike-in-recession-proof-job-searches-signals-`
**Family:** `labor_jobs`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When job-security searches surge (>40% week-over-week), labor market sentiment deteriorates. Workers fear layoffs, signaling incoming unemployment data will disappoint. Consumer discretionary companies depend on wage growth and job security; rising job anxiety predicts lower discretionary spending.

## Universe
- XLY

## Data Sources
- Google Trends weekly search volume for 'recession proof jobs' and 'job security'

## Signal Logic
Google Trends 'recession proof jobs' index jumps >40% week-over-week; XLY closes down >0.6% same week

## Entry / Exit
Entry: Google Trends 'recession proof jobs' index jumps >40% week-over-week; XLY closes down >0.6% same week Exit: XLY closes up >0.8% from entry or 3 weeks elapse

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search volume for 'recession proof jobs' and 'job security' via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Job anxiety spikes emerge 1–2 times per month around earnings seasons and macro shocks.

## Required Keys
- None
