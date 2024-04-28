class BillDetailsDAO:
    def __init__(self, connection_pool):
        self.connection_pool = connection_pool
        
    def get_bill_details(self):
        connection = self.connection_pool.get_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM CT_HoaDon')
        bill_details = cursor.fetchall()
        cursor.close()
        self.connection_pool.release_connection(connection)
        return bill_details
    
    def get_bill_detail(self, bill_detail_id):
        connection = self.connection_pool.get_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM CT_HoaDon WHERE ID = ?', (bill_detail_id,))
        bill_detail = cursor.fetchone()
        cursor.close()
        self.connection_pool.release_connection(connection)
        return bill_detail
    
    def add_bill_detail(self, bill_detail):
        connection = self.connection_pool.get_connection()
        cursor = connection.cursor()
        cursor.execute('INSERT INTO CT_HoaDon VALUES(?,?,?)', 
                       (bill_detail.item, bill_detail.quantity, bill_detail.total))
        connection.commit()
        cursor.close()
        self.connection_pool.release_connection(connection)
    
    def delete_bill_detail(self, bill_detail_id):
        connection = self.connection_pool.get_connection()
        cursor = connection.cursor()
        cursor.execute('DELETE FROM CT_HoaDon WHERE ID = ?', (bill_detail_id,))
        connection.commit()
        cursor.close()
        self.connection_pool.release_connection(connection)
        
    def delete_bill_details(self, bill_detail_ids):
        connection = self.connection_pool.get_connection()
        cursor = connection.cursor()
        cursor.execute('DELETE FROM CT_HoaDon WHERE ID IN ({})'.format(','.join(['?']*len(bill_detail_ids))), bill_detail_ids)
        connection.commit()
        cursor.close()
        self.connection_pool.release_connection(connection)
        
    def update_bill_detail(self, bill):
        connection = self.connection_pool.get_connection()
        cursor = connection.cursor()
        cursor.execute('UPDATE CT_HoaDon SET HoaDon = ?, DichVu_Thuoc = ?, SoLuong = ?, Tong = ? WHERE ID = ?', 
                       (bill.bill_detail.item, bill.bill_detail.quantity, bill.bill_detail.quantity, bill.bill_detail.id))
        connection.commit()
        cursor.close()
        self.connection_pool.release_connection(connection)
        
        
    
    
    