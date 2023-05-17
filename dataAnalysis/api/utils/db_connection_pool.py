import mysql.connector
import psycopg2
import sqlite3
import pymssql
import cx_Oracle

def get_database_connection(db_type, **kwargs):
    """
    Get a database connection object based on the database type and connection parameters.

    :param db_type: string, the type of database to connect to ('mysql', 'postgresql', 'sqlite', 'mssql', 'oracle')
    :param kwargs: dictionary, connection parameters specific to the database type
    :return: database connection object
    """

    # MySQL database connection
    if db_type == 'mysql':
        return mysql.connector.connect(
            host=kwargs.get('host'),
            user=kwargs.get('user'),
            password=kwargs.get('password'),
            database=kwargs.get('database')
        )

    # PostgreSQL database connection
    elif db_type == 'postgresql':
        return psycopg2.connect(
            host=kwargs.get('host'),
            user=kwargs.get('user'),
            password=kwargs.get('password'),
            database=kwargs.get('database')
        )

    # SQLite database connection
    elif db_type == 'sqlite':
        return sqlite3.connect(kwargs.get('database'))

    # Microsoft SQL Server database connection
    elif db_type == 'mssql':
        return pymssql.connect(
            host=kwargs.get('host'),
            user=kwargs.get('user'),
            password=kwargs.get('password'),
            database=kwargs.get('database')
        )

    # Oracle database connection
    elif db_type == 'oracle':
        return cx_Oracle.connect(
            user=kwargs.get('user'),
            password=kwargs.get('password'),
            dsn=kwargs.get('dsn')
        )

    # Raise an error if an unsupported database type is specified
    else:
        raise ValueError("Unsupported database type: %s" % db_type)
