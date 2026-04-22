# Political Insider Filing Surge In Technology Sector Executives Selling With Bearish Xlk Signal

**Idea ID:** `political-insider-filing-surge-in-technology-sector-executiv`
**Family:** `political_insider_filing`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
A cluster of insider sales by tech execs can signal near-term sector weakness or profit-taking ahead of headwinds. Tech insider sales often precede near-term sector pullbacks.

## Universe
- XLK

## Data Sources
- Political insider filings daily technology sector executive sales and Yahoo Finance daily XLK prices

## Signal Logic
Short XLK if insider filings show >3 executives selling on same day and XLK underperforms SPY

## Entry / Exit
Entry: Short XLK if insider filings show >3 executives selling on same day and XLK underperforms SPY Exit: Cover after 7 trading days or if insider selling cluster dissipates

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Political insider filings daily technology sector executive sales and Yahoo Finance daily XLK prices via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Political insider filings happen daily with clusters common enough to trigger signal.

## Required Keys
- None
