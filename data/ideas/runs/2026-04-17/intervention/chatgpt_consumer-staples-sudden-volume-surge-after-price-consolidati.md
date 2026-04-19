# Consumer Staples Sudden Volume Surge After Price Consolidation

**Idea ID:** `consumer-staples-sudden-volume-surge-after-price-consolidati`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
After 7 days of narrow price range, a volume spike often precedes breakout moves in consumer staples. Volume surges following consolidation indicate renewed buying interest in defensive stocks.

## Universe
- XLP

## Data Sources
- Yahoo Finance daily prices and volume for XLP via price_only adapter

## Signal Logic
If XLP daily range <0.5% for 7 days and volume on day 8 > 120% of 20-day average

## Entry / Exit
Entry: If XLP daily range <0.5% for 7 days and volume on day 8 > 120% of 20-day average Exit: After 10 days or 5% price gain

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Yahoo Finance daily prices and volume for XLP via price_only adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Price consolidations and volume spikes happen regularly in staples sector.

## Required Keys
- None
