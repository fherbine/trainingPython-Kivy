import os
import select
import signal
import socket

from configuration import (
    AVAILABLE_COMMANDS,
    MAPS_PATH,
    PORT,
)
from server_controllers.game_map import GameMap

class Server:
    """Controlleur serveur.

    Cette classe permet de controller tout ce qui est relatif au serveur.
    Excepté la gestion graphique du labyrinthe, et la logique de déplacement,
    des joueurs.
    """

    clients = {}
    game_map = None
    server_connection = None
    current_player = 0

    def __init__(self):
        self.get_map()
        self.start_server()

    def get_map(self):
        """On demarre l'interface utilisateur pour la partie serveur.

        On récupère un objet Map, qui est le labyrinthe."""
        map_path = ServerIhm().get_map()
        self.game_map = GameMap(map_path)

    def start_server(self):
        server_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_connection.bind(('', PORT))
        server_connection.listen(5)
        self.server_connection = server_connection
        self.run = True
        signal.signal(signal.SIGINT, self._stop_running)
        print('Le serveur est démarré !')
        print('`Ctrl+C`: pour arreter le serveur.')

    def run_server(self):
        server_connection = self.server_connection

        while self.run:
            client_available, wlist, xlist = select.select(
                [server_connection],
                [],
                [],
                .05
            )

            if client_available:
                game_map = self.game_map
                client_connection, client_infos = server_connection.accept()
                client_infos = str(client_infos)
                self.current_player = len(self.clients)
                skin = game_map.generate_player_skin()

                if not skin:
                    client_connection.send(b'Le serveur est complet !\n')
                    client_connection.close()
                    continue

                player = game_map.add_player(skin)

                self.clients.append({
                    'player': player,
                    'connection': client_connection,
                })
                self.send_message_to_client(
                    'Bienvenue, votre skin est le suivant: `%s` !\n' % skin
                )

            for client_id, client_data in enumerate(self.clients):
                recv_buffer = ''
                client_connection = client_data['client_connection']
                player = client_data['player']
                rlist, wlist, xlist = select.select(
                    [client_connetion],
                    [],
                    [],
                    .05,
                )

                if rlist:
                    recv_buffer = client_connetion.recv(1024).decode()

                if client_id == self.current_player and recv_buffer:
                    command = None

                    while command is None:
                        command, args = GameCommands().parse_command(
                            recv_buffer
                        )

                        if command is None:
                            client_connection.send((
                                'Commande inexistante `%s`' % recv_buffer
                            ).encode())
                            # ici on peut bloquer la connexion puisque on ne
                            # peut pas continuer si le client actif
                            # ne saisie pas une commande valide.
                            recv_buffer = client_connetion.recv(1024).decode()
                            continue

                        if command == '%QUIT%':
                            game_map = self.game_map
                            game_map.remove_player(player)
                            client_connection.close()
                            self.send_message_to_all_players(
                                '`%s` a quitté le jeu !' % player.skin
                            )
                        else:
                            game_map = self.game_map
                            game_map.eval_command(player, command, args)

                    self.send_game_map_to_players()
        self.stop_server()

    def send_game_map_to_players(self):
        game_map = self.game_map
        map_buffer = game_map.get_player_map(player)
        self.send_game_map_to_players(map_buffer)

    def send_message_to_all_players(self, message):
        for client_id, client_data in enumerate(self.clients):
            recv_buffer = ''
            client_connection = client_data['client_connection']
            player = client_data['player']
            rlist, wlist, xlist = select.select(
                [client_connetion],
                [],
                [],
                .05,
            )
            self.send_message_to_client(client_connetion, message)

    def send_message_to_client(self, client_conection, message):
        client_connection.send(message.encode())

    def _stop_running(self, *_):
        self.run = False

    def stop_server(self):
        self._close_client_connections()
        self.server_connection.close()
        self.server_connection = None

    def _close_client_connections(self):
        clients_connections= [
            client_data['client_connection'] for client_data in self.clients
        ]
        for client_connection in clients_connections:
            client_connection.close()

    def refuse_client(self, client):
        pass

    def add_player(self):
        pass

    def exec_client_game_cmd(self, client_infos, cmd):
        client_data = self.clients.get(client_infos)
        player = client_data['player']


class GameCommands:
    command = []

    def parse_command(self, command_line):
        if not command_line:
            return None, None

        cmd = command_line[0].upper()
        args = command_line[1:].upper()

        if self._command_is_available(cmd):
            return AVAILABLE_COMMANDS[cmd], args

        return None, None

    def _command_is_available(self, cmd):
        return cmd in AVAILABLE_COMMANDS


class ServerIhm:
    """Interface machine pour le controlleur serveur.

    Cette interface sert UNIQUEMENT pour la selection de du labyrithe coté
    serveur.
    """

    maps = []
    maps_path = MAPS_PATH

    def get_map(self, pre_selected=None):
        """On recupère la chemin vers la carte choisie par l'utilisaeur.

        Si l'input est invalide on boucle, si le nombre entré ne correspond
        à aucune carte, on boucle.

        Sinon, on retourne le chemin vers la carte.

        L'argument pre_selected, peut nous permettre de présélectionner un
        labyrinthe.
        """
        self._list_maps()
        selected_map = pre_selected
        maps = self.maps

        while selected_map is None:
            selected_map = input(
                'Entrez un nombre pour choisir un labyrithe: '
            )

            try:
                selected_map = int(selected_map)
            except:
                print('Ceci n\'est pas un nombre...')
                selected_map = None
                continue

            if selected_map > len(maps) or selected_map < 0:
                print('Merci d\'entrer un nombre valide!')
                selected_map = None
                continue

            break

        return maps[selected_map]['path']


    def _list_maps(self):
        """Liste les maps."""
        self._get_maps()
        maps = self.maps

        print('Labyrinthes existants:')

        for index, map_infos in enumerate(maps):
            print('{} - {}'.format(index, map_infos['name']))

    def _get_maps(self):
        """Recupère les maps.

        Elle doivent etre contenues dans le repertoire, précisé dans la gloable
        MAPS_PATH. par defaut `cartes`. Voir `configuration.py`

        Le tout est stocké dans l'attribut :maps:, sous la forme:
        [
            {
                'name': 'nom1',
                'path': 'cartes/nom1.txt',
            },
            {
                'name': 'nom2',
                'path': 'cartes/nom2.txt',
            },
            <...>
        ]
        """
        maps = []

        if not os.path.exists(self.maps_path):
            raise Exception('Pas de dossier: `{}`'.format(
                self.maps_path
            ))
            sys.exit(0)

        for map_file in os.listdir(self.maps_path):
            if map_file.endswith('.txt'):
                maps.append({
                    'name': map_file.split('.')[0],
                    'path': os.path.join(self.maps_path, map_file),
                })

        if not maps:
            raise Exception('Aucun labyrinthes trouvé dans `{}`'.format(
                self.maps_path
            ))

        self.maps = maps
