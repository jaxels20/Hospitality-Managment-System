import socket


class GuiConnectionManager:
    """A class to run the the connection between the client and the server.
    """    
    def __init__(self):
        """Constructs all the nessecary attributes for the GuiConnetionManager object. 
        Note that some of this attributes can be changed but should not be in this program, but for future use this could be considered.
        """        
        self.__host = '127.0.0.1'
        self.__port = 4671
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def get_socket(self):
        """Retrieve the socket object.

        Returns:
            Socket: The socket in which the server runs.
        """        
        return self.__socket

    def get_port(self):
        """Retrieve the port object.

        Returns:
            Port: The port in which the server runs.
        """        
        return self.__port

    def get_host(self):
        """Retrieve the host object.

        Returns:
            Host: The host of the socket.
        """        
        return self.__host


