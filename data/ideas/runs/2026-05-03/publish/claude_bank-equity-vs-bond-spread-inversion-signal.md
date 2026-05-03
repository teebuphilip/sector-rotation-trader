# Bank Equity Vs Bond Spread Inversion Signal

**Idea ID:** `bank-equity-vs-bond-spread-inversion-signal`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When bank stocks dramatically outperform long-duration bonds while yield curve steepens, it signals inflation expectations rising and aggressive rate hike pricing that pressures financial system margins. Rapid bond selloffs combined with bank rallies often precede forced deleveraging as refinancing costs spike and credit spreads widen.

## Universe
- XLF

## Data Sources
- Yahoo Finance daily prices for XLF (financials ETF) and TLT (20-year Treasury ETF); calculate relative performance and yield curve proxy

## Signal Logic
If XLF outperforms TLT by >3% over 5 trading days and TLT closes down >1.5% on the day

## Entry / Exit
Entry: If XLF outperforms TLT by >3% over 5 trading days and TLT closes down >1.5% on the day Exit: Exit after 7 trading days or if performance spread narrows back to <1% over 3-day window

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Yahoo Finance daily prices for XLF (financials ETF) and TLT (20-year Treasury ETF); calculate relative performance and yield curve proxy via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Rate volatility spikes occur regularly; yield curve dynamics shift frequently enough to trigger entry conditions multiple times per month.

## Required Keys
- None
