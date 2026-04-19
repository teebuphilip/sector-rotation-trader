# Financial Sector Weekly Drawdown Bounce

**Idea ID:** `financial-sector-weekly-drawdown-bounce`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
After a weekly drawdown exceeding 4%, XLF often experiences a short-term rebound the following week. Banks and finance stocks tend to mean revert after sharp weekly declines.

## Universe
- XLF

## Data Sources
- Yahoo Finance weekly prices for XLF via price_only adapter

## Signal Logic
If XLF weekly return < -4%, enter long next week

## Entry / Exit
Entry: If XLF weekly return < -4%, enter long next week Exit: After 2 weeks or 3% gain

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Yahoo Finance weekly prices for XLF via price_only adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 36
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Weekly declines >4% happen multiple times annually in financials.

## Required Keys
- None
