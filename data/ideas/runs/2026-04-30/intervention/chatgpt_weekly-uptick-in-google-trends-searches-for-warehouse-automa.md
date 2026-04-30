# Weekly Uptick In Google Trends Searches For Warehouse Automation Failure Signals Bearish Xli

**Idea ID:** `weekly-uptick-in-google-trends-searches-for-warehouse-automa`
**Family:** `freight_logistics`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising warehouse automation failure interest signals operational hiccups pressuring industrial logistics stocks. Automation failures increase costs and disrupt supply chains, negatively impacting industrials.

## Universe
- XLI

## Data Sources
- Google Trends weekly searches

## Signal Logic
Enter short XLI when weekly search interest rises 25%+ above 6-week rolling average

## Entry / Exit
Entry: Enter short XLI when weekly search interest rises 25%+ above 6-week rolling average Exit: Exit after 4 weeks or if interest falls below baseline

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly searches via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Warehouse automation issues occur regularly and generate search interest spikes.

## Required Keys
- None
