# Weekly Surge In Google Trends For Diy Plumbing Repair Signals Consumer Stress Rebound

**Idea ID:** `weekly-surge-in-google-trends-for-diy-plumbing-repair-signal`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
An uptick in DIY plumbing repair searches indicates rising household maintenance stress, often preceding increased discretionary spending on home goods. Consumer discretionary benefits as stressed consumers invest in home repairs and upgrades.

## Universe
- XLY

## Data Sources
- Google Trends weekly search interest

## Signal Logic
Enter long XLY if weekly Google Trends index for 'DIY plumbing repair' rises 15% week-over-week

## Entry / Exit
Entry: Enter long XLY if weekly Google Trends index for 'DIY plumbing repair' rises 15% week-over-week Exit: Exit after 3 weeks or if index drops 10% week-over-week

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Weekly search interest for home repair topics fluctuates regularly with seasonal and stress-driven spikes.

## Required Keys
- None
