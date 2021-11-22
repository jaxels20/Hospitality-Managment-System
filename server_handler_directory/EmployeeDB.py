import server_handler_directory.Admin as admin
import server_handler_directory.MedicalEmployee as med_emp
import pickle
from pathlib import Path
import sys

#stod der før:
# from server_handler_directory import MedicalEmployee
# from server_handler_directory import Medicine
# sys.modules['MedicalEmployee'] = MedicalEmployee
# sys.modules['Medicine'] = Medicine

#nyt
from server_handler_directory import Medicine
sys.modules['Medicine'] = Medicine
sys.modules['MedicalEmployee'] = med_emp

class EmployeeDB:
    def __init__(self):
        self.__admin = admin.Admin()
        self.__list_of_doctors = self.fill_list_of_doctors()
        self.__list_of_nurses = self.fill_list_of_nurses()


    def get_all_doctors(self):
        return self.__list_of_doctors


    def get_all_nurses(self):
        return self.__list_of_nurses

    def get_admin(self):
        return self.__admin

    def create_nurse(self, username, password, name):
        self.__list_of_nurses.append(med_emp.MedicalEmployee(username, password, name, 'nurse'))


    def create_doctor(self,username, password, name):
        self.__list_of_doctors.append(med_emp.MedicalEmployee(username, password, name, 'doctor'))


    def remove_nurse(self, nurse_username):
        for i in range(len(self.__list_of_nurses)):
            if nurse_username == self.__list_of_nurses[i].get_username():
                del self.__list_of_nurses[i]


    def remove_doctor(self, doctor_username):
        for i in range(len(self.__list_of_doctors)):
            if doctor_username == self.__list_of_doctors[i].get_username():
                del self.__list_of_doctors[i]


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