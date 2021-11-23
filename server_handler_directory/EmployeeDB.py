import server_handler_directory.Admin as admin
import server_handler_directory.MedicalEmployee as med_emp
import pickle
from pathlib import Path
import sys
from server_handler_directory import Medicine
sys.modules['Medicine'] = Medicine
sys.modules['MedicalEmployee'] = med_emp



class EmployeeDB:
    """The class containing all the employees of the hospital
    """    
    def __init__(self):
        """Constructs all the necessary attributes for the EmployeeDB object.
            The lists of doctors and nurses get filled with the fill method. 
        """        
        self.__admin = admin.Admin()
        self.__list_of_doctors = self.fill_list_of_doctors()
        self.__list_of_nurses = self.fill_list_of_nurses()


    def get_all_doctors(self):
        """Return a list of doctors.

        Returns:
            list: A list containing all the doctor objects.
        """
        return self.__list_of_doctors


    def get_all_nurses(self):
        """Return a list of nurses.

        Returns:
            list: A list containing all the nurse objects.
        """      
        return self.__list_of_nurses

    def get_admin(self):
        """Retrieve the admin object

        Returns:
            Admin: The admin object containing all the information of the admin
        """        
        return self.__admin

    def create_nurse(self, username, password, name):
        """Creates a nurse and a stores it in the database.

        Args:
            username (string): The username of nurse.
            password (string): The password of the nurse.
            name ([type]): The name of the nurse.
        """        
        self.__list_of_nurses.append(med_emp.MedicalEmployee(username, password, name, 'nurse'))


    def create_doctor(self,username, password, name):
        """Creates a doctor and a stores it in the database.

        Args:
            username (string): The username of doctor.
            password (string): The password of the doctor.
            name (string): The name of the doctor
        """        
        self.__list_of_doctors.append(med_emp.MedicalEmployee(username, password, name, 'doctor'))


    def remove_nurse(self, nurse):
        """Remove a specific nurse form the database.

        Args:
            Nurse (Nurse): The nurse you would like to delete.
        """        
        if nurse in self.__list_of_nurses:
            self.__list_of_nurses.remove(nurse)


    def remove_doctor(self, doctor):
        """Remove a specific doctor form the database.

        Args:
            Doctor (Doctor): The doctor you would like to delete.
        """      
        if doctor in self.__list_of_doctors:
            self.__list_of_doctors.remove(doctor)


    def fill_list_of_doctors(self):
        """The method load the pickle file which contains doctors and stores them in this object.
        This method is called in the constructor.

        Returns:
            list: List of all doctors.
        """        
        list =[]
        file_path = Path(__file__).parents[0].joinpath("data", "doctors_data.pkl")
        with open(file_path, 'rb') as md:
            while True:
                try:
                    list.append(pickle.load(md))
                except EOFError:
                    return list

    def fill_list_of_nurses(self):
        """The method load the pickle file which contains nurses and stores them in this object.
        This method is called in the constructor.

        Returns:
            list: List of all nurses.
        """   
        list = []
        file_path = Path(__file__).parents[0].joinpath("data", "nurses_data.pkl")
        with open(file_path, 'rb') as md:
            while True:
                try:
                    list.append(pickle.load(md))
                except EOFError:
                    return list