import PySimpleGUI as sg
import GUI.doctor.DoctorView as dview
import GUI.doctor.DoctorViewPatient as dvp
import GUI.doctor.DoctorViewMedicine as dvm
import GUI.doctor.DoctorAddMedicine as dam
import GUI.doctor.DoctorConfirmAdd as dca


class DoctorGui:
    """Represents a class that handles all the different views that a doctor can see.
    """
    def __init__(self, patient_DB):
        """Constructs all the necessary attributes for the DoctorGui object.

        Args:
            patient_DB (PatientDB): A database of patients.
            medical_DB (EmployeeDB): A database of medical employees.
        """        
        self.__doctor_view = dview.DoctorView(patient_DB)
        self.__doctor_view_patient = dvp.DoctorViewPatient()
        self.__doctor_view_medicine = dvm.DoctorViewMedicine()
        self.__doctor_add_medicine = dam.DoctorAddMedicine()
        self.__confirm_add = dca.DoctorConfirmAdd()

    def run_doctor(self, medical_DB):
        """Runs the doctor gui. Creates three variables which can hold the windows that are shown
        to the user. At first one of the windows are set to the first doctor view. The while loop
        handles all the events that can happen when a user clicks on different elements in 
        one of the windows that can be shown. 

        Args:
            patient_DB (PatientDB): A database of patients.
            medical_DB (EmployeeDB): A database of medical employees.
        """        
        DoctorView = self.__doctor_view.run_doctor_view()

        window1, window2, window3 = DoctorView, None, None


        while True:
            window, event, values = sg.read_all_windows()

            if event == sg.WIN_CLOSED or event == 'Logout' or event == 'Back' or event == 'Cancel':
                window.close()
                if window == window2: 
                    window2 = None
                elif window == window3:
                    window3 = None
                elif window == window1:
                    break
            elif event == '_PATIENT_':
                if len(values['_PATIENT_']) != 0:
                    selected_patient = values['_PATIENT_'][0]
                window3 = self.__doctor_view_patient.run_doctor_view_patient(selected_patient)
            elif event == '_MEDICAL_':
                if len(values['_MEDICAL_']) != 0:
                    selected_medicine = values['_MEDICAL_'][0]
                    window2 = self.__doctor_view_medicine.run_doctor_view_medicine()
            elif event == 'Add medicine':
                window2 = self.__doctor_add_medicine.run_doctor_add_medicine(medical_DB)
            elif event == '_MEDICINE_':
                if len(values['_MEDICINE_']) != 0:
                    medicine = values['_MEDICINE_'][0]
                    window2 = self.__confirm_add.run_doctor_confirm_add()
            elif event == 'Add':
                window.close()
                selected_patient.get_medical_record().add_medicine(medicine)
                window3['_MEDICAL_'].update(selected_patient.get_medical_record().get_patient_medical_list())
            elif event == 'Save mark':
                if values['mark_as_filled'] is True:
                    selected_medicine.mark_as_filled()
                    window.close()
                    window3['_MEDICAL_'].update(selected_patient.get_medical_record().get_patient_medical_list())
            elif event == 'Remove medicine':
                selected_patient.get_medical_record().remove_medicine(selected_medicine)
                window.close()
                window3['_MEDICAL_'].update(selected_patient.get_medical_record().get_patient_medical_list())

        window.close()
