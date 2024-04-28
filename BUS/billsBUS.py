from DAO import connection_pool,BillsDAO
from DTO import Bill, Patient, Doctor

class BillsBUS:
    def __init__(self, connection_pool):
        self.connection_pool = connection_pool
        self.billsDAO = BillsDAO(connection_pool)
        
    def get_bills(self):
        return [Bill(
            id=bill[0],
            date=bill[1],
            discount=bill[2],
            total=bill[3],
            real_total=bill[4],
            patient=Patient(
                id=bill[5],
                name=bill[6],
                gender=bill[7],
                birth=bill[8],
                address=bill[9],
                phone=bill[10],
                medical_history=bill[11]
            ),
            doctor=Doctor(
                id=bill[12],
                name=bill[13],
                gender=bill[14],
                degrees=bill[15],
                email=bill[16],
                phone=bill[17],
                image=bill[18],
                department=bill[19],
            )    
        ) for bill in self.billsDAO.get_bills()]
    
    def get_bill(self, bill_id):
        id, date, discount, total, real_total, patient_id, patient_name, patient_gender, patient_birth, patient_address, patient_phone, patient_medical_history, doctor_id, doctor_name, doctor_gender, doctor_degrees, doctor_email, doctor_phone, doctor_image, doctor_department = self.billsDAO.get_bill(bill_id)
        return Bill(
            id=id,
            date=date,
            discount=discount,
            total=total,
            real_total=real_total,
            patient=Patient(
                id=patient_id,
                name=patient_name,
                gender=patient_gender,
                birth=patient_birth,
                address=patient_address,
                phone=patient_phone,
                medical_history=patient_medical_history
            ),
            doctor=Doctor(
                id=doctor_id,
                name=doctor_name,
                gender=doctor_gender,
                degrees=doctor_degrees,
                email=doctor_email,
                phone=doctor_phone,
                image=doctor_image,
                department=doctor_department,
            )
        )
    
    def add_bill(self, bill):
        self.billsDAO.add_bill(bill)
        
    def delete_bill(self, bill_id):
        self.billsDAO.delete_bill(bill_id)
        
    def delete_bills(self, bill_ids):
        self.billsDAO.delete_bills(bill_ids)
        
    def update_bill(self, bill):
        self.billsDAO.update_bill(bill)
        
        
bills = BillsBUS(connection_pool)