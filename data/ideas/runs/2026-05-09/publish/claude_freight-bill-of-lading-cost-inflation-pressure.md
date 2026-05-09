# Freight Bill Of Lading Cost Inflation Pressure

**Idea ID:** `freight-bill-of-lading-cost-inflation-pressure`
**Family:** `freight_logistics`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When inventory growth outpaces sales growth, logistics firms hold excess cargo and rates compress. Sudden sales acceleration forces rapid restocking, spiking freight demand and rates. Freight logistics (rail, trucking, shipping) benefit from cargo volume spikes and higher utilization rates.

## Universe
- XLI

## Data Sources
- FRED series ID TOTALSA (Total Business Inventories) and FRED EXCRESW (Advance Retail Sales) ratio divergence through fred_series adapter

## Signal Logic
If weekly inventory-to-sales ratio drops below 2-month low and retail sales surprise positively by 2%+ week-over-week

## Entry / Exit
Entry: If weekly inventory-to-sales ratio drops below 2-month low and retail sales surprise positively by 2%+ week-over-week Exit: After 10 trading days or if inventory ratio rises back above 2-month moving average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series ID TOTALSA (Total Business Inventories) and FRED EXCRESW (Advance Retail Sales) ratio divergence through fred_series adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Inventory cycles reset quarterly; sales surprises and ratio inversions fire 2–4 times per quarter.

## Required Keys
- None
