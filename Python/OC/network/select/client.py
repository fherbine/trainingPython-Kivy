import socket
import select
import sys

from variables import HOST, PORT

class Client:
    def run_communication(self):
        self.client_connection = client_connection = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM,
        )

        try:
            client_connection.connect((HOST, PORT))
        except:
            raise Exception('Server unreachable.')

        while True:
            rlist, wlist, xlist = select.select(
                [client_connection],
                [],
                [],
                .05,
            )

            if rlist:
                rmessage = client_connection.recv(1024).decode()
                print(rmessage)

            message = input('>>> ')

            client_connection.send(message.encode())

            if message == 'quit':
                self.close()

    def close(self):
        client_connection = self.client_connection
        client_connection.close()
        sys.exit(0)



if __name__ == '__main__':
    Client().run_communication()
