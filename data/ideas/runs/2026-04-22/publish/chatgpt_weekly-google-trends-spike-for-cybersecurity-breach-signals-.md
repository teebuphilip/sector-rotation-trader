# Weekly Google Trends Spike For Cybersecurity Breach Signals Technology Sector Risk Aversion

**Idea ID:** `weekly-google-trends-spike-for-cybersecurity-breach-signals-`
**Family:** `attention_sentiment`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising attention to cybersecurity breaches increases risk aversion, pressuring technology sector valuations. Tech sector faces risk from security concerns impacting sentiment and investment.

## Universe
- XLK

## Data Sources
- Google Trends weekly search interest for 'cybersecurity breach'

## Signal Logic
Entry when weekly search interest rises by more than 20% week-over-week

## Entry / Exit
Entry: Entry when weekly search interest rises by more than 20% week-over-week Exit: Exit when interest drops below 10% increase or after 6 weeks

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'cybersecurity breach' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Cybersecurity breach news causes regular search interest spikes.

## Required Keys
- None
