import GUI.login.login as li
import GUI.admin.mainAdminView as av
import GUI.doctor.DoctorGui as dv
import GUI.nurse.mainNurseView as nv


class GUIClass:

    def __init__(self, medical_db, patient_db, emp_db):
        self.__login_gui = li.LoginV()
        self.__admin_gui = av.AdminV()
        self.__doctor_gui = dv.DoctorGui(patient_db, medical_db)
        self.__nurse_gui = nv.NurseV()

    def get_doctor_gui(self):
        return self.__doctor_gui



