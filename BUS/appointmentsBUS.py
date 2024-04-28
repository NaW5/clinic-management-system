from DAO import connection_pool,AppointmentsDAO
from DTO import Appointment, Patient, Doctor, Service
class AppointmentsBUS:
    def __init__(self, connection_pool):
        self.connection_pool = connection_pool
        self.appointmentsDAO = AppointmentsDAO(connection_pool)
        
    def get_appointments(self):
        return [Appointment(
            id=appointment[0],
            date=appointment[1],
            time=appointment[2],
            condition=appointment[3],
            status=appointment[4],
            patient=Patient(
                id=appointment[5],
                name=appointment[6],
                gender=appointment[7],
                birth=appointment[8],
                address=appointment[9],
                phone=appointment[10],
                medical_history=appointment[11]
            ),
            doctor=Doctor(
                id=appointment[12],
                name=appointment[13],
                gender=appointment[14],
                department=appointment[15],
                degrees=appointment[16],
                email=appointment[17],
                phone=appointment[18],
                image=appointment[19]
            ),
            service=Service(
                id=appointment[20],
                name=appointment[21],
                department=appointment[22],
                description=appointment[23],
                charge=appointment[24]
            )
        ) for appointment in self.appointmentsDAO.get_appointments()]
    
    def get_appointment(self, appointment_id):
        return Appointment(*self.appointmentsDAO.get_appointment(appointment_id))
    
    def add_appointment(self, appointment):
        self.appointmentsDAO.add_appointment(appointment)
        
    def delete_appointment(self, appointment_id):
        self.appointmentsDAO.delete_appointment(appointment_id)
        
    def delete_appointments(self, appointment_ids):
        self.appointmentsDAO.delete_appointments(appointment_ids)
        
    def update_appointment(self, appointment):
        self.appointmentsDAO.update_appointment(appointment)
        
        
appointments = AppointmentsBUS(connection_pool)