import PySimpleGUI as sg


class DoctorViewMedicine:
    """Represents the popup where a doctor can mark a medicine as filled for a specific patient.
    """
    def __init__(self):
        """Constructs all the necessary attributes for the DoctorViewMedicine object.
        """        
        self.__layout = []

    def run_doctor_view_medicine(self):
        """Runs the popup where a medicine can be marked as filled.

        Returns:
            sg.Window: Adds a label and initialize the layout for the window.
        """        
        self.__layout = [[sg.Button('Back')],
                  [sg.Text('The name of the medicine', size=(30,1))],
                  [sg.Checkbox('Mark as filled', default=False, key='mark_as_filled')],
                  [sg.Button('Save mark'), sg.Button('Remove medicine')]
                  ]
        return sg.Window("Medicine view", self.__layout, finalize=True)