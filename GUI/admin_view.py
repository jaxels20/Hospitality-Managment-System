import PySimpleGUI as sg
from server_handler_directory import ServerHandler

class AdminView:

    def __init__(self):
        self.data = []


    def run_admin(self, srv_handler):
        layout = [[sg.Button('Logout')],
                  [sg.Text('Patients', size=(45, 1)), sg.Text('Doctors', size=(45, 1)), sg.Text('Nurses', size=(45, 1))],
                  [sg.Listbox(srv_handler.get_patientdb().get_all_patients(), size=(50, 10),
                              enable_events=True, key='_PATIENT_'),
                   sg.Listbox(srv_handler.get_empployeedb().get_all_doctors(), size=(50, 10),
                              enable_events=True, key='_DOCTOR_'),
                   sg.Listbox(srv_handler.get_empployeedb().get_all_nurses(), size=(50, 10),
                              enable_events=True, key='_NURSE_')],
                  [sg.Button('Add patient', size=(45, 1)), sg.Button('Add doctor', size=(45, 1)),
                   sg.Button('Add nurse', size=(45, 1))]
                  ]
        window = sg.Window("Admin view", layout)
        event, values = window.read()
        while True:
            if event == 'Add patient':
                self.add_patient()
                event, values = self.run_admin(srv_handler)
            elif event == 'Add doctor':
                self.add_doctor()
                event, values = self.run_admin(srv_handler)
            elif event == 'Add nurse':
                self.add_nurse()
                event, values = self.run_admin(srv_handler)
            elif event == '_PATIENT_':
                self.patient_popup(values)
                event, values = self.run_admin(srv_handler)
            elif event == '_DOCTOR_':
                self.doctor_popup(values)
                event, values = self.run_admin(srv_handler)
            elif event == '_NURSE_':
                self.nurse_popup(values)
                event, values = self.run_admin(srv_handler)
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

# LISTBOX NEEDS INPUT FROM PATIENTS FINANCIAL RECORD AND A WHILE LOOP TO CREATE A BILL IF BUTTON IS PRESSED
# GENERATE BILL BUTTON NEEDS A KEY WHICH SHOULD BE USED TO OPEN click_bill()
    def patient_popup(self, values):
        layout = [
            [sg.Text('Billing record:', size=(27, 1)), sg.Text('Patient information')],
            [sg.Listbox([], size=(30, 3), enable_events=True, key='_BILL_'),
                        sg.Text(values['_PATIENT_'][0])],
            [sg.Button('Generate bill', size=(27, 1)), sg.Button('Remove patient')]
        ]
        window = sg.Window("Patient", layout)
        event, values = window.read()
        window.close()
        return event, values


    def click_bill(self, values):
        layout = [
            [sg.Text('Bill information: ')],
            [sg.Text(values['_BILL_'][0])],
            [sg.Button('Remove bill')]
        ]
        window = sg.Window("Bill", layout)
        event, values = window.read()
        window.close()
        return event, values


    def doctor_popup(self, values):
        layout = [
            [sg.Text('Doctor information: ')],
            [sg.Text(values['_DOCTOR_'][0])],
            [sg.Button('Remove doctor')]
        ]
        window = sg.Window("Doctor", layout)
        event, values = window.read()
        window.close()
        return event, values


    def nurse_popup(self, values):
        layout = [
            [sg.Text('Nurse information: ')],
            [sg.Text(values['_NURSE_'][0])],
            [sg.Button('Remove nurse')]
        ]
        window = sg.Window("Nurse", layout)
        event, values = window.read()
        window.close()
        return event, values

serverhandler1 = ServerHandler.ServerHandler()

admin = AdminView()

event, values = admin.run_admin(serverhandler1)
print(event, values)