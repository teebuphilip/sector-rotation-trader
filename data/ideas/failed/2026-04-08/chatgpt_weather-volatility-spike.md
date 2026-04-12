# Weather Volatility Spike

**Idea ID:** `weather-volatility-spike`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Sudden spikes in weather forecast volatility for major economic hubs can predict short-term market turbulence. By measuring daily changes in weather forecast uncertainty, we can anticipate increased market volatility and adjust trading positions accordingly. This signal exploits the psychological and operational impact of unpredictable weather on supply chains and consumer behavior.

## Universe
- VXX
- UVXY
- SPY
- QQQ

## Data Sources
- NOAA National Weather Service API
- OpenWeatherMap Free API

## Signal Logic
Calculate the daily standard deviation of temperature forecasts over the next 7 days for major economic cities (e.g., New York, London, Tokyo). If the 3-day moving average of this std dev rises by more than 20% compared to the previous week’s average, trigger a volatility spike signal.

## Entry / Exit
Entry (Buy volatility): When a volatility spike signal is triggered, buy VIX-related ETFs or options proxies. Exit (Sell volatility): When the 3-day moving average of forecast volatility drops back below the 7-day average, close the position.

## Position Sizing
Allocate 5% of portfolio per signal, scaling linearly with the magnitude of the volatility spike (e.g., if spike is 40% above baseline, allocate 10%).

## Risks
Weather forecast models can change due to seasonal effects unrelated to market impact. Market volatility may not always correlate with weather unpredictability. False positives during hurricane seasons or extreme weather events may occur.

## Implementation Notes
1. Collect 7-day temperature forecasts daily for selected cities. 2. Compute daily standard deviation of these forecasts. 3. Calculate moving averages and detect spikes. 4. Link signals to volatility ETFs for backtesting. 5. Implement position sizing logic based on spike magnitude.

## Required Keys
- None
