import PySimpleGUI as sg
import GUI.doctor.DoctorView as dview
import GUI.doctor.DoctorViewPatient as dvp
import GUI.doctor.DoctorViewMedicine as dvm
import GUI.doctor.DoctorAddMedicine as dam
import GUI.doctor.DoctorConfirmAdd as dca


class DoctorGui:

    def __init__(self, patient_DB, medical_DB):
        self.__doctor_view = dview.DoctorView(patient_DB)
        self.__doctor_view_patient = dvp.DoctorViewPatient()
        #ovnstående virker men gør ikke det den skal kan ikke se patient medical record
        self.__doctor_view_medicine = dvm.DoctorViewMedicine()
        self.__doctor_add_medicine = dam.DoctorAddMedicine()
        self.__confirm_add = dca.DoctorConfirmAdd()

    def run_doctor(self, patient_DB, medical_DB):
        DoctorView = self.__doctor_view.run_doctor_view()

        # Creates to attributes for windows.
        window1, window2 = DoctorView, None


        while True:
            window, event, values = sg.read_all_windows()

            if event == sg.WIN_CLOSED or event == 'Logout' or event == 'Back' or event == 'Cancel':
                window.close()
                if window == window2:  # if closing win 2, mark as closed
                    window2 = None
                elif window == window1:  # if closing win 1, exit program
                    break
            elif event == '_PATIENT_':
                selected_patient = values['_PATIENT_'][0]
                window2 = self.__doctor_view_patient.run_doctor_view_patient(selected_patient)
            elif event == '_MEDICAL_':
                window2 = self.__doctor_view_medicine.run_doctor_view_medicine()
            elif event == 'Add medicine':
                window2 = self.__doctor_add_medicine.run_doctor_add_medicine(medical_DB)
            elif event == '_MEDICINE_':
                medicine = values['_MEDICINE_'][0]
                print(medicine)
                window2 = self.__confirm_add.run_doctor_confirm_add()
            elif event == 'Add':
                selected_patient.get_medical_record().add_medicine(medicine)






        window.close()
