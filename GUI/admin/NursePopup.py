import PySimpleGUI as sg


class NursePopup:
    """Represents the popup when clicking on a nurse in the view with the overviews 
    of persons.
    """  
    def __init__(self):
        """Constructs all the necessary attributes for the NursePopup object.
        """  
        self.layout = []

    def run_nurse_popup(self, nurse_obj):
        """Runs the nurse popup view.

        Args:
            nurse_obj (MedicalEmployee): An object of a specific nurse

        Returns:
            sg.Window: Adds a label and initialize the layout for the window.
        """   
        self.layout = [
            [sg.Text('Nurse information: ')],
            [sg.Text([], key='nurse_info')],
            [sg.Button('Remove nurse')]]
        window = sg.Window("Nurse", self.layout, finalize=True)
        window.Element('nurse_info').update(nurse_obj)
        return window
