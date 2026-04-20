# Financial Sector Momentum Divergence With Spy

**Idea ID:** `financial-sector-momentum-divergence-with-spy`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
If XLF's 10-day momentum turns positive while SPY's remains negative, it often precedes outperformance in financials. Financials can lead broad market recoveries when their momentum diverges positively.

## Universe
- XLF

## Data Sources
- Yahoo Finance daily returns for XLF and SPY

## Signal Logic
Enter long XLF when 10-day momentum >0 and SPY 10-day momentum <0

## Entry / Exit
Entry: Enter long XLF when 10-day momentum >0 and SPY 10-day momentum <0 Exit: Exit if XLF momentum turns negative or SPY momentum turns positive

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Yahoo Finance daily returns for XLF and SPY via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Momentum divergences between sectors and SPY occur regularly in volatile markets.

## Required Keys
- None
