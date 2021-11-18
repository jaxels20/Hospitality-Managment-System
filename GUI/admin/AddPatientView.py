import PySimpleGUI as sg


class AddPatientView:

    def __init__(self):
        self.__layout =  [
        [sg.Text('CPR', size=(8, 1)), sg.InputText(key='p_cpr')],
        [sg.Text('Name', size=(8, 1)), sg.InputText(key='p_name')],
        [sg.Text('Bloodtype', size=(8, 1)), sg.InputText(key='p_bloodtype')],
        [sg.Text('Birthdate', size=(8, 1)), sg.InputText(key='p_birthdate')],
        [sg.Text('Height', size=(8, 1)), sg.InputText(key='p_height')],
        [sg.Submit('Save patient'), sg.Exit("Exit")]]


    def run_add_patient_view(self):
        return sg.Window("Add patient view", self.__layout, finalize=True)
