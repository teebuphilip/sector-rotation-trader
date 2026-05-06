# Food Beverage Delivery Demand Collapse Signal

**Idea ID:** `food-beverage-delivery-demand-collapse-signal`
**Family:** `consumer_stress`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When combined food/beverage delivery search interest drops 30%+ from peak trailing 3-month average, consumer discretionary stress is accelerating; staples outperform within 5-10 days. Delivery service demand collapse signals consumer retreat from discretionary spending to value/staple alternatives.

## Universe
- XLY

## Data Sources
- Google Trends weekly searches for 'food delivery deals' + 'restaurant delivery near me' + 'meal kit discount' through google_trends adapter

## Signal Logic
If delivery search index falls 30% below 3-month peak, short XLY and go long XLP on Monday open

## Entry / Exit
Entry: If delivery search index falls 30% below 3-month peak, short XLY and go long XLP on Monday open Exit: Exit after 8 trading days or if search index recovers to 75% of peak

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly searches for 'food delivery deals' + 'restaurant delivery near me' + 'meal kit discount' through google_trends adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Food delivery searches are demand-sensitive and cycle with stimulus/unemployment events; 30% drops occur 3-4 times per year.

## Required Keys
- None
