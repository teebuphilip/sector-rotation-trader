# Daily Surge In Rss Counts For Labor Union Strike Mentions Signals Bearish Financials

**Idea ID:** `daily-surge-in-rss-counts-for-labor-union-strike-mentions-si`
**Family:** `political_insider_filing`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Spike in labor strike mentions increases perceived business risk and credit risk, pressuring financial sector stocks. Labor disruptions raise operational risk and credit costs for financial institutions.

## Universe
- XLF

## Data Sources
- RSS news feed counts for labor union strike mentions

## Signal Logic
Enter short on XLF if daily RSS count for 'labor strike' mentions doubles compared to 10-day average

## Entry / Exit
Entry: Enter short on XLF if daily RSS count for 'labor strike' mentions doubles compared to 10-day average Exit: Exit after 5 trading days or when mention volume drops below average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS news feed counts for labor union strike mentions via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Labor disputes and strikes regularly generate news spikes.

## Required Keys
- None
