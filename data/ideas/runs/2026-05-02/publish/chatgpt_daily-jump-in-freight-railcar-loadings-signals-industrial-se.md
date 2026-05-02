# Daily Jump In Freight Railcar Loadings Signals Industrial Sector Acceleration

**Idea ID:** `daily-jump-in-freight-railcar-loadings-signals-industrial-se`
**Family:** `freight_logistics`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Sudden increases in railcar loadings reflect rising industrial production and freight movement intensity. Freight volume growth is a direct proxy for industrial sector health and economic activity.

## Universe
- XLI

## Data Sources
- FRED freight railcar loadings

## Signal Logic
If daily railcar loadings increase more than 3% day-over-day

## Entry / Exit
Entry: If daily railcar loadings increase more than 3% day-over-day Exit: After 5 days or when loadings drop below 2% day-over-day increase

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED freight railcar loadings via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Industrial shipping activity fluctuates frequently with supply chain needs and production cycles.

## Required Keys
- None
