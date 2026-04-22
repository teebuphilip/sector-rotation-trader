# Weekly Google Trends Spike For Solar Panel Installation Predicts Energy Sector Momentum

**Idea ID:** `weekly-google-trends-spike-for-solar-panel-installation-pred`
**Family:** `attention_sentiment`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising interest in solar installations indicates accelerating demand for renewable energy products and services. Energy sector benefits from growing renewable installation activity.

## Universe
- XLE

## Data Sources
- Google Trends weekly search interest for 'solar panel installation'

## Signal Logic
Entry when weekly search interest increases by 15% week-over-week

## Entry / Exit
Entry: Entry when weekly search interest increases by 15% week-over-week Exit: Exit when interest falls below 5% week-over-week or after 4 weeks

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'solar panel installation' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Solar installation interest regularly fluctuates with policy and weather events.

## Required Keys
- None
