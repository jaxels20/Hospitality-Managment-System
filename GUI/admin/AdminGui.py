import PySimpleGUI as sg
import GUI.admin.AdminView as aview
import GUI.admin.AddPatientView as addp
import GUI.admin.AddDoctorView as addd
import GUI.admin.AddNurseView as addn
import GUI.admin.DoctorPopup as docp
import GUI.admin.NursePopup as nurp
import GUI.admin.PatientPopup as patp
import re


class AdminGui:

    def __init__(self, patient_db, employee_db):
        self.__admin_view = aview.AdminView(patient_db, employee_db)
        self.__add_patient_view = addp.AddPatientView()
        self.__add_doctor_view = addd.AddDoctorView()
        self.__add_nurse_view = addn.AddNurseView()
        self.__doctor_popup = docp.DoctorPopup()
        self.__nurse_popup = nurp.NursePopup()
        self.__patient_popup = patp.PatientPopup()

    def run_admin(self, patient_db, employee_db):
        AdminView = self.__admin_view.run_admin_view()

        # Creates to attributes for windows.
        window1, window2 = AdminView, None

        while True:
            window, event, values = sg.read_all_windows()

            if event == sg.WIN_CLOSED or event == 'Exit' or event == 'Logout':
                window.close()
                if window == window2:  # if closing win 2, mark as closed
                    window2 = None
                elif window == window1:  # if closing win 1, exit program
                    break

            elif event == 'Add patient' and not window2:
                window2 = self.__add_patient_view.run_add_patient_view()

            elif event == 'Save patient':
                patient_db.create_patient(values['p_cpr'], values['p_name'], values['p_bloodtype'],
                                          values['p_birthdate'], values['p_height'])
                window1['_PATIENT_'].update(patient_db.get_all_patients())

            elif event == 'Add doctor' and not window2:
                window2 = self.__add_doctor_view.run_add_doctor_view()

            elif event == 'Save doctor':
                employee_db.create_doctor(values['d_username'], values['d_password'], values['d_name'])
                window1['_DOCTOR_'].update(employee_db.get_all_doctors())

            elif event == 'Add nurse' and not window2:
                window2 = self.__add_nurse_view.run_add_nurse_view()

            elif event == 'Save nurse':
                employee_db.create_nurse(values['n_username'], values['n_password'], values['n_name'])
                window1['_NURSE_'].update(employee_db.get_all_nurses())

            elif event == '_DOCTOR_':
                window2 = self.__doctor_popup.run_doctor_popup()

            elif event == 'Remove doctor':
                employee_db.remove_doctor(values['doc_to_remove'])
                window1['_DOCTOR_'].update(employee_db.get_all_doctors())

            elif event == '_NURSE_':
                window2 = self.__nurse_popup.run_nurse_popup()

            elif event == 'Remove nurse':
                employee_db.remove_nurse(values['nur_to_remove'])
                window1['_NURSE_'].update(employee_db.get_all_nurses())

            elif event == '_PATIENT_':
                window2 = self.__patient_popup.run_patient_popup(values['_PATIENT_'][0])

            elif event == 'Remove patient':
                patient_db.remove_patient(values['pat_to_remove'])
                window1['_PATIENT_'].update(patient_db.get_all_patients())

        window.close()

