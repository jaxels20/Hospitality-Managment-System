import PySimpleGUI as sg


class PatientPopup:

    def __init__(self, values):
        self.layout = [
            [sg.Text('Patient information:', size=(40, 1)), sg.Text('Billing record: ')],
            [sg.Text(values['_PATIENT_'][0], size=(40, 1)), sg.Listbox([], size=(30, 3), enable_events=True, key='_BILL_')],
            [sg.Text("Type cpr to remove patient: ")],
            [sg.InputText(key='pat_to_remove')],
            [sg.Button('Remove patient', size=(40, 1)), sg.Button('Generate bill')]]


    def run_patient_popup(self):
        return sg.Window("Patient", self.layout, finalize=True)
