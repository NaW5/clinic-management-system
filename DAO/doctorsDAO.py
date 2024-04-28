class DoctorsDAO:
    def __init__(self, connection_pool):
        self.connection_pool = connection_pool
        
    def get_doctors(self):
        connection = self.connection_pool.get_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT BacSi.ID, BacSI.HoTen, BacSi.GioiTinh, BacSi.BangCap, BacSi.Email, BacSi.SDT, BacSi.HinhAnh, PhongKhoa.* FROM BacSi JOIN PhongKhoa ON BacSi.Khoa = PhongKhoa.ID')
        doctors = cursor.fetchall()
        cursor.close()
        self.connection_pool.release_connection(connection)
        return doctors
    
    def get_doctor(self, doctor_id):
        connection = self.connection_pool.get_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT BacSi.ID, BacSI.HoTen, BacSi.GioiTinh, BacSi.BangCap, BacSi.Email, BacSi.SDT, BacSi.HinhAnh, PhongKhoa.* FROM BacSi JOIN PhongKhoa ON BacSi.Khoa = PhongKhoa.ID WHERE BacSi.ID = ?', (doctor_id,))
        doctor = cursor.fetchone()
        cursor.close()
        self.connection_pool.release_connection(connection)
        return doctor
    
    def add_doctor(self, doctor):
        connection = self.connection_pool.get_connection()
        cursor = connection.cursor()
        cursor.execute('INSERT INTO BacSi VALUES(?,?,?,?,?,?,?,?)', 
                       (doctor.id, doctor.name, doctor.gender, doctor.department.id, doctor.degrees, doctor.email, doctor.phone, doctor.image))
        connection.commit()
        cursor.close()
        self.connection_pool.release_connection(connection)
    
    def delete_doctor(self, doctor_id):
        connection = self.connection_pool.get_connection()
        cursor = connection.cursor()
        cursor.execute('DELETE FROM LichKham WHERE BacSi = ?', (doctor_id,))
        cursor.execute('DELETE FROM HoaDon WHERE BacSi = ?', (doctor_id,))
        cursor.execute('DELETE FROM BacSi WHERE ID = ?', (doctor_id,))
        connection.commit()
        cursor.close()
        self.connection_pool.release_connection(connection)
        
    def delete_doctors(self, doctor_ids):
        connection = self.connection_pool.get_connection()
        cursor = connection.cursor()
        cursor.execute('DELETE FROM LichKham WHERE BacSi IN ({})'.format(','.join(['?']*len(doctor_ids))), doctor_ids)
        cursor.execute('DELETE FROM HoaDon WHERE BacSi IN ({})'.format(','.join(['?']*len(doctor_ids))), doctor_ids)
        cursor.execute('DELETE FROM BacSi WHERE ID IN ({})'.format(','.join(['?']*len(doctor_ids))), doctor_ids)
        connection.commit()
        cursor.close()
        self.connection_pool.release_connection(connection)
        
    def update_doctor(self, doctor):
        connection = self.connection_pool.get_connection()
        cursor = connection.cursor()
        cursor.execute('UPDATE BacSi SET HoTen = ?, GioiTinh = ?, Khoa = ?, BangCap = ?, Email = ?, SDT = ?, HinhAnh = ? WHERE ID = ?', 
                       (doctor.name, doctor.gender, doctor.department.id, doctor.degrees, doctor.email, doctor.phone, doctor.image, doctor.id))
        connection.commit()
        cursor.close()
        self.connection_pool.release_connection(connection)
        
        
    
    
    