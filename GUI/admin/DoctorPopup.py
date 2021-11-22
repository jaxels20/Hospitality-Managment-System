import PySimpleGUI as sg


class DoctorPopup:

    def __init__(self):
        self.layout = []

    def run_doctor_popup(self):
        self.layout =  [
            [sg.Text('Doctor information: ')],
            [sg.Text("values['_DOCTOR_'][0]")],
            [sg.Text("Type username to remove: ")],
            [sg.InputText(key='doc_to_remove')],
            [sg.Button('Remove doctor')]]
        return sg.Window("Doctor", self.layout, finalize=True)
