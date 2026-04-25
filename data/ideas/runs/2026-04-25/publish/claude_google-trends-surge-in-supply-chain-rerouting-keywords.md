# Google Trends Surge In Supply Chain Rerouting Keywords

**Idea ID:** `google-trends-surge-in-supply-chain-rerouting-keywords`
**Family:** `freight_logistics`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Spikes in supply chain rerouting searches indicate corporate logistics strategy shifts and manufacturing relocation activity, preceding industrial and materials sector moves. Supply chain optimization spending and reshoring capex drive industrial equipment and manufacturing services demand.

## Universe
- XLI

## Data Sources
- Google Trends weekly search volume for 'nearshoring', 'supply chain resilience', 'logistics optimization'

## Signal Logic
If 3-week average of combined search volume exceeds 65th percentile of prior 52-week distribution

## Entry / Exit
Entry: If 3-week average of combined search volume exceeds 65th percentile of prior 52-week distribution Exit: After 14 trading days or if search volume falls below 50th percentile for 2 consecutive weeks

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search volume for 'nearshoring', 'supply chain resilience', 'logistics optimization' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Supply chain discussions are persistent; search volume surges occur regularly with quarterly earnings seasons and geopolitical events.

## Required Keys
- None
