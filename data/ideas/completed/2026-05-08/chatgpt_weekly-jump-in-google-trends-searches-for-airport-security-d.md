# Weekly Jump In Google Trends Searches For Airport Security Delay Signals Travel Mobility Disruptions

**Idea ID:** `weekly-jump-in-google-trends-searches-for-airport-security-d`
**Family:** `travel_mobility`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising searches for airport security delays indicate growing travel friction that may reduce air travel demand. Travel and leisure sectors suffer when mobility bottlenecks increase consumer friction.

## Universe
- XLY

## Data Sources
- Google Trends weekly search interest

## Signal Logic
If weekly searches rise 20% above 4-week average

## Entry / Exit
Entry: If weekly searches rise 20% above 4-week average Exit: When searches decline below 10% above 4-week average

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
- Why It Should Fire Soon: Travel bottlenecks fluctuate regularly with seasonal travel and regulatory changes.

## Required Keys
- None
