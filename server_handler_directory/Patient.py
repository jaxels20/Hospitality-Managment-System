import server_handler_directory.MedicalRecord as MR
import server_handler_directory.FinancialRecord as FR


class Patient:
    def __init__(self, cpr, name, bloodtype, age, height):
        self.__cpr = cpr
        self.__name = name
        self.__bloodtype = bloodtype
        self.__age = age
        self.__height = height

        self.medical_record = MR.MedicalRecord()
        self.billing_record = FR.FinancialRecord()

    def __eq__(self, other):
        if self.__cpr == other.__cpr:
            return True
        return False

    def __repr__(self):
        return f'cpr: {self.__cpr} and name: {self.__name}'