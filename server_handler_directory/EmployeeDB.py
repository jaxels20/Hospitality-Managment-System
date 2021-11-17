import Admin as admin
import MedicalEmployee as med_emp


class EmployeeDB:
    def __init__(self):
        self.__admin = admin.Admin()
        self.__list_of_doctors = []
        self.__list_of_nurses = []


    def get_all_doctors(self):
        self.__list_of_doctors


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







