import PySimpleGUI as sg


class AddPatientView:
    """Represents the view where an admin can add a patient.
    """
    def __init__(self):
        """Constructs all the necessary attributes for the AddPatientView object.
        """ 
        self.__layout = []


    def run_add_patient_view(self):
        """Runs the add patient view. 

        Returns:
            sg.Window: Adds a label and initialize the layout for the window.
        """   
        self.__layout = [
        [sg.Text('CPR', size=(8, 1)), sg.InputText(key='p_cpr')],
        [sg.Text('Name', size=(8, 1)), sg.InputText(key='p_name')],
        [sg.Text('Bloodtype', size=(8, 1)), sg.InputText(key='p_bloodtype')],
        [sg.Text('Birthdate', size=(8, 1)), sg.InputText(key='p_birthdate')],
        [sg.Text('Height', size=(8, 1)), sg.InputText(key='p_height')],
        [sg.Submit('Save patient'), sg.Exit("Exit")]]
        return sg.Window("Add patient view", self.__layout, finalize=True)
