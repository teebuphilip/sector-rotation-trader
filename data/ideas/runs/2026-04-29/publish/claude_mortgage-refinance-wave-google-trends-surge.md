# Mortgage Refinance Wave Google Trends Surge

**Idea ID:** `mortgage-refinance-wave-google-trends-surge`
**Family:** `consumer_stress`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When mortgage refinance searches spike, it signals households are actively managing debt stress; subsequent weeks show either housing demand relief (XLY bullish) or wallet tightening (XLP bullish). Successful refinances free up monthly cash flow for discretionary consumer spending.

## Universe
- XLY

## Data Sources
- Google Trends weekly search volume for 'refinance mortgage' via google_trends adapter

## Signal Logic
If weekly Google Trends interest for 'refinance mortgage' spikes 50%+ above 13-week rolling average

## Entry / Exit
Entry: If weekly Google Trends interest for 'refinance mortgage' spikes 50%+ above 13-week rolling average Exit: After 3 weeks or when XLY outperforms SPY by 2% cumulatively

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search volume for 'refinance mortgage' via google_trends adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Refinance search surges occur 2-3 times per quarter when rate expectations shift.

## Required Keys
- None
