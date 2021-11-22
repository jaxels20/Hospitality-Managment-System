import PySimpleGUI as sg


class NursePopup:

    def __init__(self):
        self.layout = []


    def run_nurse_popup(self, nurse_obj):
        self.layout = [
            [sg.Text('Nurse information: ')],
            [sg.Text([], key='nurse_info')],
            [sg.Button('Remove nurse')]]
        window = sg.Window("Nurse", self.layout, finalize=True)
        window.Element('nurse_info').update(nurse_obj)
        return window
