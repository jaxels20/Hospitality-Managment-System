import PySimpleGUI as sg


class AdminView:

    def __init__(self, patient_db, employee_db):
        self.__layout = [[sg.Button('Logout')],
              [sg.Text('Patients', size=(45, 1)), sg.Text('Doctors', size=(45, 1)), sg.Text('Nurses', size=(45, 1))],
              [sg.Listbox(patient_db.get_all_patients(), size=(50, 10),
                          enable_events=True, key='_PATIENT_'),
               sg.Listbox(employee_db.get_all_doctors(), size=(50, 10),
                          enable_events=True, key='_DOCTOR_'),
               sg.Listbox(employee_db.get_all_nurses(), size=(50, 10),
                          enable_events=True, key='_NURSE_')],
              [sg.Button('Add patient', size=(45, 1)), sg.Button('Add doctor', size=(45, 1)),
               sg.Button('Add nurse', size=(45, 1))]
              ]


    def run_admin_view(self):
        return sg.Window("Admin view", self.__layout, finalize=True)