import PySimpleGUI as sg


class DoctorConfirmAdd:
    """Represents the popup when a doctor shall confirm the adding of a medicine to a patient
    """
    def __init__(self):
        """Constructs all the necessary attributes for the DoctorConfirmAdd object.
        """ 
        self.__layout = []

    def run_doctor_confirm_add(self):
        """Runs the popup where the doctor confirm the added medicine.

        Returns:
            sg.Window: Adds a label and initialize the layout for the window.
        """        
        self.__layout = [[sg.Text('Add Medicine?', size=(30,1))],
                  [sg.Submit('Add'), sg.Exit('Cancel')]
                  ]
        return sg.Window("Confirm", self.__layout, finalize=True)