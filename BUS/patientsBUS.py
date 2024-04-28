from DAO import connection_pool,PatientsDAO
from DTO import Patient

class PatientsBUS:
    def __init__(self, connection_pool):
        self.connection_pool = connection_pool
        self.patientsDAO = PatientsDAO(connection_pool)
        
    def get_patients(self):
        return [Patient(*patient) for patient in self.patientsDAO.get_patients()]
    
    def get_patient(self, patient_id):
        return Patient(*self.patientsDAO.get_patient(patient_id))
    
    def add_patient(self, patient):
        self.patientsDAO.add_patient(patient)
        
    def delete_patient(self, patient_id):
        self.patientsDAO.delete_patient(patient_id)
        
    def delete_patients(self, patient_ids):
        self.patientsDAO.delete_patients(patient_ids)
        
    def update_patient(self, patient):
        self.patientsDAO.update_patient(patient)
        
        
patients = PatientsBUS(connection_pool)