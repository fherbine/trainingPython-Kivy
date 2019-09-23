import queue
import select
import socket
import sys
import threading

from configuration import AVAILABLE_COMMANDS, PORT, HOST

class Client:
    """Classe controlleur du client.

    Elle gère principalement le lancement du service de récuperation des inputs
    utilisateurs, mais aussi la communication avec le serveur.
    """

    client_service = None
    run = True
    service_queue = None

    def __init__(self):
        self.start_client()

    def start_client(self):
        """On demarre le client."""
        self.client_connection = client_connection = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM,
        )
        print('Tentative de connexion au serveur ...')

        try:
            client_connection.connect((HOST, PORT))
        except:
            raise Exception('Le serveur est innaccessible !')

        print('Connexion établit avec le serveur.')

        self.service_queue = service_queue = queue.Queue()
        self.client_service = service = ClientService(service_queue)
        service.start()

        self.help()

    def run_client(self):
        """Boucle principale du client.

        Gère la lecture de la queue (pile FIFO) contenant les inputs claviers,
        la communication de ces informations avec le serveur, mais également,
        l'affichage des informations reçues.
        """
        while self.run:
            send_buffer = ''
            client_connection = self.client_connection
            rlist, wlist, xlist = select.select(
                [client_connection],
                [],
                [],
                .05
            )

            if rlist:
                output = client_connection.recv(1024).decode()

                if output:
                    print(output, end='')
                else:
                    self.run = False

            queue = self.service_queue

            while not queue.empty():
                send_buffer += queue.get()

            if send_buffer:

                if AVAILABLE_COMMANDS.get(send_buffer[0], '') == '%QUIT%':
                    self.run = False
                    break

                client_connection.send(send_buffer.encode())

        print('\nVous quittez le jeu...')
        self.stop()

    def stop(self):
        """Arrete le client."""
        self.client_connection.close()
        self.client_service.join()
        sys.exit(0)

    def help(self):
        """Affiche l'aide."""
        print('Les commandes disponnibles sont:')
        print('=== DEPLACEMENTS ===')
        print('- O: Se deplacer à l\'ouest.')
        print('- E: Se deplacer à l\'est.')
        print('- N: Se deplacer au nord.')
        print('- S: Se deplacer au sud.')
        print('=== ACTIONS ===')
        print('- P[direction]: Percer une porte dans un mur.')
        print('- M[direction]: Murer une porte.')
        print('=== AUTRES ===')
        print('- Q: Quitter le jeu.')


class ClientService(threading.Thread):
    """Thread permettant de récuperer les entrées utilisateurs.

    Utilise une Queue() FIFO(First In First Out) pour communiquer sans pertes
    de données avec la classe controlleur.
    """

    queue = None
    run = True

    def __init__(self, queue, *args, **kwargs):
        self.queue = queue
        super().__init__(*args, **kwargs)

    def run(self):
        while self.run:
            user_input = input()

            if user_input and user_input[0].upper() == 'Q':
                self.run = False

            self.queue.put(user_input)
