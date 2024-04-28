class AppointmentsDAO:
    def __init__(self, connection_pool):
        self.connection_pool = connection_pool
        
    def get_appointments(self):
        connection = self.connection_pool.get_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT LichKham.ID, LichKham.Ngay, LichKham.Gio, LichKham.TrieuChung, LichKham.TrangThai, BenhNhan.*, BacSi.*, DichVu.* FROM LichKham JOIN BenhNhan ON LichKham.BenhNhan = BenhNhan.ID JOIN BacSi ON LichKham.BacSi = BacSi.ID JOIN DichVu ON LichKham.DichVu = DichVu.ID ORDER BY LichKham.Ngay DESC, LichKham.Gio DESC')
        appointments = cursor.fetchall()
        cursor.close()
        self.connection_pool.release_connection(connection)
        return appointments
    
    def get_appointment(self, appointment_id):
        connection = self.connection_pool.get_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT LichKham.ID, LichKham.Ngay, LichKham.Gio, LichKham.TrieuChung, LichKham.TrangThai, BenhNhan.*, BacSi.*, DichVu.* FROM LichKham JOIN BenhNhan ON LichKham.BenhNhan = BenhNhan.ID JOIN BacSi ON LichKham.BacSi = BacSi.ID JOIN DichVu ON LichKham.DichVu = DichVu.ID WHERE LichKham.ID = ?', (appointment_id,))
        appointment = cursor.fetchone()
        cursor.close()
        self.connection_pool.release_connection(connection)
        return appointment
    
    def add_appointment(self, appointment):
        connection = self.connection_pool.get_connection()
        cursor = connection.cursor()
        cursor.execute('INSERT INTO LichKham VALUES(?,?,?,?,?,?,?,?)', 
                       (appointment.id, appointment.patient.id, appointment.doctor.id if appointment.doctor else None, appointment.service.id, appointment.date, appointment.time, appointment.condition, appointment.status))
        connection.commit()
        cursor.close()
        self.connection_pool.release_connection(connection)
    
    def delete_appointment(self, appointment_id):
        connection = self.connection_pool.get_connection()
        cursor = connection.cursor()
        cursor.execute('DELETE FROM LichKham WHERE ID = ?', (appointment_id,))
        connection.commit()
        cursor.close()
        self.connection_pool.release_connection(connection)
        
    def delete_appointments(self, appointment_ids):
        connection = self.connection_pool.get_connection()
        cursor = connection.cursor()
        cursor.execute('DELETE FROM LichKham WHERE ID IN ({})'.format(','.join(['?']*len(appointment_ids))), appointment_ids)
        connection.commit()
        cursor.close()
        self.connection_pool.release_connection(connection)
        
    def update_appointment(self, appointment):
        connection = self.connection_pool.get_connection()
        cursor = connection.cursor()
        cursor.execute('UPDATE LichKham SET BenhNhan = ?, BacSi = ?, DichVu = ?, Ngay = ?, Gio = ?, TrieuChung = ?, TrangThai = ? WHERE ID = ?', 
                       (appointment.patient.id, appointment.doctor.id, appointment.service.id, appointment.date, appointment.time, appointment.condition, appointment.status, appointment.id))
        connection.commit()
        cursor.close()
        self.connection_pool.release_connection(connection)
        
        
    
    
    