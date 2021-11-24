import server_handler_directory.MedicalRecord as MR
import server_handler_directory.FinancialRecord as FR
import sys
sys.modules['MedicalRecord'] = MR
sys.modules['FinancialRecord'] = FR


class Patient:
    """Representation of a patient
    """     
    def __init__(self, cpr, name, bloodtype, birthdate, height):
        """Constructs all the necessary attributes for the patient object.

        Args:
            cpr (string): An unique indetifier for each patient.
            name (string): Name of the patient.
            bloodtype (string): The bloodtype of the patient.
            birthdate (string): The birthdate of the patient.
            height (integer): The height of the person.
        """        
        self.__cpr = cpr
        self.__name = name
        self.__bloodtype = bloodtype
        self.__birthdate = birthdate
        self.__height = height
        self.__medical_record = MR.MedicalRecord()
        self.__financial_record = FR.FinancialRecord()

    def get_financial_record(self):
        """retrieve the financial record of a patient.

        Returns:
            FinancialRecord: the financial record of a specific patient.
        """        
        return self.__financial_record

    def __repr__(self):
        """This built in function define how the object will behave when printed.

        Returns:
            string: The string that will be printed.
        """        
        return f'cpr: {self.__cpr} and name: {self.__name}'

    def get_cpr(self):
        """ retrieve the cpr number from a patient.

        Returns:
            string: An unique identifier for each patient.
        """        
        return self.__cpr

    def get_medical_record(self):
        """retrieve the medical record for a patient.

        Returns:
            MedicalRecord: The medical record of a patient.
        """        
        return self.__medical_record

    def get_birth(self):
        """Retrieve the birthdate of a patient.

        Returns:
            string: The birthdate of a patient.
        """        
        return self.__birthdate
