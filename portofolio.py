import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Download historical data
tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA']
data = yf.download(tickers, start='2023-01-01', end='2024-12-31')['Close']

# Daily returns
returns = data.pct_change().dropna()

# Cumulative returns
cumulative = (1 + returns).cumprod()

# Plot
cumulative.plot(figsize=(12, 6), title='Cumulative Returns 2023-2024')
plt.ylabel('Cumulative Return')
plt.grid(True)
plt.show()

print(returns.describe())
