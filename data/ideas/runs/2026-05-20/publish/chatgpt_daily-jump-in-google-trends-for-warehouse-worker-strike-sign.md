# Daily Jump In Google Trends For Warehouse Worker Strike Signals Labor Stress In Logistics

**Idea ID:** `daily-jump-in-google-trends-for-warehouse-worker-strike-sign`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Rising strike-related searches reflect potential labor disruptions in logistics-heavy sectors. Warehouse labor strikes disrupt supply chains increasing costs for industrial companies.

## Universe
- XLI

## Data Sources
- Google Trends daily search interest

## Signal Logic
If daily Google Trends for 'warehouse worker strike' rises 40% vs 7-day average

## Entry / Exit
Entry: If daily Google Trends for 'warehouse worker strike' rises 40% vs 7-day average Exit: After 7 trading days or if trend drops below 20% above baseline

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends daily search interest via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Labor disputes and strike rumors frequently spike due to contract negotiations and media coverage.

## Required Keys
- None
