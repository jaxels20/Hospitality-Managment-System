import PySimpleGUI as sg
import GUI.admin.AdminView as aview
import GUI.admin.AddPatientView as addp
import server_handler_directory.ServerHandler as ServerHandler

# Creates a serverhandler
sh = ServerHandler.ServerHandler()

# Creates a window for admin view
AdminView = aview.AdminView(sh).run_admin_view()

# Creates to attributes for windows.
window1, window2 = AdminView, None


while True:
    window, event, values = sg.read_all_windows()

    if event == sg.WIN_CLOSED:
        window.close()
        if window == window2:  # if closing win 2, mark as closed
            window2 = None
        elif window == window1:  # if closing win 1, exit program
            break
    elif event == 'Add patient' and not window2:
        window2 = addp.AddPatientView().run_addpatientview()
    elif event == 'Save patient':
        print(values)
        sh.get_patientdb().create_patient(values['p_name'])

window.close()
