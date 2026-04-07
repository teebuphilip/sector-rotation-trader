# ============================================================
# SECTOR ROTATION TRADER — CONFIG
# ============================================================

# Capital
STARTING_CASH        = 100_000.0   # base portfolio cash
MAX_POSITION_SIZE    = 10_000.0    # max $ per trade
MAX_BORROW           = 100_000.0   # max margin borrowing allowed
BORROW_RATE_ANNUAL   = 0.085       # 8.5% annual margin rate (daily accrual)

# Sector ETFs (11 SPDR sectors)
SECTOR_ETFS = ['XLK','XLV','XLF','XLY','XLI','XLC','XLP','XLE','XLB','XLRE','XLU']

# Sector rotation signal
PERF_SHORT_DAYS = 63    # ~3 months
PERF_LONG_DAYS  = 126   # ~6 months

# Entry signals (all 3 must fire)
BREAKOUT_LOOKBACK    = 10    # price closes above N-day high
VOLUME_MULT          = 1.5   # volume must be >= 150% of 20-day avg
VOLUME_AVG_DAYS      = 20
BB_PERIOD            = 20    # Bollinger Band period
BB_STD               = 2.0   # Bollinger Band std devs

# Exit signal
EXIT_MA_PERIOD       = 20    # 20-day MA
EXIT_CONSEC_DAYS     = 2     # N consecutive closes below MA triggers exit

# Risk management
STOP_LOSS_PCT        = 0.08  # 8% hard stop-loss per position
MAX_DRAWDOWN_PCT     = 0.15  # 15% portfolio drawdown — pause new entries
MAX_POSITIONS_PER_SECTOR = 5 # max open positions in the same sector

# Simulation window
SEED_DAYS            = 90    # historical days to seed state on first run
SIM_MONTHS           = 6     # total simulation duration

# Data
DATA_PERIOD          = "1y"  # yfinance download window

# Paths
STATE_FILE           = "state.json"
DASHBOARD_FILE       = "docs/index.html"
LOG_FILE             = "docs/trades.json"
