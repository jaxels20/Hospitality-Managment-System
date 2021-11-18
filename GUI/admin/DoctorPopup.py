import PySimpleGUI as sg


class DoctorPopup:

    def __init__(self, values):
        self.layout = [
            [sg.Text('Doctor information: ')],
            [sg.Text(values['_DOCTOR_'][0])],
            [sg.Text("Type username to remove: ")],
            [sg.InputText(key='doc_to_remove')],
            [sg.Button('Remove doctor')]]

    def run_doctor_popup(self):
        return sg.Window("Doctor", self.layout, finalize=True)
