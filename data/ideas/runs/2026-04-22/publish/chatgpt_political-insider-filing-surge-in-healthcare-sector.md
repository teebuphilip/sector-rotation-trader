# Political Insider Filing Surge In Healthcare Sector

**Idea ID:** `political-insider-filing-surge-in-healthcare-sector`
**Family:** `political_insider_filing`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Surge in insider selling filings in healthcare signals potential regulatory or earnings concerns. Insider selling often predicts near-term sector softness, especially in regulated sectors like healthcare.

## Universe
- XLV

## Data Sources
- SEC insider filing API for healthcare sector stocks

## Signal Logic
Enter short XLV if insider selling filings exceed 3x 30-day average on a given day

## Entry / Exit
Entry: Enter short XLV if insider selling filings exceed 3x 30-day average on a given day Exit: Exit after filings normalize below 1.5x average or after 10 trading days

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use SEC insider filing API for healthcare sector stocks via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Insider filing spikes in healthcare happen regularly around earnings and policy news.

## Required Keys
- None
