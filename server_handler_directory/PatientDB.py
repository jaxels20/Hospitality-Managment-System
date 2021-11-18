import pickle
import server_handler_directory.Patient as Patient
import server_handler_directory.MedicalRecord as MedicalRecord
import server_handler_directory.FinancialRecord as FinancialRecord

import sys
from server_handler_directory import PatientDB
sys.modules['Patient'] = Patient
sys.modules['MedicalRecord'] = MedicalRecord
sys.modules['FinancialRecord'] = FinancialRecord

class PatientDB:
    def __init__(self):
        self.__list_of_patients = self.fill_list_of_patients()

    def get_all_patients(self):
        return self.__list_of_patients

    def create_patient(self, cpr, name, bloodtype, age, birthdate, height):
        patient = Patient.Patient(cpr, name, bloodtype, age, birthdate, height)
        self.__list_of_patients.append(patient)

    def remove_patient(self, patient_object):
        if patient_object in self.__list_of_patients:
            self.__list_of_patients.remove(patient_object)


    def fill_list_of_patients(self):
        list = []
        with open(r'C:\Users\Bruger\Desktop\Hospitality-Managment-System1\server_handler_directory\data\patients_data.pkl', 'rb') as md:
            while True:
                try:
                    list.append(pickle.load(md))
                except EOFError:
                    return list

