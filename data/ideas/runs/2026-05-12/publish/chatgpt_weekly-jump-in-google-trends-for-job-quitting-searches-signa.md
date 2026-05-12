# Weekly Jump In Google Trends For Job Quitting Searches Signals Labor Market Tightness Benefiting Financial Sector

**Idea ID:** `weekly-jump-in-google-trends-for-job-quitting-searches-signa`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Increased interest in quitting jobs indicates labor market tightness and wage inflation expectations, often followed by increased borrowing and financial activity. Banks and financial companies benefit from higher loan demand and rising interest rate environments tied to strong labor markets.

## Universe
- XLF

## Data Sources
- Google Trends weekly search interest for job quitting and resignations

## Signal Logic
Enter long XLF when weekly Google Trends for job quitting rises 15%+ over previous week

## Entry / Exit
Entry: Enter long XLF when weekly Google Trends for job quitting rises 15%+ over previous week Exit: Exit after 6 weeks or when search interest declines below 5% above baseline

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for job quitting and resignations via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Labor market sentiment shifts reflected in searches happen frequently, especially near seasonal cycles.

## Required Keys
- None
