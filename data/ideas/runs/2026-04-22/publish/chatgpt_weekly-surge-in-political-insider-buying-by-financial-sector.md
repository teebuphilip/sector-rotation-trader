# Weekly Surge In Political Insider Buying By Financial Sector Executives

**Idea ID:** `weekly-surge-in-political-insider-buying-by-financial-sector`
**Family:** `political_insider_filing`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Spike in insider buying signals confidence in financial sector outlook. Insider buying often precedes positive sector performance.

## Universe
- XLF

## Data Sources
- Political insider filings aggregated weekly for XLF companies

## Signal Logic
If insider buying volume exceeds 140% of 4-week average

## Entry / Exit
Entry: If insider buying volume exceeds 140% of 4-week average Exit: After 3 weeks or buying volume falls below 110% of average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Political insider filings aggregated weekly for XLF companies via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Financial sector insider activity varies frequently with earnings and macro news.

## Required Keys
- None
