# Weekly Rise In Rss Count For Labor Strike News Signals Industrial Sector Risk

**Idea ID:** `weekly-rise-in-rss-count-for-labor-strike-news-signals-indus`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
An increase in labor strike news volume indicates rising union activity and potential production disruptions in industrial sectors. Strikes often reduce output and hurt industrial earnings.

## Universe
- XLI

## Data Sources
- RSS news feed counts

## Signal Logic
If weekly RSS news count for 'labor strike' increases by 25% week-over-week

## Entry / Exit
Entry: If weekly RSS news count for 'labor strike' increases by 25% week-over-week Exit: After 3 weeks or when count declines 20% from peak

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS news feed counts via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Labor disputes have a recurring cadence tied to contract talks and economic conditions.

## Required Keys
- None
