import pickle
import socket

class GuiConnectionManager:
    def __init__(self):
        self.__host = '127.0.0.1'
        self.__port = 4671
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    def get_socket(self):
        return self.__socket

    def get_port(self):
        return self.__port

    def get_host(self):
        return self.__host


