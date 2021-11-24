import server_handler_directory.EmployeeDB as EmployeeDB
import server_handler_directory.PatientDB as PatientDB
import server_handler_directory.Medical_DB as Medical_DB
import server_handler_directory.ServerConnectionManager as ServerConnectionManager
import pickle
import time


class ServerHandler:
    """The objects which handles the server.
    """
    def __init__(self):
        """Constructs all the necessary attributes for the ServerHandler object.
        """        
        self.__employee_db = EmployeeDB.EmployeeDB()
        self.__patient_db = PatientDB.PatientDB()
        self.__medical_db = Medical_DB.MedicalDB()
        self.__ServerConnectionManager = ServerConnectionManager.ServerConnectionManager()

    def get_empployeedb(self):
        """Retrieve the employee database.

        Returns:
            EmployeeDB: The current database of employees.
        """        
        return self.__employee_db

    def get_patientdb(self):
        """Retrieve the patient database.

        Returns:
            PatientDB: The current database of Patients.
        """         
        return self.__patient_db

    def get_medicaldb(self):
        """Retrieve the medical database.

        Returns:
            PatientDB: The current database of all the medicine objects.
        """  
        return self.__medical_db

    def send_all_data(self):
        """This method makes the server listen for clients and if a client connects it send all the data needed
        for the client.
        """        
        server_handler = ServerHandler()
        pickled_object_medical_db = pickle.dumps(server_handler.get_medicaldb())
        pickled_object_emp_db = pickle.dumps(server_handler.get_empployeedb())
        pickled_object_patient_db = pickle.dumps(server_handler.get_patientdb())

        with self.__ServerConnectionManager.get_socket() as s:
            while True:
                s.listen()
                conn, addr = s.accept()
                with conn:
                    conn.sendall(pickled_object_patient_db)
                    time.sleep(1)
                    conn.sendall(pickled_object_emp_db)
                    time.sleep(1)
                    conn.sendall(pickled_object_medical_db)


if __name__ == '__main__':
    server = ServerHandler()
    server.send_all_data()




