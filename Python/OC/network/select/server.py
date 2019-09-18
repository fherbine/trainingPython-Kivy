import socket
import select
import signal
import sys

from variables import HOST, PORT

if __name__ == '__main__':
    clients_connected = []

    server_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_connection.bind(('', PORT))
    server_connection.listen(5)

    print('Server started on {host}:{port}'.format(host=HOST, port=PORT))

    def quit_server(signal, frame):
        print('\nClose requested for server...')
        close_clients_connections(clients_connected)
        server_connection.close()
        print('QUITING!')
        sys.exit(0)

    def close_clients_connections(clients):
        for client in clients:
            client['cli_co'].close()

    signal.signal(signal.SIGINT, quit_server)

    while True:
        rlist, wlist, xlist = select.select([server_connection], [], [], .05)

        if rlist:
            new_client_co, new_client_infos = server_connection.accept()
            clients_connected.append({
                'cli_co': new_client_co,
                'cli_infos': new_client_infos,
            })
            print('New client: ' + repr(new_client_infos))

        for client in clients_connected:
            client_connection, client_infos = list(client.values())

            pending_message, wlist, xlist = select.select(
                [client_connection],
                [],
                [],
                .5,
            )

            if pending_message:
                message = client_connection.recv(1024).decode()

                if message == 'quit':
                    client_connection.close()
                    clients_connected.pop(client)
                    continue

                confirm = 'Receive `{msg}` from {cli}'.format(
                    msg=message,
                    cli=repr(client_infos),
                )

                client_connection.send(('[SERVER] ' + confirm).encode())
                print(confirm)

