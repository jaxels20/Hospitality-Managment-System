import PySimpleGUI as sg
import GUI.login.LoginView as lv


class LoginGui:
    """Represents a class that handles the login gui.
    """
    def __init__(self):
        """Constructs all the necessary attributes for the LoginGui object.
        """        
        self.__login_view = lv.LoginView()

    def run_login(self):
        """Runs the login gui. A window is set to the login view. The while loop
        handles the events that can happen when a user tryes to login to the program.

        Returns:
            str, dictionary: Event of what the user has clicked, and a dictionary with 
                             the entered username and password.
        """        
        window = self.__login_view.run_login_view()

        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'cancel':
            return None, None
        window.close()
        return event, values

    def verify_login(self, emp_db, username, password):
        """Verifies a login by an user.

        Args:
            emp_db (EmploeeDB): A database of medical employees.
            username (str): A username that is entered in the login view.
            password (str): A password that is entered in the login view.

        Returns:
            str: A string for a verified user and the type of the user.
        """        
        if username == emp_db.get_admin().get_username():
            if password == emp_db.get_admin().get_password():
                return 'verified admin'

        for doctor in emp_db.get_all_doctors():
            if username == doctor.get_username():
                if password == doctor.get_password():
                    return 'verified doctor'

        for nurse in emp_db.get_all_nurses():
            if username == nurse.get_username():
                if password == nurse.get_password():
                    return 'verified nurse'

        return 'Login denied'