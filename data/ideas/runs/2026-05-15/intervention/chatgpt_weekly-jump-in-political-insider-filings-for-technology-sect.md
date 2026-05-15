# Weekly Jump In Political Insider Filings For Technology Sector Executives Selling Shares

**Idea ID:** `weekly-jump-in-political-insider-filings-for-technology-sect`
**Family:** `political_insider_filing`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
An unusual increase in insider sales by tech executives signals potential upcoming weakness or valuation concern. Insider selling often precedes short-term sector pullbacks or increased volatility.

## Universe
- XLK

## Data Sources
- SEC insider filing API for technology sector

## Signal Logic
If weekly insider sales volume exceeds 2 standard deviations above 12-week average

## Entry / Exit
Entry: If weekly insider sales volume exceeds 2 standard deviations above 12-week average Exit: After 4 weeks or sales volume normalizes

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use SEC insider filing API for technology sector via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 36
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Regular insider sales reports and clustered executive sales happen frequently.

## Required Keys
- None
