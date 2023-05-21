
import time
import pandas as pd
from kafka import KafkaProducer

import yfinance as yf
from datetime import date
import json

current_date = str( date.today())
print(str(current_date))

# Define the list of tickers to fetch and calculate P/E ratios for
# Fetch the list of S&P 500 tickers from Wikipedia
sp500_url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
sp500_data = pd.read_html(sp500_url)
sp500_table = sp500_data[0]
sp500_tickers = sp500_table['Symbol'].tolist()

# Remove any non-alphanumeric characters from the tickers
sp500_tickers = [ticker.replace(".", "-") for ticker in sp500_tickers]

producer = KafkaProducer(bootstrap_servers=['kafka-1:9092'])
# Get the stock data for the S&P 500 tickers from Yahoo Finance

topic_name = 'stocks-demo'
pe_df = pd.DataFrame()
i=0
# Loop through each ticker and fetch its stock data from Yahoo Finance
for ticker in sp500_tickers:
    i =i+1
    if i==2:
        break
    try:
        daily_data = yf.download(ticker, period='1d')
        daily_data['Symbol'] = ticker
        daily_data = daily_data.reset_index(drop=False)
        daily_data['Date'] = daily_data['Date'].dt.strftime('%Y-%m-%d %H:%M:%S')

        if (not  daily_data.empty):
            my_dict = daily_data.iloc[-1].to_dict()

            msg = json.dumps(my_dict)

            producer.send(topic_name, key=b'Stock Update', value=msg.encode())

            print(f"Producing to {topic_name}")

            producer.flush()

        stock_data = yf.download(ticker, period='1y')
        stock_data['Symbol'] = ticker
        # Calculate the P/E ratio
        last_price = stock_data['Adj Close'][-1]
        earnings = stock_data['Adj Close'].rolling(window=365).mean()[-1]
        pe_ratio = last_price / earnings
        """        print(stock_data)
        print('Create a new DataFame with the P/E ratio')
        print(daily_data)"""
        
        data = {
            'ticker': [ticker],
            'last_price': [last_price],
            'earnings': [earnings],
            'pe_ratio': [pe_ratio],
            'Date' : [current_date]
        }

        df = pd.DataFrame(data)
        pe_df = pd.concat([pe_df,df])

        
    except Exception as e:
       # By this way we can know about the type of error occurring
        print("The error is: ",e.with_traceback())
   

print(pe_df)
file_name = "/api/data/stocksValue_"+str(current_date)+".csv"
print(file_name)
pe_df.to_csv(file_name)