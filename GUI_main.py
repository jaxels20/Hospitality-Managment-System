import GUI.GuiHandler as GH


if __name__ == '__main__':
    gui_handler = GH.GuiHandler()
    gui_handler.retrieve_data()

    while True:
        gui_handler.create_gui()

        event, values = gui_handler.run_login_gui()
        if event is None:
            break
        usertype = gui_handler.get_gui().get_login_gui().verify_login(gui_handler.get_emp_db(), values['-username'], values['-password'])

        if usertype == 'verified admin':
            gui_handler.run_admin_gui()

        if usertype == 'verified doctor':
            gui_handler.run_doctor_gui()

        if usertype == 'verified nurse':
            gui_handler.run_nurse_gui()





    #gui_handler.run_gui()


