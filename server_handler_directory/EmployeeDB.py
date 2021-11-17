import server_handler_directory.Admin as admin
import server_handler_directory.MedicalEmployee as med_emp
import pickle
from pathlib import Path
import sys
from server_handler_directory import MedicalEmployee
from server_handler_directory import Medicine
sys.modules['MedicalEmployee'] = MedicalEmployee
sys.modules['Medicine'] = Medicine


class EmployeeDB:
    def __init__(self):
        self.__admin = admin.Admin()
        self.__list_of_doctors = self.fill_list_of_doctors()
        self.__list_of_nurses = self.fill_list_of_nurses()


    def get_all_doctors(self):
        return self.__list_of_doctors


    def get_all_nurses(self):
        return self.__list_of_nurses


    def create_nurse(self, username, password, name):
        med_emp.MedicalEmployee(username, password, name, 'nurse')


    def create_doctor(self,username, password, name):
        med_emp.MedicalEmployee(username, password, name, 'doctor')


    def remove_nurse(self, nurse):
        if nurse in self.__list_of_nurses:
            self.__list_of_nurses.remove(nurse)

    def remove_doctor(self, doctor):
        if doctor in self.__list_of_doctors:
            self.__list_of_nurses.remove(doctor)

    def fill_list_of_doctors(self):
        list =[]
        file_path = Path(__file__).parents[0].joinpath("data", "doctors_data.pkl")
        with open(file_path, 'rb') as md:
            while True:
                try:
                    list.append(pickle.load(md))
                except EOFError:
                    return list

    def fill_list_of_nurses(self):
        list = []
        file_path = Path(__file__).parents[0].joinpath("data", "nurses_data.pkl")
        with open(file_path, 'rb') as md:
            while True:
                try:
                    list.append(pickle.load(md))
                except EOFError:
                    return list