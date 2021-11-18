from server_handler_directory import EmployeeDB
from server_handler_directory import PatientDB
from server_handler_directory import Medical_DB

class ServerHandler:

    def __init__(self):
        self.__employee_db = EmployeeDB.EmployeeDB()
        self.__patient_db = PatientDB.PatientDB()
        self.__medical_db = Medical_DB.MedicalDB()

    def get_empployeedb(self):
        return self.__employee_db

    def get_patientdb(self):
        return self.__patient_db

    def get_medicaldb(self):
        return self.__medical_db