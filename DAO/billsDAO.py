class BillsDAO:
    def __init__(self, connection_pool):
        self.connection_pool = connection_pool
        
    def get_bills(self):
        connection = self.connection_pool.get_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT HoaDon.ID, HoaDon.NgayTao, HoaDon.GiamGia, HoaDon.TongTien, HoaDon.TongThu, BenhNhan.*, BacSi.* FROM HoaDon JOIN BenhNhan ON HoaDon.BenhNhan = BenhNhan.ID JOIN BacSi ON HoaDon.BacSi = BacSi.ID ORDER BY HoaDon.NgayTao DESC')
        bills = cursor.fetchall()
        cursor.close()
        self.connection_pool.release_connection(connection)
        return bills
    
    def get_bill(self, bill_id):
        connection = self.connection_pool.get_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT HoaDon.ID, HoaDon.NgayTao, HoaDon.GiamGia, HoaDon.TongTien, HoaDon.TongThu, BenhNhan.*, BacSi.* FROM HoaDon JOIN BenhNhan ON HoaDon.BenhNhan = BenhNhan.ID JOIN BacSi ON HoaDon.BacSi = BacSi.ID WHERE ID = ?', (bill_id,))
        bill = cursor.fetchone()
        cursor.close()
        self.connection_pool.release_connection(connection)
        return bill
    
    def add_bill(self, bill):
        connection = self.connection_pool.get_connection()
        cursor = connection.cursor()
        cursor.execute('INSERT INTO HoaDon VALUES(?,?,?,?,?,?,?)', 
                       (bill.id, bill.patient.id, bill.doctor.id, bill.date, bill.discount, bill.total, bill.real_total))
        connection.commit()
        cursor.close()
        self.connection_pool.release_connection(connection)
    
    def delete_bill(self, bill_id):
        connection = self.connection_pool.get_connection()
        cursor = connection.cursor()
        cursor.execute('DELETE FROM HoaDon WHERE ID = ?', (bill_id,))
        connection.commit()
        cursor.close()
        self.connection_pool.release_connection(connection)
        
    def delete_bills(self, bill_ids):
        connection = self.connection_pool.get_connection()
        cursor = connection.cursor()
        cursor.execute('DELETE FROM HoaDon WHERE ID IN ({})'.format(','.join(['?']*len(bill_ids))), bill_ids)
        connection.commit()
        cursor.close()
        self.connection_pool.release_connection(connection)
        
    def update_bill(self, bill):
        connection = self.connection_pool.get_connection()
        cursor = connection.cursor()
        cursor.execute('UPDATE HoaDon SET BenhNhan = ?, BacSi = ?, NgayTao = ?, GiamGia = ?, TongTien = ?, TongThu = ? WHERE ID = ?', 
                       (bill.patient.id, bill.doctor.id, bill.date, bill.discount, bill.total, bill.real_total, bill.id))
        connection.commit()
        cursor.close()
        self.connection_pool.release_connection(connection)
        
        
    
    
    