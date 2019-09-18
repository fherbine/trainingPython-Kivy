import hashlib
import json
import os
import select
import signal
import socket
import sys

from getpass import getpass

from variables import HOST, PORT, PREFERED_HASH_ALGORITHM

class ClientsController:
    client_path = 'client.json'
    users = {}

    def create_new(self, name, password):
        self._read_users()

        if name in self.users:
            return False

        self.users[name] = {
            'password': self._hash_it(password),
            'messages': [],
        }

        self._write_users()

        return self.users[name]

    def connect(self, name, password):
        if not self._read_users():
            return False

        if name not in self.users:
            return False

        hashed_password = self._hash_it(password)

        user = self.users[name]

        if hashed_password == user['password']:
            return user

        return False

    def update_messages(self, name, messages):
        self.users[name]['messages'] = messages
        self._write_users()

    def _hash_it(self, words):
        available_algorithms = list(hashlib.algorithms_guaranteed)
        algorithm = available_algorithms[0]

        for prefered in PREFERED_HASH_ALGORITHM:
            if prefered in available_algorithms:
                algorithm = prefered
                break

        hash_function = getattr(hashlib, algorithm)

        return hash_function(words.encode()).hexdigest()

    def _read_users(self):
        client_path = self.client_path

        if not os.path.exists(client_path):
            return False

        with open(client_path) as clients_file:
            self.users = json.load(clients_file)

        return True

    def _write_users(self):
        client_path = self.client_path

        with open(client_path, 'w+') as clients_file:
            json.dump(self.users, clients_file)


class Client:
    run = True
    client_connection = None

    def __init__(self, messages):
        self.messages = messages
        self._load_previous_messages()

    def _load_previous_messages(self):
        messages = self.messages

        for message in messages:
            print(message)

    def _run_communication(self):
        signal.signal(signal.SIGINT, self._close)
        self.client_connection = client_connection = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM,
        )
        messages = self.messages

        try:
            client_connection.connect((HOST, PORT))
        except:
            raise Exception('Server unreachable.')

        while self.run:
            rlist, wlist, xlist = select.select(
                [client_connection],
                [],
                [],
                .05,
            )

            if rlist:
                rmessage = client_connection.recv(1024).decode()
                print(rmessage)
                self.messages.append(rmessage)

            message = input('>>> ')

            client_connection.send(message.encode())
            self.messages.append('>>> ' + message)

            if message == 'quit':
                self._close()

    def _close(self, *_):
        if self.client_connection:
            client_connection = self.client_connection
            client_connection.close()

        self.run = False

def get_usn_pwd():
    username = input('username: ')
    password = getpass()

    return username, password

if __name__ == '__main__':
    cli_controller = ClientsController()
    user = {}

    print('\n*======== MAXI TCHAT =========*\n')

    while True:
        print('1. sign in.')
        print('2. log in.')

        try:
            choice = int(input('\n>>>'))
        except:
            continue

        if choice not in (1, 2):
            continue

        ids = get_usn_pwd()

        if choice == 2:
            user = cli_controller.connect(*ids)

            if not user:
                print('User not found.')
                continue

        else:
            user = cli_controller.create_new(*ids)

            if not user:
                print('user already exists.')
                continue

        break

    name, _ = ids
    client = Client(user['messages'])
    client._run_communication()
    cli_controller.update_messages(name, client.messages)
