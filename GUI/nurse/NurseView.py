import PySimpleGUI as sg

class NurseView:

    def __init__(self, srv_handler):
        self.__layout = [[sg.Button('Logout')],
                         [sg.Text('Patients', size=(45,1))],
                         [sg.Listbox(srv_handler.get_patientdb().get_all_patients(),
                                     size=(45, 10), enable_events=True, key='_PATIENT_')]
                         ]

    def run_nurse_view(self):
        return sg.Window("Nurse view", self.__layout, finalize=True)