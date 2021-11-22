import PySimpleGUI as sg

class NurseViewPatient:
    def __init__(self):
        self.__layout = []

    def run_nurse_view_patient(self, patient_obj):
        self.__layout = [[sg.Button('Back')],
                          [sg.Text('Medical Record', size=(30,1)), sg.Text('Patient', size=(30,1))],
                          [sg.Listbox([],
                                      size=(30,10), enable_events=True, key = '_MEDICAL_'),
                           sg.Text([], size=(35,1), key='pat_info')]
                          ]
        window = sg.Window("View patient", self.__layout, finalize=True)
        window.Element('pat_info').update(patient_obj)
        return window

