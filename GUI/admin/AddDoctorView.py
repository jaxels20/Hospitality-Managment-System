import PySimpleGUI as sg


class AddDoctorView:

    def __init__(self):
        self.__layout = [
            [sg.Text('Name', size=(8, 1)), sg.InputText(key='d_name')],
            [sg.Text('Username', size=(8, 1)), sg.InputText(key='d_username')],
            [sg.Text('Password', size=(8, 1)),
             sg.InputText('', key='d_password', password_char='*')],
            [sg.Submit('Save doctor'), sg.Exit("Exit")]]


    def run_add_doctor_view(self):
        return sg.Window("Add doctor view", self.__layout, finalize=True)