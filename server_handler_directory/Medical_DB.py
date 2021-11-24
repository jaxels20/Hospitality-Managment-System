import pickle
from pathlib import Path


class MedicalDB:
    """The class contain on the methods and attributes of the medical db.
        This class defines what medical objects the doctor can add. In theory it will contain all possible medicine.
    """    
    def __init__(self):
        """Constructs all the necessary attributes for the Medical_DB object.
        """        
        self.__list_of_medicine = self.fill_medical_db()

    def fill_medical_db(self):
        """The method loads in the pickle file containing the predefined medical objects.
            This method gets called in the constructor.

        Returns:
            list: list containing all the medicine objects.
        """        
        list = []
        file_path = Path(__file__).parents[0].joinpath("data", "medical_data.pkl")
        with open(file_path, 'rb') as md:
            while True:
                try:
                    list.append(pickle.load(md))
                except EOFError:
                    return list

    def get_all_medicine(self):
        """get all the medicine objects in the database.

        Returns:
            list: contains all the medicine objects in the database.
        """        
        return self.__list_of_medicine


