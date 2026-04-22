# Grocery Store Foot Traffic Collapse Signal

**Idea ID:** `grocery-store-foot-traffic-collapse-signal`
**Family:** `consumer_stress`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Spikes in grocery delivery and food bank searches often precede consumer spending contractions and indicate financial strain or shift to online shopping channels. Consumer discretionary retail faces headwinds when food insecurity searches spike; signals demand destruction in consumer staples and discretionary spending.

## Universe
- XLY

## Data Sources
- Google Trends weekly search volume for 'grocery delivery' and 'food bank near me' through google_trends adapter

## Signal Logic
When 'grocery delivery' + 'food bank' combined search interest exceeds 75th percentile of 52-week rolling average

## Entry / Exit
Entry: When 'grocery delivery' + 'food bank' combined search interest exceeds 75th percentile of 52-week rolling average Exit: After 10 trading days or when combined search interest falls below 50th percentile

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search volume for 'grocery delivery' and 'food bank near me' through google_trends adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Consumer stress proxies fire monthly; grocery delivery searches spike during economic uncertainty windows which recur seasonally and cyclically.

## Required Keys
- None
