# Work From Home Frenzy

**Idea ID:** `work-from-home-frenzy`
**Source:** anthropic / claude-3-haiku-20240307
**Frequency:** weekly

## Thesis
Increased interest in remote work tools often indicates changes in workforce trends that can impact technology and services sectors. Consumer discretionary and communication services may benefit from the work-from-home trend.

## Universe
- XLY

## Data Sources
- Google Trends weekly search interest for remote work tools through google_trends adapter

## Signal Logic
If Google Trends search interest for remote work tools rises 30% above the prior 4-week average

## Entry / Exit
Entry: If Google Trends search interest for remote work tools rises 30% above the prior 4-week average Exit: After 3 weeks or when search interest falls below 10% above the prior 4-week average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for remote work tools through google_trends adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Changes in remote work trends often occur quickly in response to economic and social factors.

## Required Keys
- None
