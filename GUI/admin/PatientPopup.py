import PySimpleGUI as sg


class PatientPopup:

    def __init__(self):
        self.layout = []

    def run_patient_popup(self, patient_obj):
        self.layout = [
            [sg.Text('Patient information:', size=(40, 1)), sg.Text('Billing record: ')],
            [sg.Text([], size=(40, 1), key='pat_info'), sg.Listbox([], size=(30, 3), enable_events=True, key='_BILL_')],
            [sg.Text("Type cpr to remove patient: ")],
            [sg.InputText(key='pat_to_remove')],
            [sg.Button('Remove patient', size=(40, 1)), sg.Button('Generate bill')]]
        window = sg.Window("Patient", self.layout, finalize=True)
        window.Element('pat_info').update(patient_obj)
        window.Element('_BILL_').update(values=patient_obj.get_financial_record().get_patient_bill_list())
        return window
