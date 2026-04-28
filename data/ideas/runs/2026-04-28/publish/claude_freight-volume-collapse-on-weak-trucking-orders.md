# Freight Volume Collapse On Weak Trucking Orders

**Idea ID:** `freight-volume-collapse-on-weak-trucking-orders`
**Family:** `freight_logistics`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When weekly truck tonnage declines >3% week-over-week for 2 consecutive weeks, logistics providers face utilization collapse and pricing pressure. Industrial demand weakens ahead of broader slowdown. Trucking tonnage is a lead indicator of industrial production and capex demand; sustained declines signal margin compression across industrials and transportation.

## Universe
- XLI

## Data Sources
- FRED series TOTALSA (total truck tonnage and carloads) via API

## Signal Logic
Weekly tonnage MoM decline >3% for 2 consecutive weeks; cumulative 2-week decline >6%

## Entry / Exit
Entry: Weekly tonnage MoM decline >3% for 2 consecutive weeks; cumulative 2-week decline >6% Exit: Tonnage rebounds >1% week-over-week or 15 trading days elapsed

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series TOTALSA (total truck tonnage and carloads) via API via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 36
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Freight tonnage is volatile; 3% weekly swings occur 4–6 times annually. Signal fires regularly outside holiday periods.

## Required Keys
- None
