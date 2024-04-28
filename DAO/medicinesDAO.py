class MedicinesDAO:
    def __init__(self, connection_pool):
        self.connection_pool = connection_pool
        
    def get_medicines(self):
        connection = self.connection_pool.get_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT Thuoc.ID, Thuoc.TenThuoc, Thuoc.Loai, Thuoc.DonGia, Thuoc.SoLuong, Thuoc.NgayMua, Thuoc.NgayHetHan, NCC.* FROM Thuoc JOIN NCC ON Thuoc.NCC = NCC.ID')
        medicines = cursor.fetchall()
        cursor.close()
        self.connection_pool.release_connection(connection)
        return medicines
    
    def get_medicine(self, medicine_id):
        connection = self.connection_pool.get_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT Thuoc.ID, Thuoc.TenThuoc, Thuoc.Loai, Thuoc.DonGia, Thuoc.SoLuong, Thuoc.NgayMua, Thuoc.NgayHetHan, NCC.* FROM Thuoc JOIN NCC ON Thuoc.NCC = NCC.ID WHERE Thuoc.ID = ?', (medicine_id,))
        medicine = cursor.fetchone()
        cursor.close()
        self.connection_pool.release_connection(connection)
        return medicine
    
    def add_medicine(self, medicine):
        connection = self.connection_pool.get_connection()
        cursor = connection.cursor()
        cursor.execute('INSERT INTO Thuoc VALUES(?,?,?,?,?,?,?,?)', 
                       (medicine.id, medicine.name, medicine.type, medicine.provider.id, medicine.unit_price, medicine.quantity, medicine.buy_date, medicine.expire_date))
        connection.commit()
        cursor.close()
        self.connection_pool.release_connection(connection)
    
    def delete_medicine(self, medicine_id):
        connection = self.connection_pool.get_connection()
        cursor = connection.cursor()
        cursor.execute('DELETE FROM Thuoc WHERE ID = ?', (medicine_id,))
        connection.commit()
        cursor.close()
        self.connection_pool.release_connection(connection)
        
    def delete_medicines(self, medicine_ids):
        connection = self.connection_pool.get_connection()
        cursor = connection.cursor()
        cursor.execute('DELETE FROM Thuoc WHERE ID IN ({})'.format(','.join(['?']*len(medicine_ids))), medicine_ids)
        connection.commit()
        cursor.close()
        self.connection_pool.release_connection(connection)
        
    def update_medicine(self, medicine):
        connection = self.connection_pool.get_connection()
        cursor = connection.cursor()
        cursor.execute('UPDATE Thuoc SET TenThuoc = ?, Loai = ?, NCC = ?, DonGia = ?, SoLuong = ?, NgayMua = ?, NgayHetHan = ? WHERE ID = ?', 
                       (medicine.name, medicine.type, medicine.provider, medicine.unit_price, medicine.quantity, medicine.buy_date, medicine.expire_date, medicine.id))
        connection.commit()
        cursor.close()
        self.connection_pool.release_connection(connection)
        
        
    
    
    