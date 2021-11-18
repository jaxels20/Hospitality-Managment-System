import server_handler_directory.ServerHandler as SH
import GUI.GuiHandler as GH
import threading






# #Run the server:
# serverhandler = SH.ServerHandler
# server_thread = threading.Thread(target = serverhandler.send_all_data)
#
# #The client recieves the data
#
# gui_handler = GH.GuiHandler()
#
# gui_thread = threading.Thread(target = gui_handler.retrieve_data())
# server_thread.start()
# gui_thread.start()
#
#
# server_thread.join()
# gui_thread.join()

gui_handler = GH.GuiHandler()
gui_handler.retrieve_data()

print(gui_handler.get_medical_db().get_all_medicine())

