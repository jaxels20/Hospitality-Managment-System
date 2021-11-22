import PySimpleGUI as sg


class NursePopup:

    def __init__(self):
        self.layout = []


    def run_nurse_popup(self):
        self.layout = [
            [sg.Text('Nurse information: ')],
            [sg.Text("values['_NURSE_'][0]")],
            [sg.Text("Type username to remove: ")],
            [sg.InputText(key='nur_to_remove')],
            [sg.Button('Remove nurse')]]
        return sg.Window("Nurse", self.layout, finalize=True)
