# Political Insider Selling Spike In Financial Sector Etfs

**Idea ID:** `political-insider-selling-spike-in-financial-sector-etfs`
**Family:** `political_insider_filing`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Surge in insider selling in financial sector ETFs often precedes sector weakness due to anticipated regulatory or economic headwinds. Insider selling signals reduced confidence in financial sector outlook.

## Universe
- XLF

## Data Sources
- Political insider filings aggregated weekly (public scrape)

## Signal Logic
Enter short XLF if insider selling volume exceeds average by 30% over past 2 weeks

## Entry / Exit
Entry: Enter short XLF if insider selling volume exceeds average by 30% over past 2 weeks Exit: Exit after 5 weeks or if insider selling volume normalizes

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Political insider filings aggregated weekly (public scrape) via scrape (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Political insider filings frequently spike with sector regulatory fears.

## Required Keys
- None
