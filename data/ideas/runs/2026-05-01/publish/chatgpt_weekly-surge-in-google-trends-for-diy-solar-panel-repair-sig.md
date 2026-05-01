# Weekly Surge In Google Trends For Diy Solar Panel Repair Signals Green Energy Sector Rebound

**Idea ID:** `weekly-surge-in-google-trends-for-diy-solar-panel-repair-sig`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising searches for solar panel repairs suggest rising maintenance demand as consumers hold on to their green energy assets, signaling potential sector strength. Sustained interest in renewable energy maintenance indicates durable consumer investment in the energy sector.

## Universe
- XLE

## Data Sources
- Google Trends weekly search interest

## Signal Logic
Enter long XLE when 2-week average search volume for 'DIY solar panel repair' rises 20% above 10-week average

## Entry / Exit
Entry: Enter long XLE when 2-week average search volume for 'DIY solar panel repair' rises 20% above 10-week average Exit: Exit after 6 weeks or when the search volume falls below the 10-week average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Consumer interest in solar repairs spikes frequently due to seasonal maintenance cycles.

## Required Keys
- None
