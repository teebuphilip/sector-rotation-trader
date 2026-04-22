# Weekly Surge In Laborjobs Postings For Renewable Energy Technicians Signals Energy Sector Growth

**Idea ID:** `weekly-surge-in-laborjobs-postings-for-renewable-energy-tech`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Increasing job postings in renewable energy roles reflect sector expansion and investment appetite. Energy sector benefits from growing renewable workforce demand.

## Universe
- XLE

## Data Sources
- Labor jobs postings for renewable energy technicians

## Signal Logic
Entry when weekly job postings rise by more than 15% week-over-week

## Entry / Exit
Entry: Entry when weekly job postings rise by more than 15% week-over-week Exit: Exit after 6 weeks or when postings fall below 5% increase

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Labor jobs postings for renewable energy technicians via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Renewable energy job postings show weekly surges tied to project cycles.

## Required Keys
- None
