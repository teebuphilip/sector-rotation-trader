# Freight Rail Carload Collapse Logistics Sector Fade

**Idea ID:** `freight-rail-carload-collapse-logistics-sector-fade`
**Family:** `freight_logistics`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When weekly rail carloads drop 5%+ vs prior year AND are below 52-week median, it signals demand destruction across commodity and manufacturing chains; XLI reverses lower. Rail carloads are a coincident indicator of industrial production and logistics demand; collapses signal recession or inventory reduction.

## Universe
- XLI

## Data Sources
- FRED Carloads (RAILCARLD) weekly data via API

## Signal Logic
If carloads down 5%+ YoY and below 52-week median, short XLI.

## Entry / Exit
Entry: If carloads down 5%+ YoY and below 52-week median, short XLI. Exit: After 10 trading days or if carloads rise 3% WoW.

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED Carloads (RAILCARLD) weekly data via API via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Rail carload volatility and YoY declines occur in economic slowdowns; threshold fires 2-3 times per year reliably.

## Required Keys
- None
