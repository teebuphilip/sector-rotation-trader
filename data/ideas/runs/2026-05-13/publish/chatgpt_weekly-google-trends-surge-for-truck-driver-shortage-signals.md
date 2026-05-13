# Weekly Google Trends Surge For Truck Driver Shortage Signals Freight Logistics Risk And Industrial Cost Pressure

**Idea ID:** `weekly-google-trends-surge-for-truck-driver-shortage-signals`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising interest in truck driver shortages signals constrained freight capacity that can raise costs and slow industrial throughput. Logistics bottlenecks increase operational costs and delay shipments.

## Universe
- XLI

## Data Sources
- Google Trends weekly queries

## Signal Logic
If weekly Google Trends volume for 'truck driver shortage' rises 20% week-over-week

## Entry / Exit
Entry: If weekly Google Trends volume for 'truck driver shortage' rises 20% week-over-week Exit: After 4 weeks or when volume declines 15% from peak

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly queries via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Driver shortage coverage spikes seasonally with fuel price and regulatory changes.

## Required Keys
- None
