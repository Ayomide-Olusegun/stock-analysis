import yfinance as yf

def summarise(ticker):
    data = yf.download(ticker, period="1y", auto_adjust=True, progress=False)
    close = data["Close"].squeeze()
    returns = close.pct_change().dropna()
    drawdown = close / close.cummax() - 1
    return {
        "ticker": ticker,
        "total_return": close.iloc[-1] / close.iloc[0] - 1,
        "volatility": returns.std(),
        "max_drawdown": drawdown.min(),
    }

for ticker in ["AAPL", "MSFT", "SPY"]:
    s = summarise(ticker)
    print(f"{s['ticker']:5} return {s['total_return']:7.2%}  daily vol {s['volatility']:.3%}  max drawdown {s['max_drawdown']:.2%}")


    