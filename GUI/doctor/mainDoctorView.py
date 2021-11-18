import PySimpleGUI as sg
import GUI.doctor.DoctorView as dview
import GUI.doctor.DoctorViewPatient as dvp
import GUI.doctor.DoctorViewMedicine as dvm
import GUI.doctor.DoctorAddMedicine as dam
import GUI.doctor.DoctorConfirmAdd as dca
import server_handler_directory.ServerHandler as ServerHandler

# Creates a serverhandler
sh = ServerHandler.ServerHandler()

# Creates a window for admin view
DoctorView = dview.DoctorView(sh).run_doctor_view()

# Creates to attributes for windows.
window1, window2 = DoctorView, None


while True:
    window, event, values = sg.read_all_windows()

    if event == sg.WIN_CLOSED or event == 'Logout':
        window.close()
        if window == window2:  # if closing win 2, mark as closed
            window2 = None
        elif window == window1:  # if closing win 1, exit program
            break
    elif event == '_PATIENT_':
        window2 = dvp.DoctorViewPatient(sh).run_doctor_view_patient()
    elif event == '_MEDICAL_':
        window2 = dvm.DoctorViewMedicine().run_doctor_view_medicine()
    elif event == 'Add medicine':
        window2 = dam.DoctorAddMedicine(sh).run_doctor_add_medicine()
    elif event == '_MEDICINE_':
        window2 = dca.DoctorConfirmAdd().run_doctor_confirm_add()


window.close()
