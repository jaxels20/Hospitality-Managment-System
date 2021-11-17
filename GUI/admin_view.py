import PySimpleGUI as sg


class AdminView:

    def __init__(self):
        self.data = []


    def run_admin(self):
        layout = [[sg.Text('Patients', size=(15, 1)), sg.Text('Doctors', size=(15, 1)), sg.Text('Nurses', size=(15, 1))],
                  [sg.Listbox([], size=(15, 10)), sg.Listbox([], size=(15, 10)), sg.Listbox([], size=(15, 10))],
                  [sg.Button('Add', size=(15, 1)), sg.Button('Add', size=(15, 1)), sg.Button('Add', size=(15, 1))]
                  ]
        window = sg.Window("Admin view", layout)
        event, values = window.read()
        window.close()
        return event, values


admin = AdminView()
event, values = admin.run_admin()
print(event, values)