class EmployeesDAO:
    def __init__(self, connection_pool):
        self.connection_pool = connection_pool
        
    def get_employees(self):
        connection = self.connection_pool.get_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM NhanVien')
        employees = cursor.fetchall()
        cursor.close()
        self.connection_pool.release_connection(connection)
        return employees
    
    def get_employee(self, employee_id):
        connection = self.connection_pool.get_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM NhanVien WHERE ID = ?', (employee_id,))
        employee = cursor.fetchone()
        cursor.close()
        self.connection_pool.release_connection(connection)
        return employee
    
    def add_employee(self, employee):
        connection = self.connection_pool.get_connection()
        cursor = connection.cursor()
        cursor.execute('INSERT INTO NhanVien VALUES(?,?,?,?,?,?,?)', 
                       (employee.id, employee.name, employee.gender, employee.address, employee.email, employee.phone, employee.image))
        connection.commit()
        cursor.close()
        self.connection_pool.release_connection(connection)
    
    def delete_employee(self, employee_id):
        connection = self.connection_pool.get_connection()
        cursor = connection.cursor()
        cursor.execute('DELETE FROM NhanVien WHERE ID = ?', (employee_id,))
        connection.commit()
        cursor.close()
        self.connection_pool.release_connection(connection)
        
    def delete_employees(self, employee_ids):
        connection = self.connection_pool.get_connection()
        cursor = connection.cursor()
        cursor.execute('DELETE FROM NhanVien WHERE ID IN ({})'.format(','.join(['?']*len(employee_ids))), employee_ids)
        connection.commit()
        cursor.close()
        self.connection_pool.release_connection(connection)
        
    def update_employee(self, employee):
        connection = self.connection_pool.get_connection()
        cursor = connection.cursor()
        cursor.execute('UPDATE NhanVien SET HoTen = ?, GioiTinh = ?, DiaChi = ?, Email = ?, SDT = ?, HinhAnh = ? WHERE ID = ?', 
                       (employee.name, employee.gender, employee.address, employee.email, employee.phone, employee.image, employee.id))
        connection.commit()
        cursor.close()
        self.connection_pool.release_connection(connection)
        
        
    
    
    