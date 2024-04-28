 
class Appointment:
    def __init__(self, id, patient, service, date, time, status, doctor=None, condition=None):
        self.id = id
        self.patient = patient
        self.doctor = doctor
        self.service = service
        self.date = date
        self.time = time
        self.condition = condition
        self.status = status