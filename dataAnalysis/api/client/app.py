

import time

from kafka import KafkaProducer

import yfinance as yf

from datetime import date

import json

current_date = date.today()

company = 'TSLA'

producer = KafkaProducer(bootstrap_servers=['kafka-1:9092'])

topic_name = 'stocks-demo'

 

while True:

    data = yf.download("TSLA", period='1d',interval='2m')

    #data = yf.download(tickers=company ,start=current_date,interval='2m')

    data = data.reset_index(drop=False)

    data['Datetime'] = data['Datetime'].dt.strftime('%Y-%m-%d %H:%M:%S')

    my_dict = data.iloc[-1].to_dict()

    msg = json.dumps(my_dict)

    producer.send(topic_name, key=b'Tesla Stock Update', value=msg.encode())

    print(f"Producing to {topic_name}")

    producer.flush()

    time.sleep(120)

