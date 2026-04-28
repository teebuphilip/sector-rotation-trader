# Wage Growth Demand Surge Fast Food Google Trends

**Idea ID:** `wage-growth-demand-surge-fast-food-google-trends`
**Family:** `labor_jobs`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When combined search interest spikes >35% above 52-week baseline, it signals labor tightness in low-wage sectors. Restaurant and hospitality operators face cost inflation; profit margins compress. Fast food wage pressure forces menu price increases; consumer traffic declines or transaction sizes stall, compressing restaurant operator margins.

## Universe
- XLY

## Data Sources
- Google Trends weekly search volume for 'fast food hiring', 'minimum wage increase', 'restaurant worker pay'

## Signal Logic
Combined normalized search score >135 (baseline 100) sustained for 2 consecutive weeks

## Entry / Exit
Entry: Combined normalized search score >135 (baseline 100) sustained for 2 consecutive weeks Exit: Score falls below 115 or 18 trading days elapsed

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search volume for 'fast food hiring', 'minimum wage increase', 'restaurant worker pay' via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Fast food hiring/wage searches spike seasonally (spring/summer) and during policy announcements; fires 5–7 times per year.

## Required Keys
- None
