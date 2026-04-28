# Weekly Surge In Google Trends For Cold Storage Shortage Signals Food Supply Chain Stress

**Idea ID:** `weekly-surge-in-google-trends-for-cold-storage-shortage-sign`
**Family:** `local_economy_weirdness`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising concern around cold storage shortages often indicates supply chain stress in perishable goods. Consumer staples may face margin pressure and inventory disruption from cold storage issues.

## Universe
- XLP

## Data Sources
- Google Trends weekly search interest

## Signal Logic
Enter short XLP if weekly Google Trends for 'cold storage shortage' rises 25% week-over-week

## Entry / Exit
Entry: Enter short XLP if weekly Google Trends for 'cold storage shortage' rises 25% week-over-week Exit: Exit after 4 weeks or if search interest declines by 15% week-over-week

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Cold storage shortages are a recurrent theme during supply chain tightening and seasonal demand.

## Required Keys
- None
