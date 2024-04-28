from DAO import connection_pool,EquipmentsDAO
from DTO import Equipment, Provider

class EquipmentsBUS:
    def __init__(self, connection_pool):
        self.connection_pool = connection_pool
        self.equipmentsDAO = EquipmentsDAO(connection_pool)
        
    def get_equipments(self):
        return [Equipment(
            id=equipment[0],
            name=equipment[1],
            type=equipment[2],
            buy_date=equipment[3],
            price=equipment[4],
            quantity=equipment[5],
            provider=Provider(
                id=equipment[6],
                name=equipment[7],
                email=equipment[8],
                phone=equipment[9]
            )    
        ) for equipment in self.equipmentsDAO.get_equipments()]
    
    def get_equipment(self, equipment_id):
        id, name, type, buy_date, price, quantity, provider_id, provider_name, provider_email, provider_phone = self.equipmentsDAO.get_equipment(equipment_id)
        return Equipment(
            id=id,
            name=name,
            type=type,
            buy_date=buy_date,
            price=price,
            quantity=quantity,
            provider=Provider(
                id=provider_id,
                name=provider_name,
                email=provider_email,
                phone=provider_phone
            )
        )
    
    def add_equipment(self, equipment):
        self.equipmentsDAO.add_equipment(equipment)
        
    def delete_equipment(self, equipment_id):
        self.equipmentsDAO.delete_equipment(equipment_id)
        
    def delete_equipments(self, equipment_ids):
        self.equipmentsDAO.delete_equipments(equipment_ids)
        
    def update_equipment(self, equipment):
        self.equipmentsDAO.update_equipment(equipment)
        
        
equipments = EquipmentsBUS(connection_pool)