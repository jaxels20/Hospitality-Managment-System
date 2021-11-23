import GUI.login.LoginGui as lg
import GUI.admin.AdminGui as av
import GUI.doctor.DoctorGui as dv
import GUI.nurse.NurseGui as nv


class Gui:

    def __init__(self, medical_db, patient_db, emp_db):
        self.__login_gui = lg.LoginGui()
        self.__admin_gui = av.AdminGui(patient_db, emp_db)
        self.__doctor_gui = dv.DoctorGui(patient_db, medical_db)
        self.__nurse_gui = nv.NurseGui(patient_db)

    def get_doctor_gui(self):
        return self.__doctor_gui

    def get_nurse_gui(self):
        return self.__nurse_gui

    def get_admin_gui(self):
        return self.__admin_gui

    def get_login_gui(self):
        return self.__login_gui