# Weekly Spike In Google Trends For Port Worker Overtime Signals Bearish Xli

**Idea ID:** `weekly-spike-in-google-trends-for-port-worker-overtime-signa`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Increased searches for port worker overtime imply labor capacity strain that may delay shipments and pressure industrial stocks. Labor strain in ports slows freight logistics and industrial supply chains.

## Universe
- XLI

## Data Sources
- Google Trends weekly data for 'port worker overtime'

## Signal Logic
Enter short if weekly search interest rises 30%+ week-over-week

## Entry / Exit
Entry: Enter short if weekly search interest rises 30%+ week-over-week Exit: Exit after 4 weeks or when interest falls below 4-week average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly data for 'port worker overtime' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Port labor issues surface repeatedly due to contract talks and seasonal demand.

## Required Keys
- None
