import PySimpleGUI as sg


class LoginView:
    """Represents the view where a user can login.
    """

    def __init__(self):
        """Constructs all the necessary attributes for the LoginView object.
        """       
        self.__layout = [[sg.Text('Username', size=(8, 1)), sg.InputText(key='-username')], [sg.Text('Password', size=(8, 1)),
                    sg.InputText('', key='-password', password_char='*')], [sg.Submit("Login"), sg.Exit("Cancel")]]

    def run_login_view(self):
        """Runs the login view.

        Returns:
            sg.Window: Adds a label and initialize the layout for the window.
        """        
        return sg.Window("Login", self.__layout, finalize=True)