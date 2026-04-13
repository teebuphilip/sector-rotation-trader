# Weather Derivative Momentum

**Idea ID:** `weather-derivative-momentum`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Certain commodities and sectors are highly sensitive to short-term regional weather anomalies. By tracking daily deviations in temperature and precipitation from historical averages in key agricultural and energy-producing regions, we can generate momentum signals predicting commodity price moves. This approach exploits the lag between weather impacts and market price adjustments.

## Universe
- CORN
- WHEAT
- SOYBEAN
- WTI_OIL
- NGAS

## Data Sources
- NOAA Climate Data Online (CDO)
- USDA Crop Progress Reports
- EIA Weekly Petroleum Status Report

## Signal Logic
Calculate daily temperature and precipitation anomalies for major commodity-producing regions (e.g., Midwest US for corn, Texas for oil). If a 3-day moving average anomaly exceeds +2 standard deviations for temperature or precipitation, generate a momentum signal favoring bullish exposure to that commodity. Conversely, anomalies below -2 standard deviations generate bearish signals.

## Entry / Exit
Enter long positions when anomaly > +2 SD sustained for 3 days; exit when anomaly returns within ±1 SD. Enter short positions when anomaly < -2 SD sustained for 3 days; exit when anomaly returns within ±1 SD.

## Position Sizing
Allocate 5-10% of portfolio per position, scaled by the magnitude of the anomaly (e.g., 2 SD = 5%, 3 SD = 10%). Limit total exposure to 20% to manage risk.

## Risks
Weather anomalies may not always translate to price moves due to inventory buffers or market expectations. False signals can occur during seasonal transitions. Sudden policy changes or supply shocks unrelated to weather can invalidate signals.

## Implementation Notes
1) Obtain historical daily temperature and precipitation data from NOAA for target regions. 2) Calculate anomalies vs. 10-year daily averages. 3) Compute moving averages and standard deviations. 4) Map anomalies to commodities based on regional relevance. 5) Fetch commodity price data for signal validation. 6) Backtest signal logic on historical data.

## Required Keys
- None
