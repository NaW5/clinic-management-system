class Bill:
    def __init__(self, id, patient, doctor, date, discount, total, real_total, bill_details=None):
        self.id = id
        self.patient = patient
        self.doctor = doctor
        self.date = date
        self.discount = discount
        self.total = total
        self.real_total = real_total
        self.bill_details = bill_details