import PySimpleGUI as sg
import GUI.nurse.NurseView as nv
import GUI.nurse.NurseViewMedicine as nvm
import GUI.nurse.NurseViewPatient as nvp



class NurseGui:

    def __init__(self, patient_db):
        self.__nurse_view = nv.NurseView(patient_db)
        self.__nurse_view_medicine = nvm.NurseViewMedicine()
        self.__nurse_view_patient = nvp.NurseViewPatient()



    def run_nurse(self, patient_db):

        # Creates a window for admin view
        NurseView = self.__nurse_view.run_nurse_view()

        # Creates to attributes for windows.
        window1, window2 = NurseView, None


        while True:
            window, event, values = sg.read_all_windows()

            if event == sg.WIN_CLOSED or event == 'Logout' or event == 'Back':
                window.close()
                if window == window2:  # if closing win 2, mark as closed
                    window2 = None
                elif window == window1:  # if closing win 1, exit program
                    break
            elif event == '_PATIENT_':
                window2 = self.__nurse_view_patient.run_nurse_view_patient(values['_PATIENT_'][0])
            elif event == '_MEDICAL_':
                window2 = self.__nurse_view_medicine.run_nurse_view_medicine()

        window.close()
