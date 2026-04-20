# Energy Sector Weekly Drawdown Exhaustion

**Idea ID:** `energy-sector-weekly-drawdown-exhaustion`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
After a 3-week consecutive decline totaling more than 8%, a reversal week with a smaller loss or gain often signals short-term bottoming. Energy sector tends to mean revert after sharp multi-week declines.

## Universe
- XLE

## Data Sources
- Yahoo Finance weekly prices for XLE

## Signal Logic
Enter long if XLE drops 3 consecutive weeks totaling >8% and then weekly loss is <2% or positive

## Entry / Exit
Entry: Enter long if XLE drops 3 consecutive weeks totaling >8% and then weekly loss is <2% or positive Exit: Exit after 4 weeks or a 5% gain is realized

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Yahoo Finance weekly prices for XLE via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 36
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Energy volatility and drawdowns are common, creating regular opportunities for this pattern.

## Required Keys
- None
