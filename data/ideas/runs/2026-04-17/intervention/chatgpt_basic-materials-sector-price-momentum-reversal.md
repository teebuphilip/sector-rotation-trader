# Basic Materials Sector Price Momentum Reversal

**Idea ID:** `basic-materials-sector-price-momentum-reversal`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
After a 7-day positive momentum streak exceeding 6%, XLB often pulls back sharply before resuming trend. Sharp momentum runs are frequently followed by short-term corrections in materials.

## Universe
- XLB

## Data Sources
- Yahoo Finance daily prices for XLB using price_only adapter

## Signal Logic
If XLB gains >6% over past 7 days, enter short next day

## Entry / Exit
Entry: If XLB gains >6% over past 7 days, enter short next day Exit: After 5 days or 3% price retracement

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Yahoo Finance daily prices for XLB using price_only adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Momentum overextensions happen regularly in materials sector.

## Required Keys
- None
