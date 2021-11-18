import PySimpleGUI as sg


class AdminView:

    def __init__(self, srv_handler):
        self.__layout = [[sg.Button('Logout')],
              [sg.Text('Patients', size=(45, 1)), sg.Text('Doctors', size=(45, 1)), sg.Text('Nurses', size=(45, 1))],
              [sg.Listbox(srv_handler.get_patientdb().get_all_patients(), size=(50, 10),
                          enable_events=True, key='_PATIENT_'),
               sg.Listbox(srv_handler.get_empployeedb().get_all_doctors(), size=(50, 10),
                          enable_events=True, key='_DOCTOR_'),
               sg.Listbox(srv_handler.get_empployeedb().get_all_nurses(), size=(50, 10),
                          enable_events=True, key='_NURSE_')],
              [sg.Button('Add patient', size=(45, 1)), sg.Button('Add doctor', size=(45, 1)),
               sg.Button('Add nurse', size=(45, 1))]
              ]


    def run_admin_view(self):
        return sg.Window("Admin view", self.__layout, finalize=True)

# def run_admin(self, srv_handler):
#     layout =
#     window = sg.Window("Admin view", layout)
#     event, values = window.read()
#     while True:
#         if event == 'Add patient':
#             self.add_patient()
#             event, values = self.run_admin(srv_handler)
#         elif event == 'Add doctor':
#             self.add_doctor()
#             event, values = self.run_admin(srv_handler)
#         elif event == 'Add nurse':
#             self.add_nurse()
#             event, values = self.run_admin(srv_handler)
#         elif event == '_PATIENT_':
#             self.patient_popup(values)
#             event, values = self.run_admin(srv_handler)
#         elif event == '_DOCTOR_':
#             self.doctor_popup(values)
#             event, values = self.run_admin(srv_handler)
#         elif event == '_NURSE_':
#             self.nurse_popup(values)
#             event, values = self.run_admin(srv_handler)
#         else:
#             break
#
#     window.close()
#     return event, values
