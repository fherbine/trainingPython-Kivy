# server part
import socket

from variables import PORT, CMDS

class Server():
    def __init__(self):
        self.server_connection = None
        self.start()

    def start(self):
        self.server_connection = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM,
        )

        # socket.socket(family=AF_INET, TYPE=SOCK_STREAM, *osef)
        # family = adress family >>
        #   - AF_UNIX, AF_LOCAL (Local communications),
        #   - AF_INET (InterNET IPv4),
        #   - AF_INET6 (InterNET IPv6),
        #####
        # type = type of com (stream or datagram)
        # SOCK_STREAM (def.) for TCP, SOCK_DGRAM (UDP)

        connection = self.server_connection
        connection.bind(('', PORT))
        connection.listen(5)
        self.client_infos = connection.accept()

        self.run()

    def run(self):
        client_connection, client_information = self.client_infos

        while True:
            buffered_infos = client_connection.recv(1024)

            if buffered_infos:
                output = self._cmd(buffered_infos)
                client_connection.send(output.encode())

                if output == 'QUIT':
                    break
            
    def stop(self):
        self.server_connection.close()
        self.server_connection = None

    def reset(self):
        self.stop()
        self.start()

    def _parse(self, msg):
        msg = msg.decode()
        cmd = msg.split(' ')
        return cmd

    def _cmd(self, msg):
        args = self._parse(msg)
        cmd = args[0]

        if cmd not in CMDS or not hasattr(self, CMDS[cmd]):
            return self._help()
        
        command_function = getattr(self, CMDS[cmd])

        return command_function(args[1:])

    def _help(self, *_):
        help_message = 'Available command are:\n- m [msg]:  for message,\n- h: for help,\n- q: to close connection'
        return help_message

    def _msg(self, arg):
        return ' '.join(arg)

    def _quit(self, *_):
        self.stop()

        return 'QUIT'
