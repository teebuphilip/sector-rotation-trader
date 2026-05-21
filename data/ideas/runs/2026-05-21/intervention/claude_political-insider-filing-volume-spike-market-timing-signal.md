# Political Insider Filing Volume Spike Market Timing Signal

**Idea ID:** `political-insider-filing-volume-spike-market-timing-signal`
**Family:** `political_insider_filing`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Daily insider stock sale filings spike >45% above 30-day MA, suggesting executives are reducing exposure ahead of earnings or correction. Technology and software executives often lead sell-offs; elevated insider sales precede 3-6 month underperformance.

## Universe
- XLK

## Data Sources
- SEC insider transaction filings (Form 4) aggregate count via html_table scraper; daily count

## Signal Logic
If daily insider sale count exceeds 30-day MA by >45%

## Entry / Exit
Entry: If daily insider sale count exceeds 30-day MA by >45% Exit: After 15 trading days or on reversion to 30-day MA baseline

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use SEC insider transaction filings (Form 4) aggregate count via html_table scraper; daily count via scrape (daily).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Insider filing activity is volatile and seasonal; blackout periods create lumpy daily spikes 4-6 times per quarter.

## Required Keys
- None
