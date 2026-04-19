# Global Tech Earnings Momentum

**Idea ID:** `global-tech-earnings-momentum`
**Source:** anthropic / claude-3-haiku-20240307
**Frequency:** weekly

## Thesis
Investors often search for info on tech earnings reports ahead of the announcements, creating predictable trading patterns. Tech sector is highly sensitive to earnings sentiment.

## Universe
- XLK

## Data Sources
- Google Trends weekly search interest for tech company earnings reports through google_trends adapter

## Signal Logic
If Google Trends search interest for tech earnings reports rises 20% above the prior 4-week average

## Entry / Exit
Entry: If Google Trends search interest for tech earnings reports rises 20% above the prior 4-week average Exit: After 2 weeks or when search interest falls below 10% above the prior 4-week average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for tech company earnings reports through google_trends adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Tech earnings season is a regular quarterly event with high investor interest and market volatility.

## Required Keys
- None
