# Xle Weekly Drawdown Rebound Signal

**Idea ID:** `xle-weekly-drawdown-rebound-signal`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
After a weekly drawdown exceeding 5%, XLE often rebounds sharply the following week as energy prices stabilize. Energy sector is mean reverting after sharp short-term pullbacks.

## Universe
- XLE

## Data Sources
- Yahoo Finance weekly closing prices for XLE

## Signal Logic
Enter long on weekly close if weekly drawdown is greater than 5% from prior week's close

## Entry / Exit
Entry: Enter long on weekly close if weekly drawdown is greater than 5% from prior week's close Exit: Exit after 2 weeks or if weekly gain turns negative

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Yahoo Finance weekly closing prices for XLE via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 36
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Weekly drawdowns >5% in XLE occur multiple times a year, triggering timely rebound trades.

## Required Keys
- None
