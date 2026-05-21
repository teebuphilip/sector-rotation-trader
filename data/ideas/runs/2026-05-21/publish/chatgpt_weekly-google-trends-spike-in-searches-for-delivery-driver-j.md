# Weekly Google Trends Spike In Searches For Delivery Driver Job Signals Labor Tightness In Logistics

**Idea ID:** `weekly-google-trends-spike-in-searches-for-delivery-driver-j`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising job searches for delivery drivers indicate labor shortages and wage pressure in logistics. Labor tightness increases costs and disrupts industrial logistics operations.

## Universe
- XLI

## Data Sources
- Google Trends weekly 'delivery driver job' searches

## Signal Logic
Enter short when weekly searches rise 20% above 4-week average

## Entry / Exit
Entry: Enter short when weekly searches rise 20% above 4-week average Exit: Exit when searches fall below 10% above 4-week average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly 'delivery driver job' searches via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Driver shortages fluctuate with economic cycles and seasonal demand.

## Required Keys
- None
