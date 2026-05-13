# Weekly Jump In Google Trends For Warehouse Labor Shortage Signals Supply Chain Labor Stress And Industrial Sector Risk

**Idea ID:** `weekly-jump-in-google-trends-for-warehouse-labor-shortage-si`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Increased interest in warehouse labor shortages signals labor tightness that can disrupt supply chains and pressure industrial production costs. Labor shortages raise costs and reduce throughput in industrial operations.

## Universe
- XLI

## Data Sources
- Google Trends weekly searches

## Signal Logic
If weekly Google Trends volume for 'warehouse labor shortage' rises 20% week-over-week

## Entry / Exit
Entry: If weekly Google Trends volume for 'warehouse labor shortage' rises 20% week-over-week Exit: After 3 weeks or when volume declines 15% from peak

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly searches via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Warehouse labor tightness is a frequent topic with seasonal hiring cycles.

## Required Keys
- None
