import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Download de dados
tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA']
data = yf.download(tickers, start='2023-01-01', end='2024-12-31')['Close']

# Retornos diários
returns = data.pct_change().dropna()

# Retorno acumulado
cumulative = (1 + returns).cumprod()

# Gráfico
cumulative.plot(figsize=(12, 6), title='Retorno Acumulado 2023-2024')
plt.ylabel('Retorno Acumulado')
plt.grid(True)
plt.show()

print(returns.describe())