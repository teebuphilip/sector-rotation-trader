# Recession Whisper Google Trends Unemployment Search Surge

**Idea ID:** `recession-whisper-google-trends-unemployment-search-surge`
**Family:** `labor_jobs`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When combined search interest in unemployment + layoff terms spikes >40% above 52-week baseline in a single week, consumer anxiety peaks. Historical lead to risk-off rotation. Unemployment search spikes precede consumer spending weakness; discretionary retailers face demand headwinds 2–4 weeks later.

## Universe
- XLY

## Data Sources
- Google Trends weekly search volume for terms: 'unemployment benefits', 'job loss', 'layoffs near me'

## Signal Logic
Combined normalized search score >140 (baseline 100) and >40% above 52-week mean

## Entry / Exit
Entry: Combined normalized search score >140 (baseline 100) and >40% above 52-week mean Exit: Score falls below 120 or 20 trading days elapsed

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search volume for terms: 'unemployment benefits', 'job loss', 'layoffs near me' via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 36
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Unemployment search interest spikes 4–5 times annually during earnings seasons and macro shock periods; low barrier to fire.

## Required Keys
- None
