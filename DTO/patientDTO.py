
class Patient:
    def __init__(self, id, name, gender, birth, address, phone, medical_history=None):
        self.id = id
        self.name = name
        self.gender = gender
        self.birth = birth
        self.address = address
        self.phone = phone
        self.medical_history = medical_history
    
    