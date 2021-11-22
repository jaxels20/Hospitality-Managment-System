import server_handler_directory.MedicalRecord as MR
import server_handler_directory.FinancialRecord as FR
import pickle
import sys
sys.modules['MedicalRecord'] = MR
sys.modules['FinancialRecord'] = FR


class Patient:
    def __init__(self, cpr, name, bloodtype, birthdate, height):
        self.__cpr = cpr
        self.__name = name
        self.__bloodtype = bloodtype
        self.__birthdate = birthdate
        self.__height = height

        self.medical_record = MR.MedicalRecord()
        self.billing_record = FR.FinancialRecord()

    def __eq__(self, other):
        if self.__cpr == other.__cpr:
            return True
        return False

    def __repr__(self):
        return f'cpr: {self.__cpr} and name: {self.__name}'

    def get_cpr(self):
        return self.__cpr

    @staticmethod
    def unpickle_patient(pickle_object):
        return pickle.load(pickle_object)
