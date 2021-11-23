import GUI.login.LoginGui as lg
import GUI.admin.AdminGui as av
import GUI.doctor.DoctorGui as dv
import GUI.nurse.NurseGui as nv


class Gui:
    """Reprecents a class that combine all the guis for admin, nurses and doctors.
    """    

    def __init__(self, medical_db, patient_db, emp_db):
        """Constructs all the necessary attributes for the GUI object.

        Args:
            medical_db (Medical_DB): A database for medicine
            patient_db (PatientDB): A database for patients.
            emp_db (EmployeeDB): A database for medical employees.
        """        
        self.__login_gui = lg.LoginGui()
        self.__admin_gui = av.AdminGui(patient_db, emp_db)
        self.__doctor_gui = dv.DoctorGui(patient_db, medical_db)
        self.__nurse_gui = nv.NurseGui(patient_db)

    def get_doctor_gui(self):
        """Retrieve the doctor gui.

        Returns:
            DoctorGui: An object of the doctor Gui.
        """        
        return self.__doctor_gui

    def get_nurse_gui(self):
        """Retrieve the nurse gui.

        Returns:
            NurseGui: An object of the nurse Gui.
        """ 
        return self.__nurse_gui

    def get_admin_gui(self):
        """Retrieve the admin gui.

        Returns:
            AdminGui: An object of the admin Gui.
        """ 
        return self.__admin_gui

    def get_login_gui(self):
        """Retrieve the login gui.

        Returns:
            LoginGui: An object of the login Gui.
        """ 
        return self.__login_gui