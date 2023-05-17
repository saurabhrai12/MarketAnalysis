# We'll start by importing the DAG object
from datetime import timedelta, datetime
from pathlib import Path
from sqlalchemy import create_engine
from airflow import DAG
# We need to import the operators used in our tasks
from airflow.operators.python_operator import PythonOperator
from airflow.operators.postgres_operator import PostgresOperator
# We then import the days_ago function
from airflow.utils.dates import days_ago
import psycopg2
import pandas as pd

import os

# get dag directory path
dag_path = os.getcwd()
print('Current working dir +++++++++++++++' + dag_path)

def execution_date_to_millis(execution_date):
    """converts execution date (in DAG timezone) to epoch millis

    Args:
        date (execution date): %Y-%m-%d

    Returns:
        milliseconds
    """
    date = datetime.strptime(execution_date, "%Y-%m-%d")
    epoch = datetime.utcfromtimestamp(0)
    return (date - epoch).total_seconds() * 1000.0


def transform_data():
    try:

        print(dag_path)
        booking = pd.read_csv(f"{dag_path}/data/order_details.csv", low_memory=False)
        client = pd.read_csv(f"{dag_path}/data/customer.csv", low_memory=False)
        #hotel = pd.read_csv(f"{dag_path}/data/invoices.csv", low_memory=False)
        print('read from file')
        # merge booking with client
        data = pd.merge(booking, client, on='id')
        #data.rename(columns={'name': 'client_name', 'type': 'client_type'}, inplace=True)
        '''
        # merge booking, client & hotel
        data = pd.merge(data, hotel, on='hotel_id')
        data.rename(columns={'name': 'hotel_name'}, inplace=True)

        # make date format consistent
        data.booking_date = pd.to_datetime(data.booking_date, infer_datetime_format=True)

        # make all cost in GBP currency
        data.loc[data.currency == 'EUR', ['booking_cost']] = data.booking_cost * 0.8
        data.currency.replace("EUR", "GBP", inplace=True)

        # remove unnecessary columns
        data = data.drop('address', 1)
        '''
        # load processed data
        output_dir = Path(f'{dag_path}/processed_data/')
        output_dir.mkdir(parents=True, exist_ok=True)
        # processed_data/2021-08-15/12/2021-08-15_12.csv
        data.to_csv(f"{dag_path}/processed_data/processed_data.csv", index=False)

    except ValueError as e:
        print("datetime format should match %Y-%m-%d %H", e)
        raise e


def load_data():

    #establishing the connection
    
    #Creating a cursor object using the cursor() method

    """conn = psycopg2.connect("postgresql://airflow:airflow@postgres/Northwind")
    conn.autocommit = True
    c = conn.cursor()
    c.execute('''
                CREATE TABLE IF NOT EXISTS booking_record (
                    client_id integer NOT NULL,
                    booking_date text NOT NULL,
                    room_type text NOT NULL,
                    hotel_id integer NOT NULL,
                    booking_cost double precision,
                    currency text,
                    age integer,
                    client_name text,
                    client_type text,
                    hotel_name text
                );''')
    #processed_file = f"{dag_path}/processed_data/{file_date_path}/{file_date_path.replace('/', '_')}.csv"
    conn.close()"""
    records = pd.read_csv(f"{dag_path}/processed_data/processed_data.csv")
    engine = create_engine('postgresql+psycopg2://airflow:airflow@postgres/Northwind')
    records.to_sql('booking', engine, index=False, if_exists='append')
    

# initializing the default arguments that we'll pass to our DAG
default_args = {
    'owner': 'airflow',
    'start_date': days_ago(5)
}

ingestion_dag = DAG(
    'booking_ingestion',
    default_args=default_args,
    description='Aggregates booking records for data analysis',
    schedule_interval=timedelta(hours=1),
    catchup=False
)

task_1 = PythonOperator(
    task_id='transform_data',
    python_callable=transform_data,
    dag=ingestion_dag,
)
"""create_table = PostgresOperator(
    task_id="create_pet_table",
    sql = '''
                CREATE TABLE IF NOT EXISTS booking_record (
                    client_id integer NOT NULL,
                    booking_date text NOT NULL,
                    room_type text NOT NULL,
                    hotel_id integer NOT NULL,
                    booking_cost double precision,
                    currency text,
                    age integer,
                    client_name text,
                    client_type text,
                    hotel_name text
                );
             ''',
    dag=ingestion_dag,
)"""

task_2 = PythonOperator(
    task_id='load_data',
    python_callable=load_data,
    dag=ingestion_dag,
)


#task_1 >> create_table >> task_2
task_1  >> task_2