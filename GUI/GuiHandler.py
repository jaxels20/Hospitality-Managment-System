import GUI.GuiConnectionManager as gcm
import pickle

class GuiHandler():
    def __init__(self):
        self.__gui_connection_manager = gcm.GuiConnectionManager()
        self.__gui = []
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

gui_handler = GuiHandler()

gui_handler.retrieve_data()

print(gui_handler.get_medical_db().get_all_medicine())



