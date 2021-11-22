import PySimpleGUI as sg

class DoctorAddMedicine:

    def __init__(self):
        self.__layout = []

    def run_doctor_add_medicine(self, medical_db):
        self.__layout = [[sg.Button('Back')],
                  [sg.Text('Medical list')],
                  [sg.Text('Choose medicine to add:')],
                  [sg.Listbox(medical_db.get_all_medicine(), size=(40,10), enable_events=True, key='_MEDICINE_')]
                  ]
        window = sg.Window("Add medicine view", self.__layout, finalize=True)
        return window
