import PySimpleGUI as sg
import GUI.login.LoginView as lv


class LoginGui:

    def __init__(self):
        self.__login_view = lv.LoginView()

    def run_login(self):
        window = self.__login_view.run_login_view()

        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'cancel':
            return None, None
        window.close()
        return event, values

    def verify_login(self, emp_db, username, password):
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