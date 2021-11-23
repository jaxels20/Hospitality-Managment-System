import PySimpleGUI as sg

class NurseViewMedicine:
    """Represents the popup where a nurse can mark a medicine as filled for a specific patient.
    """
    def __init__(self):
        """Constructs all the necessary attributes for the NurseViewMedicine object.
        """  
        self.__layout = []


    def run_nurse_view_medicine(self):
        """Runs the popup where a nurse can mark a medicine as filled.

        Returns:
            sg.Window: Adds a label and initialize the layout for the window.
        """ 
        self.__layout = [[sg.Button('Back')],
                  [sg.Text('The name of the medicine', size=(30,1))],
                  [sg.Checkbox('Mark as filled', default=False, key='mark_as_filled')],
                    [sg.Submit('Save mark'), sg.Exit('Cancel')]
                    ]

        return sg.Window("Medicine view", self.__layout, finalize=True)