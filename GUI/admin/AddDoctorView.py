import PySimpleGUI as sg


class AddDoctorView:
    """Represents the view where an admin can add a doctor.
    """
    def __init__(self):
        """Constructs all the necessary attributes for the AddDoctorView object.
        """        
        self.__layout = []


    def run_add_doctor_view(self):
        """Runs the add doctor view. 

        Returns:
            sg.Window: Adds a label and initialize the layout for the window.
        """        
        self.__layout = [
            [sg.Text('Name', size=(8, 1)), sg.InputText(key='d_name')],
            [sg.Text('Username', size=(8, 1)), sg.InputText(key='d_username')],
            [sg.Text('Password', size=(8, 1)),
             sg.InputText('', key='d_password', password_char='*')],
            [sg.Submit('Save doctor'), sg.Exit("Exit")]]
        return sg.Window("Add doctor view", self.__layout, finalize=True)