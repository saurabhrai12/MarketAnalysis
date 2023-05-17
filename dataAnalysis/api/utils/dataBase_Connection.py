
import psycopg2.pool
import sqlite3


class DatabaseConnectionPoolFactory:
    """
    Get a database connection object based on the database type and connection parameters.

    :param db_type: string, the type of database to connect to ('mysql', 'postgresql', 'sqlite', 'mssql', 'oracle')
    :param kwargs: dictionary, connection parameters specific to the database type
    :return: database connection object
    """
    def __init__(self):
        self._connection_pools = {}

    def get_connection_pool(self, db_type, db_config):
        # Check if the connection pool already exists
        if db_type in self._connection_pools:
            return self._connection_pools[db_type]

        # Create a new connection pool if it doesn't exist
        if db_type == "sqlite":
            self._connection_pools[db_type] = sqlite3.connector.pooling.MySQLConnectionPool(
                pool_name="mysql_pool",
                pool_size=5,
                **db_config
            )
        elif db_type == "postgresql":
            self._connection_pools[db_type] = psycopg2.pool.SimpleConnectionPool(
                minconn=1,
                maxconn=5,
                **db_config
            )
        else :
            raise ValueError("Unsupported database type: %s" % db_type)
        '''elif db_type == "sqlite":
            self._connection_pools[db_type] = sqlite3.connect(
                **db_config,
                check_same_thread=False
            )
        elif db_type == "mssql":
            self._connection_pools[db_type] = pymssql.pool.Pool(
                **db_config,
                max_pool_size=5,
                timeout=60
            )
        elif db_type == "oracle":
            self._connection_pools[db_type] = cx_Oracle.SessionPool(
                user=db_config['user'],
                password=db_config['password'],
                dsn=db_config['dsn'],
                min=1,
                max=5,
                increment=1,
                encoding="UTF-8"
            )'''
        

        return self._connection_pools[db_type]
