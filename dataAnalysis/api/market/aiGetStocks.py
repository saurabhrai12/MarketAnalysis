from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent))

import pandas_datareader.data as web
#import psycopg2
from sqlalchemy import create_engine
import pandas as pd
import configparser
import yfinance as yf
import utils.dataBase_Connection as  db

# Define the database connection details
config = configparser.ConfigParser()
config.read("config.ini")
db_config = config["postgresql"]

# Define the list of tickers to fetch and calculate P/E ratios for
# Fetch the list of S&P 500 tickers from Wikipedia
sp500_url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
sp500_data = pd.read_html(sp500_url)
sp500_table = sp500_data[0]
sp500_tickers = sp500_table['Symbol'].tolist()

# Remove any non-alphanumeric characters from the tickers
sp500_tickers = [ticker.replace(".", "-") for ticker in sp500_tickers]

# Get the stock data for the S&P 500 tickers from Yahoo Finance
start_date = "1995-01-01"
end_date = "2023-05-13"

# Connect to the database using SqlAchemy
engine = create_engine(f"postgresql://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}")
    

# Loop through each ticker and fetch its stock data from Yahoo Finance
for ticker in sp500_tickers:
    # Fetch the stock data
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    stock_data['Symbol'] = ticker
    # Calculate the P/E ratio
    last_price = stock_data['Adj Close'][-1]
    earnings = stock_data['Adj Close'].rolling(window=365).mean()[-1]
    pe_ratio = last_price / earnings

    # Create a new DataFrame with the P/E ratio
    data = {
        'ticker': [ticker],
        'last_price': [last_price],
        'earnings': [earnings],
        'pe_ratio': [pe_ratio]
    }

    df = pd.DataFrame(data)
    print(ticker)
    # Insert the DataFrame into the database using sqlalchemy
    stock_data.to_sql('stock_price_data', engine, if_exists='append')
    stock_data.to_csv('C:\\Users\\saura\\OneDrive\\Documents\\workspace\\MarketAnalysis\\data\\stock_price_data\\' +ticker+ ".csv")

    df.to_sql('hist_stock_data', engine, if_exists='append', index=False)
    df.to_csv('C:\\Users\\saura\\OneDrive\\Documents\\workspace\\MarketAnalysis\\data\\hist_stock_data\\' +ticker+ ".csv")
# Close the database connection

