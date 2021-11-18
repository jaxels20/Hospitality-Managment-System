import PySimpleGUI as sg
from server_handler_directory import ServerHandler


class NurseView:

    def __init__(self):
        self.data = []


    def run_nurse(self, srv_handler):
        layout = [[sg.Button('Logout')],
                 [sg.Text('Patients', size=(45,1))],
                 [sg.Listbox(srv_handler.get_patientdb().get_all_patients(), size=(45,10), enable_events=True, key = '-PATIENT-')]
                 ]

        window = sg.Window('Nurse view', layout)
        event, values = window.read()

    def view_patient(self, srv_handler):
        layout = [[sg.Button('Logout')],
                  [sg.Text('Medical Record', size=(30,1)), sg.Text('Patient', size=(30,1))],
                  [sg.Listbox(srv_handler.get_medicaldb().get_all_medicine(), size=(30,10), enable_events=True, key = '-MEDICAL-'), sg.Text('patient information here', size=(35,1))]
                  ]

        window = sg.Window('Patient View', layout)
        event, values = window.read()

    def click_medicine(self):
        layout = [[sg.Button('Logout')],
                  [sg.Text('The name of the medicine', size=(30,1))],
                  [sg.Checkbox('Mark as filled', default=False)]
                  ]

        window = sg.Window('Medicine view', layout)
        event, values = window.read()


serverhandler3 = ServerHandler.ServerHandler()

nurse = NurseView()

event, values = nurse.click_medicine()
print(event, values)