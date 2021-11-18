from server_handler_directory import EmployeeDB
from server_handler_directory import PatientDB
from server_handler_directory import Medical_DB
from server_handler_directory import ServerConnectionManager
import pickle


class ServerHandler:

    def __init__(self):
        self.__employee_db = EmployeeDB.EmployeeDB()
        self.__patient_db = PatientDB.PatientDB()
        self.__medical_db = Medical_DB.MedicalDB()
        self.__ServerConnectionManager = ServerConnectionManager.ServerConnectionManager()

    def get_empployeedb(self):
        return self.__employee_db

    def get_patientdb(self):
        return self.__patient_db

    def get_medicaldb(self):
        return self.__medical_db

    def send_all_data(self):
        server_handler = ServerHandler()
        pickled_object = pickle.dumps(server_handler.__medical_db)

        with self.__ServerConnectionManager.get_socket() as s:
            s.listen()
            conn, addr = s.accept()
            with conn:
                while True:
                    data = conn.recv(1024)
                    print('connected')
                    if not data:
                        break
                    conn.sendall(data)

srv = ServerHandler()

srv.send_all_data()





