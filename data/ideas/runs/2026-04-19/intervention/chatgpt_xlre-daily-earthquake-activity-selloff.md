# Xlre Daily Earthquake Activity Selloff

**Idea ID:** `xlre-daily-earthquake-activity-selloff`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Increased local earthquake events tend to temporarily pressure real estate ETFs in affected regions. Real estate valuations are sensitive to perceived natural disaster risks.

## Universe
- XLRE

## Data Sources
- USGS daily earthquake activity counts near US urban centers

## Signal Logic
Enter short if daily earthquake counts in top 5 US metro areas exceed prior 7-day average by 200%

## Entry / Exit
Entry: Enter short if daily earthquake counts in top 5 US metro areas exceed prior 7-day average by 200% Exit: Exit after 5 trading days or if earthquake activity normalizes

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use USGS daily earthquake activity counts near US urban centers via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Earthquake clusters can happen irregularly but often multiple times a year.

## Required Keys
- None
