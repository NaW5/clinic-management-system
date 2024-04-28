class PatientsDAO:
    def __init__(self, connection_pool):
        self.connection_pool = connection_pool
        
    def get_patients(self):
        connection = self.connection_pool.get_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM BenhNhan')
        patients = cursor.fetchall()
        cursor.close()
        self.connection_pool.release_connection(connection)
        return patients
    
    def get_patient(self, patient_id):
        connection = self.connection_pool.get_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM BenhNhan WHERE ID = ?', (patient_id,))
        patient = cursor.fetchone()
        cursor.close()
        self.connection_pool.release_connection(connection)
        return patient
    
    def add_patient(self, patient):
        connection = self.connection_pool.get_connection()
        cursor = connection.cursor()
        cursor.execute('INSERT INTO BenhNhan VALUES(?,?,?,?,?,?,?)', 
                       (patient.id, patient.name, patient.gender, patient.birth, patient.address, patient.phone, patient.medical_history))
        connection.commit()
        cursor.close()
        self.connection_pool.release_connection(connection)
    
    def delete_patient(self, patient_id):
        connection = self.connection_pool.get_connection()
        cursor = connection.cursor()
        cursor.execute('DELETE FROM LichKham WHERE BenhNhan = ?', (patient_id,))
        cursor.execute('DELETE FROM HoaDon WHERE BenhNhan = ?', (patient_id,))
        cursor.execute('DELETE FROM BenhNhan WHERE ID = ?', (patient_id,))
        connection.commit()
        cursor.close()
        self.connection_pool.release_connection(connection)
        
    def delete_patients(self, patient_ids):
        connection = self.connection_pool.get_connection()
        cursor = connection.cursor()
        cursor.execute('DELETE FROM LichKham WHERE BenhNhan IN ({})'.format(','.join(['?']*len(patient_ids))), patient_ids)
        cursor.execute('DELETE FROM HoaDon WHERE BenhNhan IN ({})'.format(','.join(['?']*len(patient_ids))), patient_ids)
        cursor.execute('DELETE FROM BenhNhan WHERE ID IN ({})'.format(','.join(['?']*len(patient_ids))), patient_ids)
        connection.commit()
        cursor.close()
        self.connection_pool.release_connection(connection)
        
    def update_patient(self, patient):
        connection = self.connection_pool.get_connection()
        cursor = connection.cursor()
        cursor.execute('UPDATE BenhNhan SET HoTen = ?, GioiTinh = ?, NgaySinh = ?, DiaChi = ?, SDT = ?, TienSuBenhAn = ? WHERE ID = ?', 
                       (patient.name, patient.gender, patient.birth, patient.address, patient.phone, patient.medical_history, patient.id))
        connection.commit()
        cursor.close()
        self.connection_pool.release_connection(connection)
        
        
    
    
    