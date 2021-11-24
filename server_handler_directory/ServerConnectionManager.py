import socket


class ServerConnectionManager:
    """A class to run the connection between the server and clients.
    """    
    def __init__(self):
        """ Constructs all the necessary attributes for the ServerConnectionManager object.
        Notice that some of this attributes can be changed but should not be in this program, but for future use this
        could be considered
        """        
        self.__host = '127.0.0.1'
        self.__port = 4671
        self.__BUFFSIZE = 1024
        self.__ADDR = (self.__host, self.__port)
        self.__server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.__server.bind(self.__ADDR)

    def get_socket(self):
        """retrieve the socket object.

        Returns:
            Socket: The socket in which the server runs.
        """        
        return self.__server
