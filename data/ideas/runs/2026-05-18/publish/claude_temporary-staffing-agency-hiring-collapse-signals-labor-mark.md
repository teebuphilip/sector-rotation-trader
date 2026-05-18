# Temporary Staffing Agency Hiring Collapse Signals Labor Market Deterioration

**Idea ID:** `temporary-staffing-agency-hiring-collapse-signals-labor-mark`
**Family:** `labor_jobs`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Weekly announcements of collapsed temporary hiring intentions from major staffing agencies precede broader labor market deterioration and consumer spending weakness. Temp hiring collapse signals companies expect weak demand, reducing consumer spending power and leading to discretionary spending cuts.

## Universe
- XLY

## Data Sources
- ManpowerGroup and Kforce weekly hiring intention indices from earnings call transcripts and press releases through rss_count adapter

## Signal Logic
If weekly temp hiring intention index falls 12% or more below 3-month MA, short XLY.

## Entry / Exit
Entry: If weekly temp hiring intention index falls 12% or more below 3-month MA, short XLY. Exit: Exit after 10 trading days or when index stabilizes above MA.

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use ManpowerGroup and Kforce weekly hiring intention indices from earnings call transcripts and press releases through rss_count adapter via scrape (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Temp hiring swings 12%+ quarterly and reports are published weekly, creating 3–5 signals per quarter.

## Required Keys
- None
