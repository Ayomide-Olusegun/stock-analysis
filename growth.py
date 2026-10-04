import yfinance as yf
import matplotlib.pyplot as plt

tickers = ["AAPL", "MSFT", "SPY"]
prices = yf.download(tickers, period="1y", auto_adjust=True, progress=False)["Close"]
growth = prices / prices.iloc[0] * 100
growth.plot(figsize=(10, 5), title="Growth of 100 invested")
plt.savefig("growth.png")
print(prices.pct_change().corr().round(2))