# Consumer Discretionary Weekly Volume-price Divergence

**Idea ID:** `consumer-discretionary-weekly-volume-price-divergence`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
When price drops more than 3% but volume increases 20% week-over-week, a reversal bounce often follows. Divergence often signals capitulation and institutional accumulation.

## Universe
- XLY

## Data Sources
- Yahoo Finance weekly price and volume for XLY via price_only adapter

## Signal Logic
If weekly price return < -3% and volume > 120% of prior 4-week average

## Entry / Exit
Entry: If weekly price return < -3% and volume > 120% of prior 4-week average Exit: After 3 weeks or price rebounds 5%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Yahoo Finance weekly price and volume for XLY via price_only adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Volume-price divergences appear multiple times yearly in consumer discretionary.

## Required Keys
- None
