# import server_handler_directory.MedicalRecord as MR
# import server_handler_directory.FinancialRecord as FR
# import sys

import GUI.GuiConnectionManager as gcm
import pickle
import GUI.GUI_class as GUI_class



class GuiHandler():
    def __init__(self):
        self.__gui_connection_manager = gcm.GuiConnectionManager()
        self.__gui = None
        self.__medical_db = []
        self.__emp_db = []
        self.__patient_db = []

    def retrieve_data(self):
        with self.__gui_connection_manager.get_socket() as s:
            s.connect((self.__gui_connection_manager.get_host(), self.__gui_connection_manager.get_port()))
            emp_db_pickle = s.recv(1024)
            patient_db_pickle = s.recv(1024)
            medical_db_pickle = s.recv(1024)

            self.__emp_db = pickle.loads(emp_db_pickle)
            self.__patient_db = pickle.loads(patient_db_pickle)
            self.__medical_db = pickle.loads(medical_db_pickle)

    def get_medical_db(self):
        return self.__medical_db

    def get_patient_db(self):
        return self.__patient_db

    def get_emp_db(self):
        return self.__emp_db

    def get_gui(self):
        return self.__gui

    def run_doctor_gui(self):
        self.__gui.get_doctor_gui().run_doctor(self.__patient_db, self.__medical_db)

    def run_nurse_gui(self):
        self.__gui.get_nurse_gui().run_nurse(self.__patient_db)

    def run_admin_gui(self):
        self.__gui.get_admin_gui().run_admin(self.__patient_db, self.__emp_db)

    def run_login_gui(self):
        return self.__gui.get_login_gui().run_login()

    def create_gui(self):
        self.__gui = GUI_class.GUIClass(self.__medical_db, self.__patient_db, self.__emp_db)




