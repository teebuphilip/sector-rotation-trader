# Weekly Drop In Us Jobless Claims Signals Bullish Labor Market And Financial Sector Strength

**Idea ID:** `weekly-drop-in-us-jobless-claims-signals-bullish-labor-marke`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
A material weekly decline in jobless claims indicates improving labor conditions and economic strength. Lower unemployment claims support stronger credit demand and financial sector profit growth.

## Universe
- XLF

## Data Sources
- FRED weekly US jobless claims via fred_series adapter

## Signal Logic
If weekly jobless claims drop more than 5% week-over-week

## Entry / Exit
Entry: If weekly jobless claims drop more than 5% week-over-week Exit: When claims rise above 2% week-over-week

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED weekly US jobless claims via fred_series adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 48
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Weekly jobless claims data shows regular fluctuations tied to economic cycles.

## Required Keys
- None
