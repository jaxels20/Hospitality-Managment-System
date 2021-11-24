import PySimpleGUI as sg


class DoctorView:
    """Represents the view where a doctor can see an overview of all the patients.
    """
    def __init__(self, patient_db):
        """Constructs all the necessary attributes for the DoctorView object.

        Args:
            patient_db (PatientDB): A database of patients.
        """        
        self.__layout = [[sg.Button('Logout')],
                         [sg.Text('Patients', size=(45,1))],
                         [sg.Listbox(patient_db.get_all_patients(), size=(45,10), enable_events=True, key = '_PATIENT_')]
                         ]

    def run_doctor_view(self):
        """Runs the doctor view.

        Returns:
            sg.Window: Adds a label and initialize the layout for the window.
        """        
        return sg.Window("Doctor view", self.__layout, finalize=True)
