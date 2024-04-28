from DAO import connection_pool,DoctorsDAO
from DTO import Doctor
from DTO import Department

class DoctorsBUS:
    def __init__(self, connection_pool):
        self.connection_pool = connection_pool
        self.doctorsDAO = DoctorsDAO(connection_pool)
        
    def get_doctors(self):
        return [Doctor(
            id=doctor[0],
            name=doctor[1],  
            gender=doctor[2],
            degrees=doctor[3],
            email=doctor[4],
            phone=doctor[5],
            image=doctor[6],
            department=Department(
                id=doctor[7],
                name=doctor[8],
                description=doctor[9],
                status=doctor[10]
            )
        ) for doctor in self.doctorsDAO.get_doctors()]
    
    def get_doctor(self, doctor_id):
        return Doctor(*self.doctorsDAO.get_doctor(doctor_id))
    
    def add_doctor(self, doctor):
        self.doctorsDAO.add_doctor(doctor)
        
    def delete_doctor(self, doctor_id):
        self.doctorsDAO.delete_doctor(doctor_id)
        
    def delete_doctors(self, doctor_ids):
        self.doctorsDAO.delete_doctors(doctor_ids)
        
    def update_doctor(self, doctor):
        self.doctorsDAO.update_doctor(doctor)
        
        
doctors = DoctorsBUS(connection_pool)