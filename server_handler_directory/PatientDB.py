import Patient
import pickle


class PatientsDB:
    def __init__(self):
        self.__list_of_patients = []

    def get_all_patients(self):
        return self.__list_of_patients

    def create_patient(self, cpr, name, bloodtype, age, birthdate, height):
        patient = Patient.Patient(cpr, name, bloodtype, age, birthdate, height)
        self.__list_of_patients.append(patient)

    def remove_patient(self, patient_object):
        if patient_object in self.__list_of_patients:
            self.__list_of_patients.remove(patient_object)


    def fill_list_of_patients(self):
        with open('data/patients_data.pkl', 'rb') as md:
            while True:
                try:
                    self.__list_of_patients.append(pickle.load(md))
                except EOFError:
                    break
