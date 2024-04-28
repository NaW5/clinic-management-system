class DepartmentsDAO:
    def __init__(self, connection_pool):
        self.connection_pool = connection_pool
        
    def get_departments(self):
        connection = self.connection_pool.get_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM PhongKhoa')
        departments = cursor.fetchall()
        cursor.close()
        self.connection_pool.release_connection(connection)
        return departments
    
    def get_department(self, department_id):
        connection = self.connection_pool.get_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM PhongKhoa WHERE ID = ?', (department_id,))
        department = cursor.fetchone()
        cursor.close()
        self.connection_pool.release_connection(connection)
        return department
    
    def add_department(self, department):
        connection = self.connection_pool.get_connection()
        cursor = connection.cursor()
        cursor.execute('INSERT INTO PhongKhoa VALUES(?,?,?,?)', 
                       (department.id, department.name, department.description, 1 if department.status == 'Hoạt động' else 0))
        connection.commit()
        cursor.close()
        self.connection_pool.release_connection(connection)
    
    def delete_department(self, department_id):
        connection = self.connection_pool.get_connection()
        cursor = connection.cursor()
        cursor.execute('DELETE FROM BacSi WHERE Khoa = ?', (department_id,))
        cursor.execute('DELETE FROM DichVu WHERE Khoa = ?', (department_id,))
        cursor.execute('DELETE FROM PhongKhoa WHERE ID = ?', (department_id,))
        connection.commit()
        cursor.close()
        self.connection_pool.release_connection(connection)
        
    def delete_departments(self, department_ids):
        connection = self.connection_pool.get_connection()
        cursor = connection.cursor()
        cursor.execute('DELETE FROM BacSi WHERE Khoa IN ({})'.format(','.join(['?']*len(department_ids))), department_ids)
        cursor.execute('DELETE FROM DichVu WHERE Khoa IN ({})'.format(','.join(['?']*len(department_ids))), department_ids)
        cursor.execute('DELETE FROM PhongKhoa WHERE ID IN ({})'.format(','.join(['?']*len(department_ids))), department_ids)
        connection.commit()
        cursor.close()
        self.connection_pool.release_connection(connection)
        
    def update_department(self, department):
        connection = self.connection_pool.get_connection()
        cursor = connection.cursor()
        cursor.execute('UPDATE PhongKhoa SET TenPhong = ?, MoTa = ?, TrangThai = ? WHERE ID = ?', 
                       (department.name, department.description, department.status, department.id))
        connection.commit()
        cursor.close()
        self.connection_pool.release_connection(connection)
        
        
    
    
    