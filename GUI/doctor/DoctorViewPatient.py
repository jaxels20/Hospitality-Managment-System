import PySimpleGUI as sg


class DoctorViewPatient:

    def __init__(self):
        self.__layout = []

    def run_doctor_view_patient(self, patient_obj):
        self.__layout = [[sg.Button('Back')],
                  [sg.Text('Medical record', size=(30,1)), sg.Text('Patients', size=(30,1))],
                #Her skal medical record ændres til patientens eget medicin
                  [sg.Listbox([], size=(30,10), enable_events=True, key = '_MEDICAL_'), sg.Text([], size=(30,1), key='pat_info')],
                  [sg.Button('Add medicine')]
                  ]
        window = sg.Window("View Patient", self.__layout, finalize=True)
        window.Element('pat_info').update(patient_obj)
        window.Element('_MEDICAL_').update(patient_obj.get_medical_record().get_patient_medical_list())
        return window
