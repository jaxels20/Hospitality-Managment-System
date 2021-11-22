import server_handler_directory.EmployeeDB as EmployeeDB
import server_handler_directory.PatientDB as PatientDB
import server_handler_directory.Medical_DB as Medical_DB
import server_handler_directory.ServerConnectionManager as ServerConnectionManager
import pickle
import time


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
        pickled_object_medical_db = pickle.dumps(server_handler.get_medicaldb())
        pickled_object_emp_db = pickle.dumps(server_handler.get_empployeedb())
        pickled_object_patient_db = pickle.dumps(server_handler.get_patientdb())

        with self.__ServerConnectionManager.get_socket() as s:
            while True:
                s.listen()
                conn, addr = s.accept()
                with conn:
                    conn.sendall(pickled_object_emp_db)
                    time.sleep(1)
                    conn.sendall(pickled_object_patient_db)
                    time.sleep(1)
                    conn.sendall(pickled_object_medical_db)


serv = ServerHandler()

serv.send_all_data()




