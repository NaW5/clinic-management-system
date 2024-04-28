import pyodbc
from queue import Queue

class ODBCConnectionPool:
    def __init__(self, connection_string, pool_size=10):
        self.connection_string = connection_string
        self.pool = Queue(maxsize=pool_size)
        for _ in range(pool_size):
            self.pool.put(pyodbc.connect(connection_string))
            
    def get_connection(self):
        return self.pool.get()
    
    def release_connection(self, connection):
        self.pool.put(connection)
        
    def close_all(self):
        while not self.pool.empty():
            connection = self.pool.get()
            connection.close()