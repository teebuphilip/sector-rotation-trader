# Daily Surge In Fred Series Producer Price Index For Steel Signals Industrial Cost Pressure

**Idea ID:** `daily-surge-in-fred-series-producer-price-index-for-steel-si`
**Family:** `macro_input_pressure`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
A sharp increase in steel producer prices signals rising input costs for industrial producers. Rising steel prices increase costs and compress margins for industrial companies.

## Universe
- XLI

## Data Sources
- FRED PPI Steel weekly data

## Signal Logic
Enter short when weekly steel PPI increases 1.5% week-over-week

## Entry / Exit
Entry: Enter short when weekly steel PPI increases 1.5% week-over-week Exit: Exit when weekly PPI growth slows below 0.5% week-over-week

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED PPI Steel weekly data via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Steel price fluctuations occur regularly with supply/demand shifts and tariff news.

## Required Keys
- None
