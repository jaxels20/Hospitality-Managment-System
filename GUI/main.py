import GUI.login as lg
import GUI.admin.AdminView as aview
import GUI.admin.AddPatientView as addp
import server_handler_directory.ServerHandler as ServerHandler

sh = ServerHandler.ServerHandler()
adminview = aview.AdminView(sh)
addpatient = addp.AddPatientView()

window = adminview.run_admin_view()

event, values = window.read()
window.close()

# new_login = lg.LoginView()
#
# event, values = new_login.run_login()
#
# while True:
#     if event == 'Cancel':
#         event, values = new_login.run_login()
#     else:
#         print("Login accepted")
#         break
#
# username, password = values['-username'], values['-password']
#
# print(username, password)