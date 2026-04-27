# Weekly Spike In Google Trends For Truck Driver Shortage Signals Bearish Xli

**Idea ID:** `weekly-spike-in-google-trends-for-truck-driver-shortage-sign`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising searches for truck driver shortage signal labor constraints in logistics, pressuring industrial and transportation sectors. Labor shortages increase costs and disrupt freight logistics, pressuring industrial stocks.

## Universe
- XLI

## Data Sources
- Google Trends weekly data for 'truck driver shortage'

## Signal Logic
Enter short if weekly Google Trends interest rises by 25% or more compared to prior week

## Entry / Exit
Entry: Enter short if weekly Google Trends interest rises by 25% or more compared to prior week Exit: Exit after 4 weeks or if interest declines 2 consecutive weeks

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly data for 'truck driver shortage' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Labor shortage concerns fluctuate due to news and economic cycles.

## Required Keys
- None
