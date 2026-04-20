# Lumber Futures Rollercoaster

**Idea ID:** `lumber-futures-rollercoaster`
**Source:** anthropic / claude-3-haiku-20240307
**Frequency:** daily

## Thesis
Lumber futures can experience wild price swings that outpace the broader market, often correcting sharply after a rapid run-up. Lumber is a key industrial commodity that feeds into construction and housing costs.

## Universe
- XLB

## Data Sources
- Yahoo Finance daily prices for LBS and SPY through price_only adapter

## Signal Logic
If LBS closes up more than 6% for the day

## Entry / Exit
Entry: If LBS closes up more than 6% for the day Exit: After 5 trading days or once LBS underperforms SPY by 4%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Yahoo Finance daily prices for LBS and SPY through price_only adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Lumber futures are known for their volatile price swings, often driven by supply chain disruptions and weather-related events.

## Required Keys
- None
