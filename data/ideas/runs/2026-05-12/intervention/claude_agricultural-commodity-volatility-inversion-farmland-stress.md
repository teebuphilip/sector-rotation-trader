# Agricultural Commodity Volatility Inversion Farmland Stress

**Idea ID:** `agricultural-commodity-volatility-inversion-farmland-stress`
**Family:** `local_economy_weirdness`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When corn and wheat volatility invert (one spikes while the other collapses), it signals supply/demand dislocations that stress rural credit and farm equipment demand. Agricultural equipment manufacturers (John Deere, AGCO) are sensitive to farm profitability; commodity volatility inversions signal margin compression.

## Universe
- XLI

## Data Sources
- FRED series PPIACO (Corn price) and PPIWHE (Wheat price) daily; calculate 10-day rolling volatility for each

## Signal Logic
If 10-day corn vol rises >50% while wheat vol falls >30%, and XLI closes down >1%

## Entry / Exit
Entry: If 10-day corn vol rises >50% while wheat vol falls >30%, and XLI closes down >1% Exit: After 6 trading days or when both volatilities normalize within 20% of each other

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series PPIACO (Corn price) and PPIWHE (Wheat price) daily; calculate 10-day rolling volatility for each via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Seasonal weather, USDA reports, and geopolitical events drive commodity vol spikes monthly.

## Required Keys
- None
