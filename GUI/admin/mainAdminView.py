import PySimpleGUI as sg
import GUI.admin.AdminView as aview
import GUI.admin.AddPatientView as addp
import GUI.admin.AddDoctorView as addd
import GUI.admin.AddNurseView as addn
import GUI.admin.DoctorPopup as docp
import GUI.admin.NursePopup as nurp
import GUI.admin.PatientPopup as patp
import server_handler_directory.ServerHandler as ServerHandler


class AdminV:

    def __init__(self):
        self.data = []

    def run_admin(self):
        # Creates a serverhandler
        sh = ServerHandler.ServerHandler()

        # Creates a window for admin view
        AdminView = aview.AdminView(sh).run_admin_view()

        # Creates to attributes for windows.
        window1, window2 = AdminView, None


        while True:
            window, event, values = sg.read_all_windows()

            if event == sg.WIN_CLOSED or event == 'Exit':
                window.close()
                if window == window2:  # if closing win 2, mark as closed
                    window2 = None
                elif window == window1:  # if closing win 1, exit program
                    break
            elif event == 'Add patient' and not window2:
                window2 = addp.AddPatientView().run_add_patient_view()
            elif event == 'Save patient':
                sh.get_patientdb().create_patient(values['p_cpr'], values['p_name'], values['p_bloodtype'], values['p_birthdate'], values['p_height'])
                window1['_PATIENT_'].update(sh.get_patientdb().get_all_patients())
            elif event == 'Add doctor' and not window2:
                window2 = addd.AddDoctorView().run_add_doctor_view()
            elif event == 'Save doctor':
                sh.get_empployeedb().create_doctor(values['d_username'], values['d_password'], values['d_name'])
                window1['_DOCTOR_'].update(sh.get_empployeedb().get_all_doctors())
            elif event == 'Add nurse' and not window2:
                window2 = addn.AddNurseView().run_add_nurse_view()
            elif event == 'Save nurse':
                sh.get_empployeedb().create_nurse(values['n_username'], values['n_password'], values['n_name'])
                window1['_NURSE_'].update(sh.get_empployeedb().get_all_nurses())
            elif event == '_DOCTOR_':
                window2 = docp.DoctorPopup(values).run_doctor_popup()
            elif event == 'Remove doctor':
                sh.get_empployeedb().remove_doctor(values['doc_to_remove'])
                window1['_DOCTOR_'].update(sh.get_empployeedb().get_all_doctors())
            elif event == '_NURSE_':
                window2 = nurp.NursePopup(values).run_nurse_popup()
            elif event == 'Remove nurse':
                sh.get_empployeedb().remove_nurse(values['nur_to_remove'])
                window1['_NURSE_'].update(sh.get_empployeedb().get_all_nurses())
            elif event == '_PATIENT_':
                window2 = patp.PatientPopup(values).run_patient_popup()
            elif event == 'Remove patient':
                sh.get_patientdb().remove_patient(values['pat_to_remove'])
                window1['_PATIENT_'].update(sh.get_patientdb().get_all_patients())

        window.close()
