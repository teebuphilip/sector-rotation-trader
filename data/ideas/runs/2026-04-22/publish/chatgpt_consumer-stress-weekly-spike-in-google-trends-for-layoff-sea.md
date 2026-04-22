# Consumer Stress Weekly Spike In Google Trends For Layoff Searches During Non-peak Seasons

**Idea ID:** `consumer-stress-weekly-spike-in-google-trends-for-layoff-sea`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising layoff search interest signals rising fear of unemployment, pressuring consumer discretionary stocks. Layoff concerns reduce consumer spending appetite.

## Universe
- XLY

## Data Sources
- Google Trends weekly search interest for 'layoff'

## Signal Logic
Enter short XLY if weekly 'layoff' search interest jumps 20% above 6-week average outside typical seasonal peaks

## Entry / Exit
Entry: Enter short XLY if weekly 'layoff' search interest jumps 20% above 6-week average outside typical seasonal peaks Exit: Exit after 4 weeks or if interest declines below 10% above average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'layoff' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Layoff search interest fluctuates frequently with economic news cycles.

## Required Keys
- None
