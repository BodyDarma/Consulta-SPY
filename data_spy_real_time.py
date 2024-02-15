import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Definindo o ticker onde desejamos coletar os dados
ticker = "SPY"

# Coletando dados do último mês
dados_spy = yf.download(ticker, period="1mo")

# Limpeza de dados: neste caso, vamos apenas remover possíveis valores faltantes
dados_spy.dropna(inplace=True)

# Plotando os dados
# Estamos interessados principalmente no preço de fechamento ajustado
dados_spy['Adj Close'].plot(title=f"Preço de fechamento ajustado do {ticker} - último mês", figsize=(10, 6))

plt.xlabel("Data")
plt.ylabel("Preço de fechamento ajustado (USD)")
plt.show()
