# Weekly Surge In Political Insider Selling Filings Signals Bearish Xlf

**Idea ID:** `weekly-surge-in-political-insider-selling-filings-signals-be`
**Family:** `political_insider_filing`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Increased insider selling among financial sector political figures suggests upcoming negative sentiment or regulation. Political insider selling often precedes sector underperformance due to regulatory risk.

## Universe
- XLF

## Data Sources
- Political insider trading filings weekly aggregated

## Signal Logic
Enter short XLF if weekly insider selling volume spikes 40% above 12-week average

## Entry / Exit
Entry: Enter short XLF if weekly insider selling volume spikes 40% above 12-week average Exit: Exit after 6 weeks or when insider selling subsides below 15% above average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Political insider trading filings weekly aggregated via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Political insider activity cycles with legislative and earnings calendar.

## Required Keys
- None
