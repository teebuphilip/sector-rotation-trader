# Google Gusts

**Idea ID:** `google-gusts`
**Source:** anthropic / claude-3-haiku-20240307
**Frequency:** weekly

## Thesis
Fluctuations in Google search trends can signal shifting consumer and investor interest in various industries. Search trends are a key indicator of digital/tech sector performance.

## Universe
- XLC

## Data Sources
- Google Trends weekly search interest for key industry terms through google_trends adapter

## Signal Logic
If the weekly Google Trends index for a major industry term increases more than 10% from the prior 4-week average

## Entry / Exit
Entry: If the weekly Google Trends index for a major industry term increases more than 10% from the prior 4-week average Exit: After 2 trading weeks or once the index falls back to the prior 4-week average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for key industry terms through google_trends adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Google Trends data exhibits regular weekly patterns, and deviations from typical ranges often occur.

## Required Keys
- None
