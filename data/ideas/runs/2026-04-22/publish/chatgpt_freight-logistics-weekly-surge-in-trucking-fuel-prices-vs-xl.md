# Freight Logistics Weekly Surge In Trucking Fuel Prices Vs Xli Weakness

**Idea ID:** `freight-logistics-weekly-surge-in-trucking-fuel-prices-vs-xl`
**Family:** `freight_logistics`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising trucking fuel costs concurrent with industrial ETF weakness signals margin pressure on logistics-heavy industries. Higher fuel costs squeeze industrial margins, pressuring sector performance.

## Universe
- XLI

## Data Sources
- FRED weekly diesel fuel price

## Signal Logic
Enter short XLI if diesel prices rise >3% WoW and XLI falls >1.5% WoW

## Entry / Exit
Entry: Enter short XLI if diesel prices rise >3% WoW and XLI falls >1.5% WoW Exit: Exit after fuel prices stabilize or XLI rebounds 3%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED weekly diesel fuel price via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 36
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Weekly fuel price volatility combined with sector reactions is common.

## Required Keys
- None
