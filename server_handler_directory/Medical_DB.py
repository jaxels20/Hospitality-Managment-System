import pickle


class MedicalDB:
    def __init__(self):
        self.__list_of_medicine = []

    def fill_medical_db(self):
        with open('data/medical_data.pkl', 'rb') as md:
            while True:
                try:
                    self.__list_of_medicine.append(pickle.load(md))
                except EOFError:
                    break

    def get_all_medicine(self):
        return self.__list_of_medicine


