import PySimpleGUI as sg


class AdminView:

    def __init__(self):
        self.data = []


    def run_admin(self):
        layout = [[sg.Button('Logout')],
                  [sg.Text('Patients', size=(15, 1)), sg.Text('Doctors', size=(15, 1)), sg.Text('Nurses', size=(15, 1))],
                  [sg.Listbox([], size=(15, 10)), sg.Listbox([], size=(15, 10)), sg.Listbox([], size=(15, 10))],
                  [sg.Button('Add patient', size=(15, 1)), sg.Button('Add doctor', size=(15, 1)), sg.Button('Add nurse', size=(15, 1))]
                  ]
        window = sg.Window("Admin view", layout)
        event, values = window.read()

        while True:
            if event == 'Add patient':
                self.add_patient()
                event, values = self.run_admin()
            elif event == 'Add doctor':
                self.add_doctor()
                event, values = self.run_admin()
            elif event == 'Add nurse':
                self.add_nurse()
                event, values = self.run_admin()
            else:
                break

        window.close()
        return event, values


    def add_patient(self):
        layout = [
            [sg.Text('Name', size=(8, 1)), sg.InputText(key='p_name')],
            [sg.Text('CPR', size=(8, 1)), sg.InputText(key='p_cpr')],
            [sg.Text('Bloodtype', size=(8, 1)), sg.InputText(key='p_bloodtype')],
            [sg.Text('Birthdate', size=(8, 1)), sg.InputText(key='p_birthdate')],
            [sg.Text('Financial info', size=(8, 1)), sg.InputText(key='p_financial')],
            [sg.Submit('Add patient'), sg.Exit("Cancel")]
        ]
        window = sg.Window("Add patient view", layout)
        event, values = window.read()
        window.close()
        return event, values


    def add_doctor(self):
        layout = [
            [sg.Text('Name', size=(8, 1)), sg.InputText(key='d_name')],
            [sg.Text('Username', size=(8, 1)), sg.InputText(key='d_username')],
            [sg.Text('Password', size=(8, 1)),
             sg.InputText('', key='d_password', password_char='*')],
            [sg.Submit('Add doctor'), sg.Exit("Cancel")]
        ]
        window = sg.Window("Add doctor view", layout)
        event, values = window.read()
        window.close()
        return event, values


    def add_nurse(self):
        layout = [
            [sg.Text('Name', size=(8, 1)), sg.InputText(key='n_name')],
            [sg.Text('Username', size=(8, 1)), sg.InputText(key='n_username')],
            [sg.Text('Password', size=(8, 1)),
             sg.InputText('', key='n_password', password_char='*')],
            [sg.Submit('Add nurse'), sg.Exit("Cancel")]
        ]
        window = sg.Window("Add nurse view", layout)
        event, values = window.read()
        window.close()
        return event, values

admin = AdminView()
event, values = admin.run_admin()
print(event, values)