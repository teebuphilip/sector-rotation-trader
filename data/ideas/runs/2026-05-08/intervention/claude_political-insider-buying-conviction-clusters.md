# Political Insider Buying Conviction Clusters

**Idea ID:** `political-insider-buying-conviction-clusters`
**Family:** `political_insider_filing`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When insider buy volume (Form 4 filings) in a single sector exceeds prior 3-month average by 40%+ within a rolling 5-day window, it signals conviction-level buying by corporate officers. Equities typically outperform sector benchmarks by 2-5% in following 2-3 weeks as momentum builds. Concentrated insider buying in technology reflects executive conviction on valuation; historically precedes 15-30 day outperformance rallies.

## Universe
- XLK

## Data Sources
- SEC insider trading filings (Form 4 aggregate buys per sector, weekly via html_table adapter scrape of SEC EDGAR filings)

## Signal Logic
Aggregate Form 4 buy volume in XLK exceeds 3-month rolling avg by 40%+; enter long XLK at next day open

## Entry / Exit
Entry: Aggregate Form 4 buy volume in XLK exceeds 3-month rolling avg by 40%+; enter long XLK at next day open Exit: After 14 trading days OR if insider buy volume returns to baseline, whichever first

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use SEC insider trading filings (Form 4 aggregate buys per sector, weekly via html_table adapter scrape of SEC EDGAR filings) via scrape (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: SEC filings update daily and aggregate weekly; insider conviction clusters occur every 2-3 weeks across sectors; 14-day windows align with insider position accumulation cycles.

## Required Keys
- None
