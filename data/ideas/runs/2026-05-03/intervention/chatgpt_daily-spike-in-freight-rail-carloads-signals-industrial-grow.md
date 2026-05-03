# Daily Spike In Freight Rail Carloads Signals Industrial Growth Pressure

**Idea ID:** `daily-spike-in-freight-rail-carloads-signals-industrial-grow`
**Family:** `freight_logistics`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
A sharp daily increase in freight rail carloads indicates rising industrial activity and supply chain demand pressure. Industrial sector benefits directly from freight volume expansions.

## Universe
- XLI

## Data Sources
- Federal Railroad Administration daily freight carloads

## Signal Logic
Enter long XLI if daily rail carloads increase 5% over 5-day moving average

## Entry / Exit
Entry: Enter long XLI if daily rail carloads increase 5% over 5-day moving average Exit: Exit after 7 trading days or if carloads revert below 5-day average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Federal Railroad Administration daily freight carloads via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Freight volumes vary frequently with industrial activity and often show bursts around economic data releases.

## Required Keys
- None
