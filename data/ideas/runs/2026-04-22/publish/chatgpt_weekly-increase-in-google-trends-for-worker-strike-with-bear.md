# Weekly Increase In Google Trends For Worker Strike With Bearish Xli And Xly

**Idea ID:** `weekly-increase-in-google-trends-for-worker-strike-with-bear`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising labor unrest concerns can pressure industrial and consumer discretionary sectors through supply disruptions and demand uncertainty. Industrial sector is sensitive to labor disruptions.

## Universe
- XLI

## Data Sources
- Google Trends weekly for 'worker strike' and Yahoo Finance weekly XLI and XLY prices

## Signal Logic
Short XLI and XLY when 'worker strike' searches increase >15% week-over-week and sectors underperform SPY

## Entry / Exit
Entry: Short XLI and XLY when 'worker strike' searches increase >15% week-over-week and sectors underperform SPY Exit: Cover after 4 weeks or when search interest declines

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly for 'worker strike' and Yahoo Finance weekly XLI and XLY prices via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Labor unrest spikes happen seasonally and during economic stress.

## Required Keys
- None
