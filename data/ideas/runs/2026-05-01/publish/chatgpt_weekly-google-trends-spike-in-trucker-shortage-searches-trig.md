# Weekly Google Trends Spike In Trucker Shortage Searches Triggers Bearish Freight Logistics Sector

**Idea ID:** `weekly-google-trends-spike-in-trucker-shortage-searches-trig`
**Family:** `freight_logistics`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising concern over truck driver shortages signals imminent freight bottlenecks and cost pressures. Logistics companies face margin compression and delays from labor shortages.

## Universe
- XLI

## Data Sources
- Google Trends weekly search interest

## Signal Logic
Enter short XLI when weekly searches for 'truck driver shortage' exceed 30% above 12-week average

## Entry / Exit
Entry: Enter short XLI when weekly searches for 'truck driver shortage' exceed 30% above 12-week average Exit: Exit after 5 weeks or when search volume drops below 12-week average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Labor shortage narratives rise and fall regularly, producing frequent actionable signals.

## Required Keys
- None
