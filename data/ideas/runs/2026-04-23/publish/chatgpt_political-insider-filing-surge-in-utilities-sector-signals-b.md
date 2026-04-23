# Political Insider Filing Surge In Utilities Sector Signals Bearish Xlu

**Idea ID:** `political-insider-filing-surge-in-utilities-sector-signals-b`
**Family:** `political_insider_filing`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Increased insider selling in utilities often signals upcoming sector weakness or regulatory risk. Insider selling precedes sector underperformance due to anticipated headwinds.

## Universe
- XLU

## Data Sources
- Insider trading filings in utilities sector

## Signal Logic
Enter short XLU when insider sell filings exceed 150% of 4-week average

## Entry / Exit
Entry: Enter short XLU when insider sell filings exceed 150% of 4-week average Exit: Exit after 6 weeks or when filings revert below 120%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Insider trading filings in utilities sector via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Insider trading filings vary weekly with ongoing corporate actions.

## Required Keys
- None
