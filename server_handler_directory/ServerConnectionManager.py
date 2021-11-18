
import socket
import sys
import time

class ServerConnectionManager:
    def __init__(self):
        self.__host = '127.0.0.1'
        self.__port = 4670
        self.__BUFFSIZE = 1024
        self.__clients = {}
        self.__addresses = {}
        self.__ADDR = (self.__host, self.__port)
        self.__server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.__server.bind(self.__ADDR)

    def get_socket(self):
        return self.__server


connection_man =ServerConnectionManager()

with connection_man.get_socket() as s:
    s.listen()
    conn, addr = s.accept()
    with conn:
        while True:
            data = conn.recv(1024)
            print('connected')
            if not data:
                break
            conn.sendall(data)