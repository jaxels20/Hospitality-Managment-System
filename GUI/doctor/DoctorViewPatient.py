import PySimpleGUI as sg


class DoctorViewPatient:

    def __init__(self):
        self.__layout = [[sg.Button('Logout')],
                  [sg.Text('Medical record', size=(30,1)), sg.Text('Patients', size=(30,1))],
                #Her skal medical record ændres til patientens eget medicin
                  [sg.Listbox([], size=(30,10), enable_events=True, key = '_MEDICAL_'), sg.Text('patient information here', size=(30,1))],
                  [sg.Button('Add medicine')]
                  ]

    def run_doctor_view_patient(self):
        return sg.Window("View Patient", self.__layout, finalize=True)