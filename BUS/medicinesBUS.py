from DAO import connection_pool,MedicinesDAO
from DTO import Medicine, Provider
class MedicinesBUS:
    def __init__(self, connection_pool):
        self.connection_pool = connection_pool
        self.medicinesDAO = MedicinesDAO(connection_pool)
        
    def get_medicines(self):
        return [Medicine(
            id=medicine[0],
            name=medicine[1],
            type=medicine[2],
            unit_price=medicine[3],
            quantity=medicine[4],
            buy_date=medicine[5],
            expire_date=medicine[6],
            provider=Provider(
                id=medicine[7],
                name=medicine[8],
                email=medicine[9],
                phone=medicine[10]
            )
        ) for medicine in self.medicinesDAO.get_medicines()]
    
    def get_medicine(self, medicine_id):
        id, name, type, unit_price, quantity, buy_date, expire_date, provider_id, provider_name, provider_email, provider_phone=self.medicinesDAO.get_medicine(medicine_id)
        return Medicine(
            id=id,
            name=name,
            type=type,
            unit_price=unit_price,
            quantity=quantity,
            buy_date=buy_date,
            expire_date=expire_date,
            provider=Provider(
                id=provider_id,
                name=provider_name,
                email=provider_email,
                phone=provider_phone
            )
        )
    
    def add_medicine(self, medicine):
        self.medicinesDAO.add_medicine(medicine)
        
    def delete_medicine(self, medicine_id):
        self.medicinesDAO.delete_medicine(medicine_id)
        
    def delete_medicines(self, medicine_ids):
        self.medicinesDAO.delete_medicines(medicine_ids)
        
    def update_medicine(self, medicine):
        self.medicinesDAO.update_medicine(medicine)
        
        
medicines = MedicinesBUS(connection_pool)