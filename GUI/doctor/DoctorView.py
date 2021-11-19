import PySimpleGUI as sg


class DoctorView:

    def __init__(self, patient_db):
        self.__layout = [[sg.Button('Logout')],
                         [sg.Text('Patients', size=(45,1))],
                         [sg.Listbox(patient_db.get_all_patients(), size=(45,10), enable_events=True, key = '_PATIENT_')]
                         ]

    def run_doctor_view(self):
        return sg.Window("Doctor view", self.__layout, finalize=True)
