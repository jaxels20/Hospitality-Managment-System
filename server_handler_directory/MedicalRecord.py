
class MedicalRecord:
    """ A class which represent a medical record of one patient.
    """    
    def __init__(self):
        """Constructs all the necessary attributes for the medical record object.
        """        
        self.__patient_medical_list = []

    def add_medicine(self, medicine_object):
        """Add a medicine object to the medical list.

        Args:
            medicine_object (Medicine): The medicine object you want to add to the medical list.
        """        
        self.__patient_medical_list.append(medicine_object)

    def remove_medicine(self, medicine_object):
        """Remove medicine object from medical object.

        Args:
            medicine_object (Medicine: The medicine object you want to remove from the medical list.
        """        
        if medicine_object in self.__patient_medical_list:
            self.__patient_medical_list.remove(medicine_object)

    def get_patient_medical_list(self):
        """Retrieve all the medicine in medical list.

        Returns:
            list: patient medical list.
        """        
        return self.__patient_medical_list

