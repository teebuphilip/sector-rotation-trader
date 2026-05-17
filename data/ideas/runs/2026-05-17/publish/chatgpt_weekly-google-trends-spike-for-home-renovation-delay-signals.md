# Weekly Google Trends Spike For Home Renovation Delay Signals Local Economy Strain

**Idea ID:** `weekly-google-trends-spike-for-home-renovation-delay-signals`
**Family:** `local_economy_weirdness`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Increasing searches for renovation delays reflect localized supply or labor shortages affecting construction. Materials sector demand is pressured when homebuilding and renovations stall.

## Universe
- XLB

## Data Sources
- Google Trends weekly search interest for 'home renovation delay'

## Signal Logic
Enter short XLB if weekly Google Trends for 'home renovation delay' rises 30%+ WoW

## Entry / Exit
Entry: Enter short XLB if weekly Google Trends for 'home renovation delay' rises 30%+ WoW Exit: Exit after 5 weeks or if trend declines below 15% WoW increase

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'home renovation delay' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Home renovation interest fluctuates with local supply issues and seasonal cycles.

## Required Keys
- None
