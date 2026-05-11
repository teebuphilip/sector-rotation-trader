# Healthcare Cost Inflation Google Trends Acceleration

**Idea ID:** `healthcare-cost-inflation-google-trends-acceleration`
**Family:** `consumer_stress`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When combined search index for healthcare cost anxiety spikes 80%+ above 8-week baseline, it signals consumer stress, pressuring discretionary spending and benefiting defensive healthcare. Rising healthcare cost anxiety drives insurance/pharma stock gains as consumers perceive healthcare as non-negotiable essential services.

## Universe
- XLV

## Data Sources
- Google Trends weekly search interest for 'healthcare costs rising' + 'medical debt help' via google_trends adapter

## Signal Logic
If combined healthcare cost anxiety search index exceeds 8-week average by 80%

## Entry / Exit
Entry: If combined healthcare cost anxiety search index exceeds 8-week average by 80% Exit: After 12 trading days or if index reverts to <110% of baseline

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'healthcare costs rising' + 'medical debt help' via google_trends adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Healthcare cost anxieties spike seasonally during enrollment periods, rate hikes, and insurance news cycles; 2-3 signals per quarter expected.

## Required Keys
- None
