# Healthcare Cost Shock Google Search Spike

**Idea ID:** `healthcare-cost-shock-google-search-spike`
**Family:** `consumer_stress`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Spikes in healthcare cost-related searches signal consumer financial strain and pressure on healthcare utilization; precedes healthcare sector demand pullback. Rising search interest in medical debt and prescription costs signals demand elasticity; healthcare equity valuations compress on utilization concerns.

## Universe
- XLV

## Data Sources
- Google Trends weekly search volume for 'medical debt' and 'prescription drug cost' through google_trends adapter

## Signal Logic
When 'medical debt' + 'prescription drug cost' combined search interest exceeds 72nd percentile of 26-week rolling baseline

## Entry / Exit
Entry: When 'medical debt' + 'prescription drug cost' combined search interest exceeds 72nd percentile of 26-week rolling baseline Exit: After 6 trading days or when combined search interest falls below 50th percentile

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search volume for 'medical debt' and 'prescription drug cost' through google_trends adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Insurance deductible resets (Jan), drug price negotiations, and benefits season (Nov) create 2–3 cost-shock search spikes per quarter.

## Required Keys
- None
