import pickle
import server_handler_directory.Patient as Patient
from pathlib import Path
import sys
sys.modules['Patient'] = Patient


class PatientDB:
    """A class to represent a database of patients
    """    
    def __init__(self):
        """Constructs all the necessary attributes for the patientDB object.
        """        
        self.__list_of_patients = self.fill_list_of_patients()

    def get_all_patients(self):
        """ retrieve all the patients in the database

        Returns:
            list: list of all the patients in the database.
        """        
        return self.__list_of_patients

    def create_patient(self, cpr, name, bloodtype, birthdate, height):
        """create a patient and add it to the database.

        Args:
            cpr (string): A string containing the cpr of the patient.
            name (string): A string containing the name of the patient.
            bloodtype (string): A string containing the bloodtype of the patient.
            birthdate ([string): A string containing the birthdate of the patient.
            height (integer): An integer containing the height of the patient.
        """        
        patient = Patient.Patient(cpr, name, bloodtype, birthdate, height)
        self.__list_of_patients.append(patient)

    def remove_patient(self, patient_object):
        """remove a specific patient from the database.

        Args:
            patient_object (Patient): the patient object you would like to remove from the database.
        """        
        if patient_object in self.__list_of_patients:
            self.__list_of_patients.remove(patient_object)

    def fill_list_of_patients(self):
        """ This method is called in the constructor and is loading the patients from a pickle file.

        Returns:
            list: list of all the patients from the pickle file.
        """        
        file_path = Path(__file__).parents[0].joinpath("data", "patients_data.pkl")
        list = []
        with open(file_path, 'rb') as md:
            while True:
                try:
                    list.append(pickle.load(md))
                except EOFError:
                    return list
