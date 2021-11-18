import PySimpleGUI as sg

class NurseViewPatient:
    def __init__(self, srv_handler):
        self.__layout = [[sg.Button('Logout')],
                  [sg.Text('Medical Record', size=(30,1)), sg.Text('Patient', size=(30,1))],
                # Her skal ændres til patientens egen medical record
                  [sg.Listbox(srv_handler.get_medicaldb().get_all_medicine(), size=(30,10), enable_events=True, key = '_MEDICAL_'), sg.Text('patient information here', size=(35,1))]
                  ]

    def run_nurse_view_patient(self):
        return sg.Window("View patient", self.__layout, finalize=True)

