import GUI.login as lg

new_login = lg.LoginView()

event, values = new_login.run_login()

while True:
    if event == 'Cancel':
        event, values = new_login.run_login()
    else:
        print("Login accepted")
        break

username, password = values['-username'], values['-password']

print(username, password)