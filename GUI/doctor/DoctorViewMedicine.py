import PySimpleGUI as sg


class DoctorViewMedicine:

    def __init__(self):
        self.__layout = []

    def run_doctor_view_medicine(self):
        self.__layout = [[sg.Button('Back')],
                  [sg.Text('The name of the medicine', size=(30,1))],
                  [sg.Checkbox('Mark as filled', default=False, key='mark_as_filled')],
                  [sg.Button('Save mark'), sg.Button('Remove medicine')]
                  ]
        return sg.Window("Medicine view", self.__layout, finalize=True)