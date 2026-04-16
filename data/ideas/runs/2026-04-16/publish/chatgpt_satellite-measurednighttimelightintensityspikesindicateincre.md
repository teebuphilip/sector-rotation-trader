# Satellite-measurednighttimelightintensityspikesindicateincreasedtechdatacenteractivity

**Idea ID:** `satellite-measurednighttimelightintensityspikesindicateincre`
**Source:**  / 
**Frequency:** daily

## Thesis
Sudden increases in nighttime light emissions from known data center locations suggest heightened cloud computing demand. XLK includes major cloud and data center operators whose revenues correlate with data usage intensity.

## Universe
- XLK

## Data Sources
- NASA Black Marble Nighttime Lights API

## Signal Logic
If 3-day average nighttime light intensity in data center regions rises >10% vs prior month average

## Entry / Exit
Entry: If 3-day average nighttime light intensity in data center regions rises >10% vs prior month average Exit: After 7 trading days or if intensity falls below prior month average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use NASA Black Marble Nighttime Lights API via api (daily).

## Required Keys
- None
