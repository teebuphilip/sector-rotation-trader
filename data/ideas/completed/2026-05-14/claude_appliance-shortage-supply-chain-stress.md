# Appliance Shortage Supply Chain Stress

**Idea ID:** `appliance-shortage-supply-chain-stress`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Spikes in appliance availability searches signal supply chain bottlenecks and producer input cost shocks, suggesting manufacturing and logistics stress. Supply constraints indicate upstream cost inflation and margin compression for appliance manufacturers and retailers.

## Universe
- XLI

## Data Sources
- Google Trends weekly search volume for 'appliance shortage' and 'where to buy washing machine'

## Signal Logic
If weekly Google Trends volume for 'appliance shortage' rises >35% above 12-week moving average

## Entry / Exit
Entry: If weekly Google Trends volume for 'appliance shortage' rises >35% above 12-week moving average Exit: After 15 trading days or when volume drops below entry baseline

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search volume for 'appliance shortage' and 'where to buy washing machine' via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Supply chain disruptions occur regularly; seasonal demand surges (spring/summer home repair) create predictable shortage cycles.

## Required Keys
- None
