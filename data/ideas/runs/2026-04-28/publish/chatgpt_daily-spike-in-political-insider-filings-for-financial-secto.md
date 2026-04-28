# Daily Spike In Political Insider Filings For Financial Sector Executives Signals Volatility

**Idea ID:** `daily-spike-in-political-insider-filings-for-financial-secto`
**Family:** `political_insider_filing`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Sudden increase in insider selling or buying among financial sector executives often precedes short-term sector volatility. Insider selling spikes can signal expected headwinds or risk in financials.

## Universe
- XLF

## Data Sources
- SEC insider filings data

## Signal Logic
Enter short XLF if daily insider filings for financial execs increase by 30% over 5-day average with net selling >50%

## Entry / Exit
Entry: Enter short XLF if daily insider filings for financial execs increase by 30% over 5-day average with net selling >50% Exit: Exit after 7 trading days or if insider buying overtakes selling

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use SEC insider filings data via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Political insider activity fluctuates frequently with market conditions and regulatory news.

## Required Keys
- None
