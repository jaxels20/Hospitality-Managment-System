import MedicalRecord as MR
import FinancialRecord as FR

class Patient:
    def __init__(self, cpr, name, bloodtype, age, birthdate, height):
        self.__cpr = cpr
        self.__name = name
        self.__bloodtype = bloodtype
        self.__age = age
        self.__birthdate = birthdate
        self.__height = height

        self.medical_record = MR.MedicalRecord()
        self.billing_record = FR.FinancialRecord()


    def __eq__(self, other):
        if self.__cpr == other.__cpr:
            return True
        return False