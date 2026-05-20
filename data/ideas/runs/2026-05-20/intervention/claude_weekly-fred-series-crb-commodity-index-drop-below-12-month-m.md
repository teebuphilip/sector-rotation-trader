# Weekly Fred Series Crb Commodity Index Drop Below 12-month Ma

**Idea ID:** `weekly-fred-series-crb-commodity-index-drop-below-12-month-m`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Commodity index declines below long-term trend signal demand weakness and deflationary pressure; lead indicator for industrial and energy sector underperformance. CRB collapse signals commodity demand destruction and raw material price weakness; compresses materials and energy margins.

## Universe
- XLB

## Data Sources
- FRED series CRB (Commodity Research Bureau Index) weekly data via fred_series adapter

## Signal Logic
When weekly CRB closes 6% or more below its 52-week moving average

## Entry / Exit
Entry: When weekly CRB closes 6% or more below its 52-week moving average Exit: After 16 trading days or once CRB closes within 2% of 52-week MA

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series CRB (Commodity Research Bureau Index) weekly data via fred_series adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Commodity cycles generate regular 6%+ dips below long-term trends; fires 1–2 times per quarter.

## Required Keys
- None
