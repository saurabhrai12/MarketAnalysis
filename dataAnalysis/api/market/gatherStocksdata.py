import pandas_datareader.data as web
import yfinance as yf
import pandas as pd

# Fetch the list of S&P 500 tickers from Wikipedia
sp500_url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
sp500_data = pd.read_html(sp500_url)
sp500_table = sp500_data[0]
sp500_tickers = sp500_table['Symbol'].tolist()

# Remove any non-alphanumeric characters from the tickers
sp500_tickers = [ticker.replace(".", "-") for ticker in sp500_tickers]

# Get the stock data for the S&P 500 tickers from Yahoo Finance
start_date = "2010-01-01"
end_date = "2023-12-31"
#sp500_data = web.DataReader(sp500_tickers, 'yahoo', start_date, end_date)

# Print the data for the first five tickers
for ticker in sp500_tickers[:5]:
    print(ticker)
    # Fetch the stock data for a company
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    #stock_data = yf.(symbols=ticker, start=start_date, end=end_date)

    # Calculate the daily returns
    daily_returns = stock_data['Adj Close'].pct_change()

    # Calculate the monthly returns
    monthly_returns = stock_data['Adj Close'].resample('M').ffill().pct_change()

    # Calculate the annual returns
    annual_returns = stock_data['Adj Close'].resample('Y').ffill().pct_change()
    latest_price = yf.Ticker(ticker).info["regularMarketPrice"]
    latest_eps = yf.Ticker(ticker).info["trailingEps"]
    pe_ratio = latest_price / latest_eps

    print(f"The latest price for {ticker} is {latest_price:.2f} USD.")
    print(f"The latest EPS for {ticker} is {latest_eps:.2f} USD.")
    print(f"The P/E ratio for {ticker} is {pe_ratio:.2f}.")

    # Print the first five rows of each returns series
    print("Daily returns:")
    print(daily_returns.head())
    print("\nMonthly returns:")
    print(monthly_returns.head())
    print("\nAnnual returns:")
    print(annual_returns.head())



# Fetch the stock data for a company

# Calculate the P/E ratio
