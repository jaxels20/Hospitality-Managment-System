import PySimpleGUI as sg
import GUI.nurse.NurseView as nv
import GUI.nurse.NurseViewMedicine as nvm
import GUI.nurse.NurseViewPatient as nvp
import server_handler_directory.ServerHandler as ServerHandler


class NurseV:

    def __init__(self):
        self.data = []

    def run_nurse(self):
        # Creates a serverhandler
        sh = ServerHandler.ServerHandler()

        # Creates a window for admin view
        NurseView = nv.NurseView(sh).run_nurse_view()

        # Creates to attributes for windows.
        window1, window2 = NurseView, None


        while True:
            window, event, values = sg.read_all_windows()

            if event == sg.WIN_CLOSED or event == 'Logout':
                window.close()
                if window == window2:  # if closing win 2, mark as closed
                    window2 = None
                elif window == window1:  # if closing win 1, exit program
                    break
            elif event == '_PATIENT_':
                window2 = nvp.NurseViewPatient(sh).run_nurse_view_patient()
            elif event == '_MEDICAL_':
                window2 = nvm.NurseViewMedicine().run_nurse_view_medicine()

        window.close()
