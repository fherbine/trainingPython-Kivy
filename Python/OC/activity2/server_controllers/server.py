import os

from configuration import MAPS_PATH

class Server:
    """Controlleur serveur.
    
    Cette classe permet de controller tout ce qui est relatif au serveur.
    Excepté la gestion graphique du labyrinthe, et la logique de déplacement,
    des joueurs.
    """

    def get_map(self):
        """On demarre l'interface utilisateur pour la partie serveur.
        
        On récupère un objet Map, qui est le labyrinthe."""
        map_path = ServeurIhm().get_map()


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

            if selected_map > len(maps) or selected_map < 1:
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
