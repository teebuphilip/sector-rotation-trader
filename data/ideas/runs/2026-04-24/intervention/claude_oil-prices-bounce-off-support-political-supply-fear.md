# Oil Prices Bounce Off Support Political Supply Fear

**Idea ID:** `oil-prices-bounce-off-support-political-supply-fear`
**Family:** `political_insider_filing`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Crude oil prices fall to 2-year support level, then reverse sharply on news of supply disruption (OPEC+ cuts, geopolitical event), driving energy sector rebound. Energy stocks rally when oil prices stabilize at support after sharp declines.

## Universe
- XLE

## Data Sources
- EIA weekly crude inventories and price data via eia_electricity adapter and price_only for crude (CL=F)

## Signal Logic
If crude price closes >5% below 52-week MA and EIA inventory reports decline, long XLE

## Entry / Exit
Entry: If crude price closes >5% below 52-week MA and EIA inventory reports decline, long XLE Exit: Exit after 10 trading days or if crude breaks support again

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use EIA weekly crude inventories and price data via eia_electricity adapter and price_only for crude (CL=F) via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Oil bounces off support 2–4 times per year; geopolitical events trigger supply fear spikes monthly on average.

## Required Keys
- None
