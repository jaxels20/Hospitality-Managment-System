import PySimpleGUI as sg

class DoctorConfirmAdd:

    def __init__(self):
        self.__layout = []


    def run_doctor_confirm_add(self):
        self.__layout = [[sg.Text('Add Medicine?', size=(30,1))],
                  [sg.Submit('Add'), sg.Exit('Cancel')]
                  ]
        return sg.Window("Confirm", self.__layout, finalize=True)