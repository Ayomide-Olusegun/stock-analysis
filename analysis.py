import yfinance as yf
import matplotlib.pyplot as plt

data = yf.download("AAPL", period="1y", auto_adjust=True)
close = data["Close"].squeeze()
returns = close.pct_change().dropna()

print(f"Days of data: {len(close)}")
print(f"Average daily return: {returns.mean():.3%}")
print(f"Daily volatility: {returns.std():.3%}")
print(f"Total return: {close.iloc[-1] / close.iloc[0] - 1:.2%}")

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 7), sharex=True)
ax1.plot(close)
ax1.set_title("AAPL closing price")
ax2.plot(returns)
ax2.set_title("Daily returns")
plt.tight_layout()
plt.savefig("aapl.png")
print("Saved chart to aapl.png")

running_max = close.cummax()
drawdown = close / running_max - 1
print(f"Max drawdown: {drawdown.min():.2%}")

fig2, (ax3, ax4, ax5) = plt.subplots(3, 1, figsize=(10, 9))
ax3.hist(returns, bins=40)
ax3.set_title("Distribution of daily returns")
ax4.plot(returns.rolling(30).std())
ax4.set_title("30-day rolling volatility")
ax5.plot(drawdown)
ax5.set_title("Drawdown from previous peak")
plt.tight_layout()
plt.savefig("aapl_risk.png")