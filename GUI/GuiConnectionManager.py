import pickle
import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 4670       # The port used by the server
#
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.connect((HOST, PORT))
#     s.sendall(b'')
#     data = s.recv(1024)
#     #data_variable = pickle.loads(data)
#     print(data)