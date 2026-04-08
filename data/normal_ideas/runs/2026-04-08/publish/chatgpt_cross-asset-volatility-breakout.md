# Cross-Asset Volatility Breakout

**Idea ID:** `cross-asset-volatility-breakout`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
This model exploits volatility breakouts across multiple asset classes to capture trend initiations. By identifying when an asset's realized volatility exceeds its historical average, the strategy signals potential strong directional moves. The approach diversifies risk by applying the same logic across equities, commodities, and bonds, aiming to enter positions early in emerging trends.

## Universe
- SPY
- GLD
- TLT
- USO
- EEM

## Data Sources
- yfinance (price data for equities, commodities, bonds)
- FRED (for bond yields and macroeconomic indicators if needed)

## Signal Logic
Calculate 20-day realized volatility (rolling standard deviation of daily returns) and 60-day average realized volatility. A volatility breakout signal occurs when the 20-day volatility exceeds 1.5 times the 60-day average volatility.

## Entry / Exit
Entry: Buy the asset at next open if volatility breakout signal is present and the 5-day momentum (close/close_5days_ago - 1) is positive. Exit: Sell when 20-day volatility falls below 1.2 times the 60-day average volatility or momentum turns negative.

## Position Sizing
Allocate equal dollar amounts to each asset with an active long signal. If multiple signals are active, divide capital equally among them. No leverage used.

## Risks
False volatility spikes can trigger premature entries leading to whipsaws. Low liquidity or gaps can cause slippage. The model may underperform in low volatility or mean-reverting markets.

## Implementation Notes
1) Download daily OHLCV data for universe via yfinance. 2) Calculate daily returns and rolling volatilities (20-day and 60-day). 3) Compute 5-day momentum. 4) Generate signals based on volatility breakout and momentum. 5) Backtest entry and exit rules with daily rebalancing. 6) Track positions and returns accordingly.

## Required Keys
- None
