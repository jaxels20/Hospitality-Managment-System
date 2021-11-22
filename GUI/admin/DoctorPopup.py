import PySimpleGUI as sg


class DoctorPopup:

    def __init__(self):
        self.layout = []

    def run_doctor_popup(self, doctor_obj):
        self.layout =  [
            [sg.Text('Doctor information: ')],
            [sg.Text([], key='doc_info')],
            [sg.Button('Remove doctor')]]
        window = sg.Window("Doctor", self.layout, finalize=True)
        window.Element('doc_info').update(doctor_obj)
        return window
