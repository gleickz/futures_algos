import yfinance as yf

# Define the ticker symbol for gold futures
symbol = "GC=F"

# Retrieve historical data for gold futures
data = yf.download(symbol, start="2021-01-01", end="2023-03-20")

# Define the moving average window sizes for the mean reversion strategy
short_window = 20
long_window = 50

# Compute the moving averages
data["short_mavg"] = data["Close"].rolling(window=short_window, min_periods=1).mean()
data["long_mavg"] = data["Close"].rolling(window=long_window, min_periods=1).mean()

# Define the signals for the mean reversion strategy
data["signal"] = 0.0
data["signal"][short_window:] = np.where(data["short_mavg"][short_window:] > data["long_mavg"][short_window:], 1.0, -1.0)

# Compute the returns for the strategy
data["returns"] = data["Close"].pct_change() * data["signal"].shift(1)

# Compute the cumulative returns for the strategy
data["cum_returns"] = (1.0 + data["returns"]).cumprod()

# Plot the results
import matplotlib.pyplot as plt

plt.figure(figsize=(12,8))
plt.plot(data["cum_returns"])
plt.title("Mean Reversion Trading Strategy for Gold Futures")
plt.xlabel("Date")
plt.ylabel("Cumulative Returns")
plt.show()
