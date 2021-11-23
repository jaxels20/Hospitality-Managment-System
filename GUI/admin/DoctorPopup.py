import PySimpleGUI as sg


class DoctorPopup:
    """Represents the popup when clicking on a doctor in the view with the overviews 
    of persons.
    """    
    def __init__(self):
        """Constructs all the necessary attributes for the DoctorPopup object.
        """        
        self.layout = []

    def run_doctor_popup(self, doctor_obj):
        """Runs the doctor popup view.

        Args:
            doctor_obj (MedicalEmployee): An object of a specific doctor

        Returns:
            sg.Window: Adds a label and initialize the layout for the window.
        """        
        self.layout =  [
            [sg.Text('Doctor information: ')],
            [sg.Text([], key='doc_info')],
            [sg.Button('Remove doctor')]]
        window = sg.Window("Doctor", self.layout, finalize=True)
        window.Element('doc_info').update(doctor_obj)
        return window
