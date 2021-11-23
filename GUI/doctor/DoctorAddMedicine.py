import PySimpleGUI as sg

class DoctorAddMedicine:
    """Represents the view when a doctor wants to add medicine to a patient.
    """ 
    def __init__(self):
        """Constructs all the necessary attributes for the DoctorAddMedicine object.
        """  
        self.__layout = []

    def run_doctor_add_medicine(self, medical_db):
        """Runs the doctor add medicine view.

        Args:
            medical_db (MedicalDB): A database of medicine objects.

        Returns:
            sg.Window: Adds a label and initialize the layout for the window.
        """        
        self.__layout = [[sg.Button('Back')],
                  [sg.Text('Medical list')],
                  [sg.Text('Choose medicine to add:')],
                  [sg.Listbox(medical_db.get_all_medicine(), size=(40,10), enable_events=True, key='_MEDICINE_')]
                  ]
        window = sg.Window("Add medicine view", self.__layout, finalize=True)
        return window
