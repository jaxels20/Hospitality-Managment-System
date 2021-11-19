import PySimpleGUI as sg


class LoginV:

    def __init__(self):
        self.data = []

    def run_login(self):
        layout = [[sg.Text('Username', size=(8, 1)), sg.InputText(key='-username')], [sg.Text('Password', size=(8, 1)),
                    sg.InputText('', key='-password', password_char='*')], [sg.Submit("Login"), sg.Exit("Cancel")]]
        window = sg.Window("Login", layout)
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            return None
        window.close()
        return event, values
