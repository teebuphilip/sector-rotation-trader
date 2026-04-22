# Political Insider Selling Spike In Financial Sector Etf

**Idea ID:** `political-insider-selling-spike-in-financial-sector-etf`
**Family:** `political_insider_filing`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Surge in insider selling by political figures signals sector-specific risk perception or regulatory fears. Political insiders often have early knowledge on regulatory or economic risks impacting finance.

## Universe
- XLF

## Data Sources
- Public political insider filings aggregated weekly

## Signal Logic
Enter short XLF when insider selling volume spikes more than 30% WoW above 12-week average

## Entry / Exit
Entry: Enter short XLF when insider selling volume spikes more than 30% WoW above 12-week average Exit: Exit after 3 weeks or when selling volume normalizes below 10% above average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Public political insider filings aggregated weekly via scrape (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Weekly insider filings often have clustered selling before major news or market rotations.

## Required Keys
- None
