class EquipmentsDAO:
    def __init__(self, connection_pool):
        self.connection_pool = connection_pool
        
    def get_equipments(self):
        connection = self.connection_pool.get_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT ThietBi.ID, ThietBi.TenThietBi, ThietBi.Loai, ThietBi.NgayMua, ThietBi.Gia, ThietBi.SoLuong, NCC.* FROM ThietBi JOIN NCC ON ThietBi.NCC = NCC.ID')
        equipments = cursor.fetchall()
        cursor.close()
        self.connection_pool.release_connection(connection)
        return equipments
    
    def get_equipment(self, equipment_id):
        connection = self.connection_pool.get_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT ThietBi.ID, ThietBi.TenThietBi, ThietBi.Loai, ThietBi.NgayMua, ThietBi.Gia, ThietBi.SoLuong, NCC.* FROM ThietBi JOIN NCC ON ThietBi.NCC = NCC.ID WHERE ID = ?', (equipment_id,))
        equipment = cursor.fetchone()
        cursor.close()
        self.connection_pool.release_connection(connection)
        return equipment
    
    def add_equipment(self, equipment):
        connection = self.connection_pool.get_connection()
        cursor = connection.cursor()
        cursor.execute('INSERT INTO ThietBi VALUES(?,?,?,?,?,?,?)', 
                       (equipment.id, equipment.name, equipment.type, equipment.provider.id, equipment.buy_date, equipment.price, equipment.quantity))
        connection.commit()
        cursor.close()
        self.connection_pool.release_connection(connection)
    
    def delete_equipment(self, equipment_id):
        connection = self.connection_pool.get_connection()
        cursor = connection.cursor()
        cursor.execute('DELETE FROM ThietBi WHERE ID = ?', (equipment_id,))
        connection.commit()
        cursor.close()
        self.connection_pool.release_connection(connection)
        
    def delete_equipments(self, equipment_ids):
        connection = self.connection_pool.get_connection()
        cursor = connection.cursor()
        cursor.execute('DELETE FROM ThietBi WHERE ID IN ({})'.format(','.join(['?']*len(equipment_ids))), equipment_ids)
        connection.commit()
        cursor.close()
        self.connection_pool.release_connection(connection)
        
    def update_equipment(self, equipment):
        connection = self.connection_pool.get_connection()
        cursor = connection.cursor()
        cursor.execute('UPDATE ThietBi SET TenThietBi = ?, Loai = ?, NCC = ?, NgayMua = ?, Gia = ?, SoLuong = ? WHERE ID = ?', 
                       (equipment.name, equipment.type, equipment.provider.id, equipment.buy_date, equipment.price, equipment.quantity, equipment.id))
        connection.commit()
        cursor.close()
        self.connection_pool.release_connection(connection)
        
        
    
    
    