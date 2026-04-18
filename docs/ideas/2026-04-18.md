# Satelliteimageryofnighttimelightsoversemiconductorfabricationplantscorrelateswithupcomingsupplychainbottlenecks

**Idea ID:** `satelliteimageryofnighttimelightsoversemiconductorfabricatio`
**Source:**  / 
**Frequency:** weekly

## Thesis
A sudden dimming of nighttime lights at major chip fabs indicates reduced production activity, forecasting supply constraints. Reduced chip supply drives up prices and benefits technology sector earnings.

## Universe
- XLK

## Data Sources
- NASA Black Marble nighttime lights dataset

## Signal Logic
If normalized light intensity drops >10% week-over-week at top fabs

## Entry / Exit
Entry: If normalized light intensity drops >10% week-over-week at top fabs Exit: After 15 trading days or when light intensity recovers by 5%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use NASA Black Marble nighttime lights dataset via api (weekly).

## Required Keys
- None
