import PySimpleGUI as sg
import GUI.nurse.NurseView as nv
import GUI.nurse.NurseViewMedicine as nvm
import GUI.nurse.NurseViewPatient as nvp



class NurseGui:
    """Represents a class that handles all the different views that a nurse can see.
    """
    def __init__(self, patient_db):
        """Constructs all the necessary attributes for the NurseGui object.

        Args:
            patient_DB (PatientDB): A database of patients.
        """        
        self.__nurse_view = nv.NurseView(patient_db)
        self.__nurse_view_medicine = nvm.NurseViewMedicine()
        self.__nurse_view_patient = nvp.NurseViewPatient()



    def run_nurse(self):
        """Runs the nurse gui. Creates three variables which can hold the windows that are shown
        to the user. At first one of the windows are set to the first nurse view. The while loop
        handles all the events that can happen when a user clicks on different elements in 
        one of the windows that can be shown. 

        Args:
            patient_db (PatientDB): A database of patients.
        """        
        NurseView = self.__nurse_view.run_nurse_view()

        window1, window2, window3 = NurseView, None, None


        while True:
            window, event, values = sg.read_all_windows()

            if event == sg.WIN_CLOSED or event == 'Logout' or event == 'Back':
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
                    window3 = self.__nurse_view_patient.run_nurse_view_patient(selected_patient)
            elif event == '_MEDICAL_':
                if len(values['_MEDICAL_']) != 0:
                    selected_medicine = values['_MEDICAL_'][0]
                    window2 = self.__nurse_view_medicine.run_nurse_view_medicine()
            elif event == 'Save mark':
                if values['mark_as_filled'] is True:
                    selected_medicine.mark_as_filled()
                    window.close()
                    window3['_MEDICAL_'].update(selected_patient.get_medical_record().get_patient_medical_list())

        window.close()
