import PySimpleGUI as sg
import GUI.admin.AdminView as aview
import GUI.admin.AddPatientView as addp
import GUI.admin.AddDoctorView as addd
import GUI.admin.AddNurseView as addn
import GUI.admin.DoctorPopup as docp
import GUI.admin.NursePopup as nurp
import GUI.admin.PatientPopup as patp


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

            elif event == 'Add patient':
                window2 = self.__add_patient_view.run_add_patient_view()

            elif event == 'Save patient':
                window.close()
                patient_db.create_patient(values['p_cpr'], values['p_name'], values['p_bloodtype'],
                                          values['p_birthdate'], values['p_height'])
                window1['_PATIENT_'].update(patient_db.get_all_patients())

            elif event == 'Add doctor':
                window2 = self.__add_doctor_view.run_add_doctor_view()

            elif event == 'Save doctor':
                window.close()
                employee_db.create_doctor(values['d_username'], values['d_password'], values['d_name'])
                window1['_DOCTOR_'].update(employee_db.get_all_doctors())

            elif event == 'Add nurse':
                window2 = self.__add_nurse_view.run_add_nurse_view()

            elif event == 'Save nurse':
                window.close()
                employee_db.create_nurse(values['n_username'], values['n_password'], values['n_name'])
                window1['_NURSE_'].update(employee_db.get_all_nurses())

            elif event == '_DOCTOR_':
                selected_doctor = values['_DOCTOR_'][0]
                window2 = self.__doctor_popup.run_doctor_popup(selected_doctor)

            elif event == 'Remove doctor':
                window.close()
                employee_db.remove_doctor(selected_doctor)
                window1['_DOCTOR_'].update(employee_db.get_all_doctors())

            elif event == '_NURSE_':
                selected_nurse = values['_NURSE_'][0]
                window2 = self.__nurse_popup.run_nurse_popup(selected_nurse)

            elif event == 'Remove nurse':
                window.close()
                employee_db.remove_nurse(selected_nurse)
                window1['_NURSE_'].update(employee_db.get_all_nurses())

            elif event == '_PATIENT_':
                selected_patient = values['_PATIENT_'][0]
                window2 = self.__patient_popup.run_patient_popup(selected_patient)

            elif event == 'Remove patient':
                window.close()
                patient_db.remove_patient(selected_patient)
                window1['_PATIENT_'].update(patient_db.get_all_patients())

            elif event == 'Generate bill':
                selected_patient.get_financial_record().generate_bill(selected_patient)
                window2['_BILL_'].update(selected_patient.get_financial_record().get_patient_bill_list())

        window.close()

