import PySimpleGUI as sg


class AddNurseView:

    def __init__(self):
        self.__layout = []


    def run_add_nurse_view(self):
        self.__layout = [
            [sg.Text('Name', size=(8, 1)), sg.InputText(key='n_name')],
            [sg.Text('Username', size=(8, 1)), sg.InputText(key='n_username')],
            [sg.Text('Password', size=(8, 1)),
             sg.InputText('', key='n_password', password_char='*')],
            [sg.Submit('Save nurse'), sg.Exit('Exit')]]
        return sg.Window("Add nurse view", self.__layout, finalize=True)