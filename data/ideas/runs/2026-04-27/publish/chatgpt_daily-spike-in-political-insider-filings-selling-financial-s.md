# Daily Spike In Political Insider Filings Selling Financial Stocks Signals Bearish Xlf

**Idea ID:** `daily-spike-in-political-insider-filings-selling-financial-s`
**Family:** `political_insider_filing`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
A surge in insider selling filings by politicians in financial stocks suggests negative sentiment or anticipated headwinds for the sector. Insider selling by politically connected persons hints at deteriorating sector outlook.

## Universe
- XLF

## Data Sources
- Political insider filing daily reports

## Signal Logic
Enter short if daily filings showing insider sales in XLF stocks exceed 2 standard deviations above 30-day average

## Entry / Exit
Entry: Enter short if daily filings showing insider sales in XLF stocks exceed 2 standard deviations above 30-day average Exit: Exit after 5 trading days or when filings normalize

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Political insider filing daily reports via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Political insider filings regularly fluctuate with market events.

## Required Keys
- None
