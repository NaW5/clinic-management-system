class AccountsDAO:
    def __init__(self, connection_pool):
        self.connection_pool = connection_pool
    
    def get_accounts(self):
        connection = self.connection_pool.get_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM TaiKhoan')
        accounts = cursor.fetchall()
        cursor.close()
        self.connection_pool.release_connection(connection)
        return accounts
    
    def add_account(self, account):
        connection = self.connection_pool.get_connection()
        cursor = connection.cursor()
        cursor.execute('''
        INSERT INTO TaiKhoan VALUES (?, ?, ?)
        ''', (account.role, account.username, account.password))
        connection.commit()
        cursor.close()
        self.connection_pool.release_connection(connection)