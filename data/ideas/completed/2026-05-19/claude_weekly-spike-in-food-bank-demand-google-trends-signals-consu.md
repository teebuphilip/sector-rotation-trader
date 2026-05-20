# Weekly Spike In Food Bank Demand Google Trends Signals Consumer Staples Demand Surge

**Idea ID:** `weekly-spike-in-food-bank-demand-google-trends-signals-consu`
**Family:** `consumer_stress`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Food bank search interest spikes when unemployment rises or benefit cliffs hit; trailing indicator of demand for value-priced staples; signals XLP sector support. Increased food bank searches correlate with higher staples consumption and discount retailer foot traffic.

## Universe
- XLP

## Data Sources
- Google Trends weekly search volume for 'food bank near me' OR 'food assistance' through google_trends adapter

## Signal Logic
When weekly search volume exceeds 70th percentile of 52-week rolling average

## Entry / Exit
Entry: When weekly search volume exceeds 70th percentile of 52-week rolling average Exit: When search volume drops below 55th percentile for 2 consecutive weeks or after 14 days

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search volume for 'food bank near me' OR 'food assistance' through google_trends adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Benefit payment cycles and seasonal unemployment create predictable search patterns every 2-3 weeks.

## Required Keys
- None
