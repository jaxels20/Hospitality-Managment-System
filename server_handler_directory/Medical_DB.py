import pickle
from pathlib import Path
import server_handler_directory.MedicalEmployee as MedicalEmployee

class MedicalDB:
    def __init__(self):
        self.__list_of_medicine = self.fill_medical_db()

    def fill_medical_db(self):
        list = []
        file_path = Path(__file__).parents[0].joinpath("data", "medical_data.pkl")
        with open(file_path, 'rb') as md:
            while True:
                try:
                    list.append(pickle.load(md))
                except EOFError:
                    return list

    def get_all_medicine(self):
        return self.__list_of_medicine


