import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

# Get gold futures data from Yahoo Finance
gold = yf.download('GC=F', start='2019-01-01', end='2022-03-21')

# Calculate the 20-day moving average
gold['20-day'] = gold['Close'].rolling(window=20).mean()

# Calculate the 50-day moving average
gold['50-day'] = gold['Close'].rolling(window=50).mean()

# Calculate the 200-day moving average
gold['200-day'] = gold['Close'].rolling(window=200).mean()

# Plot the gold futures prices and moving averages
plt.figure(figsize=(12,6))
plt.plot(gold['Close'])
plt.plot(gold['20-day'])
plt.plot(gold['50-day'])
plt.plot(gold['200-day'])
plt.legend(['Gold Futures', '20-day MA', '50-day MA', '200-day MA'])
plt.title('Gold Futures Prices and Moving Averages')
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()

# Calculate the z-score for the 20-day moving average
gold['20-day z-score'] = (gold['Close'] - gold['20-day']) / np.std(gold['Close'] - gold['20-day'])

# Plot the z-score for the 20-day moving average
plt.figure(figsize=(12,6))
plt.plot(gold['20-day z-score'])
plt.axhline(y=0, color='red', linestyle='-')
plt.axhline(y=1, color='gray', linestyle='--')
plt.axhline(y=-1, color='gray', linestyle='--')
plt.title('Gold Futures 20-day Moving Average Z-Score')
plt.xlabel('Date')
plt.ylabel('Z-Score')
plt.show()
