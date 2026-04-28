# Commodity Input Cost Shock Mining Sector Margin Crunch

**Idea ID:** `commodity-input-cost-shock-mining-sector-margin-crunch`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When FRED commodity index (broad basket) spikes >3% in a single day while XLB stays flat or declines, input costs surge faster than mining/materials producer pricing. Margin squeeze imminent. Materials producers cannot immediately pass through input cost shocks; operating margins compress until prices normalize or they cut production.

## Universe
- XLB

## Data Sources
- FRED commodity price indices (energy, metals, agricultural) daily series; XLB ETF daily price via price_only adapter

## Signal Logic
Commodity index +3% day AND XLB +0.5% or lower same day

## Entry / Exit
Entry: Commodity index +3% day AND XLB +0.5% or lower same day Exit: XLB closes >1.5% above entry close or 8 trading days elapsed

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED commodity price indices (energy, metals, agricultural) daily series; XLB ETF daily price via price_only adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Daily commodity shocks >3% occur 2–3 times per month. Divergence with materials ETF pricing happens 4–6 times annually.

## Required Keys
- None
