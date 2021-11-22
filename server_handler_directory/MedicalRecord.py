
class MedicalRecord:
    def __init__(self):
        self.__patient_medical_list = []

    def add_medicine(self, medicine_object):
        self.__patient_medical_list.append(medicine_object)

    def remove_medicine(self, medicine_object):
        if medicine_object in self.__patient_medical_list:
            self.__patient_medical_list.remove(medicine_object)

    def get_patient_medical_list(self):
        return self.__patient_medical_list

