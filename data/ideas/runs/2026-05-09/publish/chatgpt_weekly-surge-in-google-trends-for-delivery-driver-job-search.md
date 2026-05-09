# Weekly Surge In Google Trends For Delivery Driver Job Searches Signals Labor Tightness Benefiting Industrials

**Idea ID:** `weekly-surge-in-google-trends-for-delivery-driver-job-search`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
An uptick in searches for delivery driver jobs indicates rising labor demand or shortages in logistics roles, often preceding increased freight and delivery costs. Industrial sector firms benefit from higher freight demand and pricing power amid labor tightness.

## Universe
- XLI

## Data Sources
- Google Trends weekly search interest

## Signal Logic
Enter long if delivery driver job search interest increases by more than 15% week-over-week

## Entry / Exit
Entry: Enter long if delivery driver job search interest increases by more than 15% week-over-week Exit: Exit after 3 weeks or if search interest declines 10% from peak

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Weekly labor demand shifts are common with seasonal and economic changes, producing multiple signals annually.

## Required Keys
- None
