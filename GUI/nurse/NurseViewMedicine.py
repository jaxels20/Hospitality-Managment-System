import PySimpleGUI as sg

class NurseViewMedicine:

    def __init__(self):
        self.__layout = []


    def run_nurse_view_medicine(self):
        self.__layout = [[sg.Button('Back')],
                  [sg.Text('The name of the medicine', size=(30,1))],
                  [sg.Checkbox('Mark as filled', default=False, key='mark_as_filled')],
                    [sg.Submit('Save mark'), sg.Exit('Cancel')]
                    ]

        return sg.Window("Medicine view", self.__layout, finalize=True)