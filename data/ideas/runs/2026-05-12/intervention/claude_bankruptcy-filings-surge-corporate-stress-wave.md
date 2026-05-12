# Bankruptcy Filings Surge Corporate Stress Wave

**Idea ID:** `bankruptcy-filings-surge-corporate-stress-wave`
**Family:** `labor_jobs`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Spikes in corporate bankruptcy filings (Chapter 11) signal debt stress across the economy; lag 1–2 weeks before credit spreads widen and equities selloff. Rising corporate bankruptcies increase bank loan losses and reduce confidence in credit quality; financial sector reprices risk higher.

## Universe
- XLF

## Data Sources
- US Courts public bankruptcy filing data (Chapter 7, 11, 13) via html_table scrape; weekly aggregation of new filings

## Signal Logic
If weekly Chapter 11 filings exceed 12-week MA by >20% and XLF closes down >0.5%

## Entry / Exit
Entry: If weekly Chapter 11 filings exceed 12-week MA by >20% and XLF closes down >0.5% Exit: After 10 trading days or when weekly filings fall below 12-week MA

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use US Courts public bankruptcy filing data (Chapter 7, 11, 13) via html_table scrape; weekly aggregation of new filings via scrape (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Economic cycles and credit tightening events drive bankruptcy waves; signal fires 2–3 times per year.

## Required Keys
- None
