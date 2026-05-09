# Weekly Google Trends Surge For Warehouse Worker Strike Signals Freight Logistics Disruption

**Idea ID:** `weekly-google-trends-surge-for-warehouse-worker-strike-signa`
**Family:** `freight_logistics`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
A spike in strike-related searches implies potential supply chain or freight disruptions, often pressuring industrial stocks but benefiting alternative logistics firms. Industrial sector faces pressure from labor disruptions affecting supply chains and freight operations.

## Universe
- XLI

## Data Sources
- Google Trends weekly search interest

## Signal Logic
Enter short if weekly 'warehouse worker strike' search interest increases by more than 30% week-over-week

## Entry / Exit
Entry: Enter short if weekly 'warehouse worker strike' search interest increases by more than 30% week-over-week Exit: Exit after 4 weeks or once interest normalizes below 15% increase

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Labor disputes in logistics appear repeatedly with seasonal or contractual cycles.

## Required Keys
- None
