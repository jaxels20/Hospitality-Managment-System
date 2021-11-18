import PySimpleGUI as sg

class DoctorViewMedicine:

    def __init__(self):
        self.__layout = [[sg.Button('Logout')],
                  [sg.Text('The name of the medicine', size=(30,1))],
                  [sg.Checkbox('Mark as filled', default=False)],
                  [sg.Button('Remove medicine')]
                  ]

    def run_doctor_view_medicine(self):
        return sg.Window("Medicine view", self.__layout, finalize=True)