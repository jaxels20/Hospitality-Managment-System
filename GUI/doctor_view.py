import PySimpleGUI as sg
from server_handler_directory import ServerHandler


class DoctorView:


    def __init__(self):
        self.data = []


    def run_doctor(self, srv_handler):
        layout = [[sg.Button('Logout')],
                 [sg.Text('Patients', size=(45,1))],
                 [sg.Listbox(srv_handler.get_patientdb().get_all_patients(), size=(45,10), enable_events=True, key = '-PATIENT-')]
                 ]

        window = sg.Window('Doctor view', layout)
        event, values = window.read()


    def view_patient(self, srv_handler):
        layout = [[sg.Button('Logout')],
                  [sg.Text('Medical record', size=(30,1)), sg.Text('Patients', size=(30,1))],
                  [sg.Listbox(srv_handler.get_medicaldb().get_all_medicine(), size=(30,10), enable_events=True, key = '-MEDICAL-'), sg.Text('patient information here', size=(30,1))],
                  [sg.Button('Add')]
                  ]

        window = sg.Window('Patient View', layout)
        event, values = window.read()


    def click_medicine(self):
        layout = [[sg.Button('Logout')],
                  [sg.Text('The name of the medicine', size=(30,1))],
                  [sg.Checkbox('Mark as filled', default=False)],
                  [sg.Button('Remove medicine')]
                  ]

        window = sg.Window('Medicine view', layout)
        event, values = window.read()


    def add_medicine(self, srv_handler):
        layout = [[sg.Button('Logout')],
                  [sg.Text('Medical list')],
                  [sg.Text('Choose medicine to add:')],
                  [sg.Listbox(srv_handler.get_medicaldb().get_all_medicine(), size=(40,10), enable_events=True, key='-MEDICINE-')]
                  ]

        window = sg.Window('Add medicine view', layout)
        event, values = window.read()


    def confirm_add_medicine(self):
        layout = [[sg.Text('Add Medicine?', size=(30,1))],
                  [sg.Button('Add')]
                  ]

        window = sg.Window('Confirm', layout)
        event, values = window.read()

serverhandler2 = ServerHandler.ServerHandler()
doctor = DoctorView()

event, values = doctor.view_patient(serverhandler2)
print(event, values)


