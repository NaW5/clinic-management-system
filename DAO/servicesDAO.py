class ServicesDAO:
    def __init__(self, connection_pool):
        self.connection_pool = connection_pool
        
    def get_services(self):
        connection = self.connection_pool.get_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT DichVu.ID, DichVu.TenDichVu, DichVu.MoTa, DichVu.Phi, PhongKhoa.* FROM DichVu JOIN PhongKhoa ON DichVu.Khoa = PhongKhoa.ID')
        services = cursor.fetchall()
        cursor.close()
        self.connection_pool.release_connection(connection)
        return services
    
    def get_service(self, service_id):
        connection = self.connection_pool.get_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT DichVu.ID, DichVu.TenDichVu, DichVu.MoTa, DichVu.Phi, PhongKhoa.* FROM DichVu JOIN PhongKhoa ON DichVu.Khoa = PhongKhoa.ID WHERE DichVu.ID = ?', (service_id,))
        service = cursor.fetchone()
        cursor.close()
        self.connection_pool.release_connection(connection)
        return service
    
    def add_service(self, service):
        connection = self.connection_pool.get_connection()
        cursor = connection.cursor()
        cursor.execute('INSERT INTO DichVu VALUES(?,?,?,?,?)', 
                       (service.id, service.name, service.department.id , service.description, service.charge))
        connection.commit()
        cursor.close()
        self.connection_pool.release_connection(connection)
    
    def delete_service(self, service_id):
        connection = self.connection_pool.get_connection()
        cursor = connection.cursor()
        cursor.execute('DELETE FROM LichKham WHERE DichVu = ?', (service_id))
        cursor.execute('DELETE FROM DichVu WHERE ID = ?', (service_id))
        connection.commit()
        cursor.close()
        self.connection_pool.release_connection(connection)
        
    def delete_services(self, service_ids):
        connection = self.connection_pool.get_connection()
        cursor = connection.cursor()
        cursor.execute('DELETE FROM LichKham WHERE DichVu IN ({})'.format(','.join(['?']*len(service_ids))), service_ids)
        cursor.execute('DELETE FROM DichVu WHERE ID IN ({})'.format(','.join(['?']*len(service_ids))), service_ids)
        connection.commit()
        cursor.close()
        self.connection_pool.release_connection(connection)
        
    def update_service(self, service):
        connection = self.connection_pool.get_connection()
        cursor = connection.cursor()
        cursor.execute('UPDATE DichVu SET TenDichVu = ?, Khoa = ?, MoTa = ?, Phi = ? WHERE ID = ?', 
                       (service.name, service.department.id, service.description, service.charge, service.id))
        connection.commit()
        cursor.close()
        self.connection_pool.release_connection(connection)
        
        
    
    
    