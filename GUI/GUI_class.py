import GUI.login.login as li
import GUI.admin.mainAdminView as av
import GUI.doctor.mainDoctorView as dv
import GUI.nurse.mainNurseView as nv


class GUIClass:

    def __init__(self):
        self.login = li.LoginV()
        self.admin = av.AdminV()
        self.doctor = dv.DoctorV()
        self.nurse = nv.NurseV()
