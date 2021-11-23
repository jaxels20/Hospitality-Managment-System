# import server_handler_directory.MedicalRecord as MR
# import server_handler_directory.FinancialRecord as FR
# import sys

import GUI.GuiConnectionManager as gcm
import pickle
import GUI.Gui as GUI_class



class GuiHandler():
    """A class with the object which handles the GUI.
    """     
    def __init__(self):
        """Constructs all the nessecary attributes for the GuiHandler object.
        """         
        self.__gui_connection_manager = gcm.GuiConnectionManager()
        self.__gui = None
        self.__medical_db = []
        self.__emp_db = []
        self.__patient_db = []

    def retrieve_data(self):
        """Retrieves all the data through a connection as pickle files, and load the files in to the different databases for patients, medicine and medical employees.
        """        
        with self.__gui_connection_manager.get_socket() as s:
            s.connect((self.__gui_connection_manager.get_host(), self.__gui_connection_manager.get_port()))
            patient_db_pickle = s.recv(1024)
            emp_db_pickle = s.recv(1024)
            medical_db_pickle = s.recv(1024)

            self.__patient_db = pickle.loads(patient_db_pickle)
            self.__emp_db = pickle.loads(emp_db_pickle)
            self.__medical_db = pickle.loads(medical_db_pickle)

    def get_medical_db(self):
        """Retrieve the medical database.

        Returns:
            Medical_DB: An object of the medical database.
        """ 
        return self.__medical_db

    def get_patient_db(self):
        """Retrieve the patient database.

        Returns:
            PatientDB: An object of the patient database.
        """ 
        return self.__patient_db

    def get_emp_db(self):
        """Retrieve the medical employee database.

        Returns:
            EmployeeDB: An object of the medical employee database.
        """ 
        return self.__emp_db

    def get_gui(self):
        """Retrieve the gui.

        Returns:
            GUI: An object of the GUI.
        """ 
        return self.__gui

    def run_doctor_gui(self):
        """Runs the doctor gui.
        """        
        self.__gui.get_doctor_gui().run_doctor(self.__patient_db, self.__medical_db)

    def run_nurse_gui(self):
        """Runs the nurse gui.
        """  
        self.__gui.get_nurse_gui().run_nurse(self.__patient_db)

    def run_admin_gui(self):
        """Runs the admin gui.
        """  
        self.__gui.get_admin_gui().run_admin(self.__patient_db, self.__emp_db)

    def run_login_gui(self):
        """Runs the login gui.

        Returns:
            str, dictionary: Event of what the user has clicked, and a dictionary with the entered username and password.
        """        
        return self.__gui.get_login_gui().run_login()

    def create_gui(self):
        """Creates a Gui object with the databases for medicine, patients, and medical employees.
        """        
        self.__gui = GUI_class.Gui(self.__medical_db, self.__patient_db, self.__emp_db)




