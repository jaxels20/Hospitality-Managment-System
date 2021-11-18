import PySimpleGUI as sg


class AddPatientView:

    def __init__(self):
        self.__layout =  [
        [sg.Text('Name', size=(8, 1)), sg.InputText(key='p_name')],
        [sg.Text('CPR', size=(8, 1)), sg.InputText(key='p_cpr')],
        [sg.Text('Bloodtype', size=(8, 1)), sg.InputText(key='p_bloodtype')],
        [sg.Text('Birthdate', size=(8, 1)), sg.InputText(key='p_birthdate')],
        [sg.Text('Financial info', size=(8, 1)), sg.InputText(key='p_financial')],
        [sg.Submit('Save patient'), sg.Exit("Cancel")]]


    def run_addpatientview(self):
        return sg.Window("Add patient view", self.__layout, finalize=True)
