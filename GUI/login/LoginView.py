import PySimpleGUI as sg


class LoginView:

    def __init__(self):
        self.__layout = [[sg.Text('Username', size=(8, 1)), sg.InputText(key='-username')], [sg.Text('Password', size=(8, 1)),
                    sg.InputText('', key='-password', password_char='*')], [sg.Submit("Login"), sg.Exit("Cancel")]]

    def run_login_view(self):
        return sg.Window("Login", self.__layout, finalize=True)