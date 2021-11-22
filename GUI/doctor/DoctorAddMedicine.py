import PySimpleGUI as sg

class DoctorAddMedicine:

    def __init__(self, medical_db):
        self.__layout = []

    def run_doctor_add_medicine(self):
        self.__layout = [[sg.Button('Logout')],
                  [sg.Text('Medical list')],
                  [sg.Text('Choose medicine to add:')],
                  [sg.Listbox([], size=(40,10), enable_events=True, key='_MEDICINE_')]
                  ]
        return sg.Window("Add medicine view", self.__layout, finalize=True)
