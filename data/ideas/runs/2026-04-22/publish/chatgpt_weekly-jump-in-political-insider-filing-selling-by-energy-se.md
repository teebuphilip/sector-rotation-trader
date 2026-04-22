# Weekly Jump In Political Insider Filing Selling By Energy Sector Insiders

**Idea ID:** `weekly-jump-in-political-insider-filing-selling-by-energy-se`
**Family:** `political_insider_filing`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
An unusual spike in insider selling in energy sector signals potential negative near-term outlook or regulatory concerns. Insider selling often precedes negative sector performance.

## Universe
- XLE

## Data Sources
- Political insider filings aggregated weekly for XLE companies

## Signal Logic
If insider selling volume exceeds 150% of 4-week average

## Entry / Exit
Entry: If insider selling volume exceeds 150% of 4-week average Exit: After 3 weeks or if selling volume returns below 110% of average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Political insider filings aggregated weekly for XLE companies via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Insider selling activity fluctuates frequently with earnings and regulatory cycles.

## Required Keys
- None
