# Weekly Spike In Macroinputpressure Fred Series For Natural Gas Prices Signals Bullish Xle

**Idea ID:** `weekly-spike-in-macroinputpressure-fred-series-for-natural-g`
**Family:** `macro_input_pressure`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising natural gas prices benefit energy producers and related energy sector stocks. Higher input prices increase revenues and margins for energy companies.

## Universe
- XLE

## Data Sources
- FRED weekly natural gas price data

## Signal Logic
If weekly natural gas prices increase more than 5% week-over-week

## Entry / Exit
Entry: If weekly natural gas prices increase more than 5% week-over-week Exit: After 3 weeks or if prices decline below 1% growth

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED weekly natural gas price data via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 36
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Natural gas prices are volatile and frequently trend in short bursts.

## Required Keys
- None
