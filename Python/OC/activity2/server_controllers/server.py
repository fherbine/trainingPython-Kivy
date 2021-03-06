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

    clients = []
    current_player = 0
    game_map = None
    server_connection = None

    def __init__(self):
        self.get_map()
        self.start_server()

    def get_map(self):
        """On demarre l'interface utilisateur pour la partie serveur.

        On récupère un objet Map, qui est le labyrinthe."""
        map_path = ServerIhm().get_map()
        self.game_map = GameMap(map_path)

    def start_server(self):
        """Demarre le server.

        Initialise le socket, ecoute en local sur le port indiqué dans
        `configuration.py`
        """
        server_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_connection.bind(('', PORT))
        server_connection.listen(5)
        self.server_connection = server_connection
        self.run = True
        signal.signal(signal.SIGINT, self._stop_running)
        print('Le serveur est démarré !')
        print('`Ctrl+C`: pour arreter le serveur.')

    def run_server(self):
        """Methode principale du serveur.

        Boucle sur les methodes/fonctions permettant la connection,
        la communication, et le traitement des données coté serveur.
        """
        server_connection = self.server_connection

        while self.run:
            client_available, wlist, xlist = select.select(
                [server_connection],
                [],
                [],
                .05
            )

            if client_available:
                client_is_added = self._add_new_client()

                if not client_is_added:
                    continue

            for client_id, client_data in enumerate(self.clients):
                recv_buffer = ''
                client_connection = client_data['connection']
                player = client_data['player']
                rlist, wlist, xlist = select.select(
                    [client_connection],
                    [],
                    [],
                    .05,
                )

                if rlist:
                    recv_buffer = client_connection.recv(1024).decode()

                if client_id == self.current_player and recv_buffer:
                    running = self._get_current_client_cmd(
                        client_data,
                        player,
                        recv_buffer,
                    )

                    if not running:
                        return

                    self._send_game_map_to_players()
        self.stop_server()

    def _get_current_client_cmd(self, client_data, player, recv_buffer):
        """Ecoute les entrees utilisateur, recupère l'entrée utilisateur brute.

        Envoie cette entrée au differentes methodes de parsing/traitement.
        """
        command = None
        client_connection = client_data['connection']

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
                recv_buffer = client_connection.recv(1024).decode()
                continue

            if command == '%QUIT%':
                # commande spéciale traité depuis cette classe
                # elle est appelé lorsqu'un utilisateur quitte la partie.
                game_map = self.game_map
                game_map.remove_player(player)
                client_connection.close()
                self.clients.remove(client_data)
                self._send_message_to_all_players(
                    '`%s` a quitté le jeu !' % player
                )
            else:
                # on execute les autres commandes au sein de la GameMap.
                game_map = self.game_map
                cmd_done, return_code = game_map.eval_command(
                    player,
                    command,
                    args,
                )

                if return_code == '%WIN%':
                    # Si la dernière action a fait gagné l'utilisateur.
                    self._send_message_to_all_players(
                        '\n`%s` a gagné la partie !\n' % player
                    )
                    self._send_game_map_to_players()
                    self.run = False
                    self.stop_server()
                    return False

                elif cmd_done:
                    # On change d'utilisateur courant.
                    if self.current_player + 1 < len(self.clients):
                        self.current_player += 1
                    else:
                        self.current_player = 0
                else:
                    # Si la commande a échoué.
                    self._send_message_to_client(
                        client_connection,
                    'Commande impossible: `%s` !\n' % recv_buffer
                    )
        return True

    def _add_new_client(self):
        """On ajoute un nouveau client."""
        server_connection = self.server_connection
        game_map = self.game_map

        client_connection, _ = server_connection.accept()
        self.current_player = len(self.clients)
        # on génère un skin pour le nouvel utilisateur.
        skin = game_map.generate_player_skin()

        if not skin:
            client_connection.send(b'Le serveur est complet !\n')
            client_connection.close()
            return False

        game_map.add_player(skin)

        # on l'ajoute à notre attribut(lite) `self.clients`
        self.clients.append({
            'player': skin,
            'connection': client_connection,
        })
        self._send_message_to_client(
            client_connection,
            'Bienvenue, votre skin est le suivant: `%s` !\n' % skin
        )
        self._send_game_map_to_players()
        return True

    def _send_prompt_to_current_client(self):
        """Envoie le 'prompt', `>>>` au client courant."""
        if not self.clients:
            return

        client_connection = self.clients[self.current_player]['connection']
        client_connection.send(b'>>>')

    def _send_game_map_to_players(self):
        """On envoie la carte aux joueurs."""
        for client_id, client_data in enumerate(self.clients):
            recv_buffer = ''
            client_connection = client_data['connection']
            player = client_data['player']
            rlist, wlist, xlist = select.select(
                [client_connection],
                [],
                [],
                .05,
            )
            game_map = self.game_map
            # On génère une carte spécifique pour chaque utilisateur.
            map_buffer = game_map.get_player_map(player)
            self._send_message_to_client(client_connection, map_buffer)
        self._send_prompt_to_current_client()

    def _send_message_to_all_players(self, message):
        """Envoie un message à tous les joueurs."""
        for client_id, client_data in enumerate(self.clients):
            recv_buffer = ''
            client_connection = client_data['connection']
            player = client_data['player']
            rlist, wlist, xlist = select.select(
                [client_connection],
                [],
                [],
                .05,
            )
            self._send_message_to_client(client_connection, message)

    def _send_message_to_client(self, client_connection, message):
        """Envoie un message à un client en particulier."""
        client_connection.send(message.encode())

    def _stop_running(self, *_):
        self.run = False

    def stop_server(self):
        """On arrete le serveur."""
        self._close_client_connections()
        self.server_connection.close()
        self.server_connection = None

    def _close_client_connections(self):
        """Ferme les connexions des clients."""
        clients_connections= [
            client_data['connection'] for client_data in self.clients
        ]
        for client_connection in clients_connections:
            client_connection.close()


class GameCommands:
    """Classe permettant le parsing des commandes.

    Commandes brutes > assemblage d'une commande et d'arguments.
    """

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
