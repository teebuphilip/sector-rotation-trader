# Weekly Google Trends Surge For Political Insider Stock Buys Signals Bullish Financial Sector

**Idea ID:** `weekly-google-trends-surge-for-political-insider-stock-buys-`
**Family:** `political_insider_filing`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
An increase in political insider stock purchase filings often precedes bullish sentiment in financial stocks. Political insiders buying stocks signals confidence, driving financial sector optimism.

## Universe
- XLF

## Data Sources
- Scraped political insider filings from public tables

## Signal Logic
If weekly count of insider buy filings rises by 25% vs prior 4-week average

## Entry / Exit
Entry: If weekly count of insider buy filings rises by 25% vs prior 4-week average Exit: After 4 weeks or when filings fall below prior average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Scraped political insider filings from public tables via scrape (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Insider buying filings cluster around certain weeks each quarter.

## Required Keys
- None
