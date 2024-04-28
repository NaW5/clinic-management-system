class ProvidersDAO:
    def __init__(self, connection_pool):
        self.connection_pool = connection_pool
        
    def get_providers(self):
        connection = self.connection_pool.get_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM NCC')
        providers = cursor.fetchall()
        cursor.close()
        self.connection_pool.release_connection(connection)
        return providers
    
    def get_provider(self, provider_id):
        connection = self.connection_pool.get_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM NCC WHERE ID = ?', (provider_id,))
        provider = cursor.fetchone()
        cursor.close()
        self.connection_pool.release_connection(connection)
        return provider
    
    def add_provider(self, provider):
        connection = self.connection_pool.get_connection()
        cursor = connection.cursor()
        cursor.execute('INSERT INTO NCC VALUES(?,?,?,?)', 
                       (provider.id, provider.name, provider.email, provider.phone))
        connection.commit()
        cursor.close()
        self.connection_pool.release_connection(connection)
    
    def delete_provider(self, provider_id):
        connection = self.connection_pool.get_connection()
        cursor = connection.cursor()
        cursor.execute('DELETE FROM NCC WHERE ID = ?', (provider_id,))
        connection.commit()
        cursor.close()
        self.connection_pool.release_connection(connection)
        
    def delete_providers(self, provider_ids):
        connection = self.connection_pool.get_connection()
        cursor = connection.cursor()
        cursor.execute('DELETE FROM NCC WHERE ID IN ({})'.format(','.join(['?']*len(provider_ids))), provider_ids)
        connection.commit()
        cursor.close()
        self.connection_pool.release_connection(connection)
        
    def update_provider(self, provider):
        connection = self.connection_pool.get_connection()
        cursor = connection.cursor()
        cursor.execute('UPDATE NCC SET Ten = ?, Email = ?, SDT = ? WHERE ID = ?', 
                       (provider.name, provider.email, provider.phone, provider.id))
        connection.commit()
        cursor.close()
        self.connection_pool.release_connection(connection)
        
        
    
    
    