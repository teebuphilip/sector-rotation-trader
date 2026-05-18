# Freight Rail Car Utilization Collapse Signals Logistics Downturn

**Idea ID:** `freight-rail-car-utilization-collapse-signals-logistics-down`
**Family:** `freight_logistics`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Railroad freight car utilization drops sharply when industrial demand weakens, signaling recession pressure on logistics and manufacturing. Weekly AAR reports are consistent and predictable. Low freight utilization precedes industrial slowdown and manufacturing contraction, directly impacting industrial equipment and transportation stocks.

## Universe
- XLI

## Data Sources
- Association of American Railroads weekly freight car availability and utilization through html_table adapter

## Signal Logic
If weekly freight car utilization falls more than 8% below its 12-week moving average, enter short.

## Entry / Exit
Entry: If weekly freight car utilization falls more than 8% below its 12-week moving average, enter short. Exit: Exit after 10 trading days or when utilization rebounds to within 3% of 12-week MA.

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Association of American Railroads weekly freight car availability and utilization through html_table adapter via scrape (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Freight utilization swings 8%+ several times per quarter in normal economic cycles, making it a frequent signal generator.

## Required Keys
- None
