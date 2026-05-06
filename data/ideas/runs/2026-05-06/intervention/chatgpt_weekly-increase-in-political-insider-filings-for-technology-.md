# Weekly Increase In Political Insider Filings For Technology Sector Executives

**Idea ID:** `weekly-increase-in-political-insider-filings-for-technology-`
**Family:** `political_insider_filing`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
A jump in insider buying or selling by tech executives signals confidence or concern about near-term sector performance. Insider buying often precedes positive price moves in technology stocks.

## Universe
- XLK

## Data Sources
- Political insider filings weekly aggregation

## Signal Logic
If insider filings for tech execs show net buying volume increase of 30% week-over-week

## Entry / Exit
Entry: If insider filings for tech execs show net buying volume increase of 30% week-over-week Exit: After 4 weeks or when net buying returns below 10%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Political insider filings weekly aggregation via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Executive insider activity is steady and reacts to quarterly earnings or guidance changes.

## Required Keys
- None
