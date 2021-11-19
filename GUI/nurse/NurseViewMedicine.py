import PySimpleGUI as sg

class NurseViewMedicine:

    def __init__(self):
        self.__layout = [[sg.Button('Logout')],
                  [sg.Text('The name of the medicine', size=(30,1))],
                  [sg.Checkbox('Mark as filled', default=False)]
                  ]


    def run_nurse_view_medicine(self):
        return sg.Window("Medicine view", self.__layout, finalize=True)