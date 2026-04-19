# Healthcare Sector Google Trends Flu Surge

**Idea ID:** `healthcare-sector-google-trends-flu-surge`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising flu-related search interest can predict increased healthcare service demand and pharmaceutical sales. Seasonal illness surges drive higher healthcare utilization and product demand.

## Universe
- XLV

## Data Sources
- Google Trends weekly 'flu symptoms' searches mapped to XLV

## Signal Logic
If weekly flu-related search interest rises >20% week-over-week

## Entry / Exit
Entry: If weekly flu-related search interest rises >20% week-over-week Exit: After 4 weeks or search interest normalizes

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly 'flu symptoms' searches mapped to XLV via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 36
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Flu season spikes annually and affects healthcare demand predictably.

## Required Keys
- None
