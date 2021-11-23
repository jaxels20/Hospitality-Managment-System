import PySimpleGUI as sg

class NurseViewPatient:
    """Represents the view where a nurse can see more specific details about medicine for a patient.
    """
    def __init__(self):
        """Constructs all the necessary attributes for the NurseViewPatient object.
        """
        self.__layout = []

    def run_nurse_view_patient(self, patient_obj):
        """Runs the view where a nurse can see more datails about a patient.

        Args:
            patient_obj (Patient): An object of a specific patient.

        Returns:
            sg.Window: Adds a label and initialize the layout for the window.
        """      
        self.__layout = [[sg.Button('Back')],
                          [sg.Text('Medical Record', size=(30,1)), sg.Text('Patient', size=(30,1))],
                          [sg.Listbox([],
                                      size=(30,10), enable_events=True, key = '_MEDICAL_'),
                           sg.Text([], size=(35,1), key='pat_info')]
                          ]
        window = sg.Window("View patient", self.__layout, finalize=True)
        window.Element('pat_info').update(patient_obj)
        window.Element('_MEDICAL_').update(patient_obj.get_medical_record().get_patient_medical_list())
        return window

