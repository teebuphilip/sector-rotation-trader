# Truck Driver Wage Search Surge

**Idea ID:** `truck-driver-wage-search-surge`
**Family:** `labor_jobs`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Spikes in truck driver job and wage searches signal labor market tightening in freight, often preceding freight rate increases and logistics sector rallies. Tight trucking labor markets correlate with stronger freight demand and pricing power for logistics and industrial companies.

## Universe
- XLI

## Data Sources
- Google Trends weekly search interest for 'truck driver jobs' and 'truck driver salary'

## Signal Logic
If weekly Google Trends index for 'truck driver jobs' or 'truck driver salary' exceeds its 12-week median by 40% or more

## Entry / Exit
Entry: If weekly Google Trends index for 'truck driver jobs' or 'truck driver salary' exceeds its 12-week median by 40% or more Exit: Close after 3 weeks or when index falls below 20% above median

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'truck driver jobs' and 'truck driver salary' via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Labor shortages in transportation are chronic; wage/job search spikes occur 4–6 times per year as seasonal demand fluctuates.

## Required Keys
- None
