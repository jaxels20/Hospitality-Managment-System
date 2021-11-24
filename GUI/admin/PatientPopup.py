import PySimpleGUI as sg


class PatientPopup:
    """Represents the popup when clicking on a patient in the view with the overviews 
    of persons.
    """
    def __init__(self):
        """Constructs all the necessary attributes for the PatientPopup object.
        """  
        self.layout = []

    def run_patient_popup(self, patient_obj):
        """Runs the patient popup view.

        Args:
            patient_obj (Patient): An object of a specific patient.

        Returns:
            sg.Window: Adds a label and initialize the layout for the window.
        """        
        self.layout = [
            [sg.Text('Patient information:', size=(40, 1)), sg.Text('Billing record: ')],
            [sg.Text([], size=(40, 1), key='pat_info'), sg.Listbox([], size=(50, 3), enable_events=True, key='_BILL_')],
            [sg.Button('Remove patient', size=(40, 1)), sg.Button('Generate bill')]]
        window = sg.Window("Patient", self.layout, finalize=True)
        window.Element('pat_info').update(patient_obj)
        window.Element('_BILL_').update(values=patient_obj.get_financial_record().get_patient_bill_list())
        return window
