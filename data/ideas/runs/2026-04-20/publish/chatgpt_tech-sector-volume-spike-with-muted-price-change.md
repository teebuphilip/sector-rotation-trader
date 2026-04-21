# Tech Sector Volume Spike With Muted Price Change

**Idea ID:** `tech-sector-volume-spike-with-muted-price-change`
**Family:** ``
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
A sudden 30%+ spike in daily volume without a corresponding 1% price move suggests accumulation or distribution, often preceding a directional breakout. Volume spikes with flat price often indicate institutional positioning in technology stocks.

## Universe
- XLK

## Data Sources
- Yahoo Finance daily volume and price for XLK

## Signal Logic
Enter long if daily volume is 30% higher than 20-day average and price change is between -0.5% and +0.5%

## Entry / Exit
Entry: Enter long if daily volume is 30% higher than 20-day average and price change is between -0.5% and +0.5% Exit: Exit after 7 trading days or if price drops more than 2% from entry

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Yahoo Finance daily volume and price for XLK via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Volume spikes without price moves happen regularly in XLK due to sector rotation and news cycles.

## Required Keys
- None
