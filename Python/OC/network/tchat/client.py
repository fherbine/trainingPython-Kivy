# client
import socket
from variables import PORT, HOST

class Client():
    def __init__(self, debug=False):
        self.debug = debug
        self.client_connection = socket.socket()
        self.client_connection.connect((HOST, PORT))

    def get_message(self):
        buffered = True
        message = ''
        buffered = self.client_connection.recv(1024)
        message = buffered.decode()

        return message

    def send_message(self, msg='h'):
        self.client_connection.send(msg.encode())

    def close_all(self):
        self.send_message('q')
        self.client_connection.close()
