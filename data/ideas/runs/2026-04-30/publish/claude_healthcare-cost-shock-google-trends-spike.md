# Healthcare Cost Shock Google Trends Spike

**Idea ID:** `healthcare-cost-shock-google-trends-spike`
**Family:** `consumer_stress`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Combined search volume across healthcare cost keywords rises 35%+ from prior week, signaling consumer anxiety about medical affordability. Spike in healthcare cost searches precedes pressure on healthcare stocks due to pricing concerns, regulatory scrutiny, and consumer pushback.

## Universe
- XLV

## Data Sources
- Google Trends weekly search volume for 'health insurance costs', 'medical debt', 'prescription drug prices' through google_trends adapter

## Signal Logic
If combined weekly search volume for healthcare cost keywords is 35%+ above prior week and above 52-week median

## Entry / Exit
Entry: If combined weekly search volume for healthcare cost keywords is 35%+ above prior week and above 52-week median Exit: After 9 trading days or once search volume returns to 2-week average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search volume for 'health insurance costs', 'medical debt', 'prescription drug prices' through google_trends adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Healthcare cost anxiety spikes monthly around enrollment periods, earnings reports, and policy news; threshold fires 2-3 times per quarter.

## Required Keys
- None
