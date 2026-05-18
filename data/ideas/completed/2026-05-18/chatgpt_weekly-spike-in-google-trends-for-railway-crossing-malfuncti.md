# Weekly Spike In Google Trends For Railway Crossing Malfunction Signals Freight Sector Risk

**Idea ID:** `weekly-spike-in-google-trends-for-railway-crossing-malfuncti`
**Family:** `freight_logistics`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
A surge in railway crossing malfunction searches may indicate rising rail transport risks and delays. Rail transport is critical to freight logistics; malfunctions cause operational disruption.

## Universe
- XLI

## Data Sources
- Google Trends weekly search interest for 'railway crossing malfunction'

## Signal Logic
If weekly searches rise by more than 20% over prior 5-week average

## Entry / Exit
Entry: If weekly searches rise by more than 20% over prior 5-week average Exit: Exit after 3 weeks or when interest falls below 10% increase

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'railway crossing malfunction' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Railway issues occur intermittently and generate local news/search attention.

## Required Keys
- None
