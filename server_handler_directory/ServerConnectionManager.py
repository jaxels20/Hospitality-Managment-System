
import socket
import sys
import time

class ServerConnectionManager:
    def __init__(self):
        self.__host = '127.0.0.1'
        self.__port = 4671
        self.__BUFFSIZE = 1024
        self.__ADDR = (self.__host, self.__port)
        self.__server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.__server.bind(self.__ADDR)

    def get_socket(self):
        return self.__server
