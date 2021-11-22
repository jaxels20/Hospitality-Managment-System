import pickle
import server_handler_directory.Patient as Patient
from pathlib import Path
import sys
sys.modules['Patient'] = Patient


class PatientDB:
    def __init__(self):
        self.__list_of_patients = self.fill_list_of_patients()

    def get_all_patients(self):
        return self.__list_of_patients

    def create_patient(self, cpr, name, bloodtype, birthdate, height):
        patient = Patient.Patient(cpr, name, bloodtype, birthdate, height)
        self.__list_of_patients.append(patient)

    # def remove_patient(self, patient_object):
    #     if patient_object in self.__list_of_patients:
    #         self.__list_of_patients.remove(patient_object)

    def remove_patient(self, patient_cpr):
        for i in range(len(self.__list_of_patients)):
            if patient_cpr == self.__list_of_patients[i].get_cpr():
                del self.__list_of_patients[i]


    def fill_list_of_patients(self):
        file_path = Path(__file__).parents[0].joinpath("data", "patients_data.pkl")
        list = []
        with open(file_path, 'rb') as md:
            while True:
                try:
                    list.append(Patient.Patient.unpickle_patient(md))
                except EOFError:
                    return list

