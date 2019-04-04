# -*-coding:Utf-8 -*

"""Ce module contient la classe Labyrinthe."""


# dict() faisant correspondre les direction a des mouvement en tuples
# de coordonnees cartesiennes & dict() faisant correspondres des noms de classes
# (element_carte.py) a des caracteres ASCII

moves = {'N': (0, -1), 'E': (1, 0), 'S': (0, 1), 'O': (-1, 0)}
static_elems = {'Porte': '.', 'Mur': 'O', 'Arrivee': 'U'}

class Labyrinthe:

    """Classe représentant un labyrinthe."""

    def __init__(self, map_objects):
        """Constructeur de la classe Labyrinthe en prends en compte:
            - map_objects, labyrinthe de l' objet Carte
            - les dimensions de la map extraite de map_objects
            - player pointe vers l'objet Personnage de map_objects
            - win, un attribut permettant de connaitre le moment où l'on gagne
        """
        self._map_dimensions = map_objects.labyrinthe['dimensions']
        del map_objects.labyrinthe['dimensions']
        self._map_objects = map_objects.labyrinthe
        self._player = self._map_objects['Personnage'][0]
        self._win = False

    def _from_map_to_str(self):
        """Methode permettant la conversion de notre map en string."""
        # on recupere les dimensions de la map pour en faire un premier tableau
        # 2D
        tx, ty = self._map_dimensions
        tmp_map = [[' ' for _ in range(tx)] for _ in range(ty)]

        # on ajoute les caracteres ASCII correspondant a nos objets et leurs
        # position dans le tableau.
        for elem_class, elems in self._map_objects.items():
            if elem_class == 'Personnage':
                continue
            for elem in elems:
                x, y = elem.position
                tmp_map[y][x] = static_elems[elem_class]

        # on ajoute le joueur apres pour etre sûr qu'en cas de superposition il
        # se trouve encore au premier plan
        x, y = self._player.position
        tmp_map[y][x] = 'X'

        #on compresse le tableau 2D en chaine de caractere
        tmp_map = '\n'.join([''.join(line) for line in tmp_map])
        return tmp_map

    def display_map(self):
        """Methode affichant la map"""
        print(self._from_map_to_str(), '\n')

    def _single_move_player(self, cmd):
        """Methode executant un mouvement utilisateur"""
        #on calcul la nouvelle position voir ElementCarte().__add__(...)
        new_position = self._player + moves[cmd]

        for elem_name, elems in self._map_objects.items():
            # On parcours les elements de la map ne correspondant pas
            # a notre personnage
            if elem_name == 'Personnage':
                continue
            for elem in elems:
                # si les position sont egales mais que le player n'est pas
                # superposable avec l'element (= Mur) voir ElementCarte().__add__(...)
                # ou qu'il s'agit de l'arrivée
                if tuple(elem.position) == tuple(new_position) and not elem + self._player:
                    return False
                elif tuple(elem.position) == tuple(new_position) and elem_name == 'Arrivee':
                    self._win = True

        # si on peut déplacer le joueur à la nouvelle position
        self._player.position = new_position
        return True

    def move_player(self, cmd, n_moves=1):
        """Methode permettant de chainer les mouvements."""
        for _ in range(n_moves):
            if not self._single_move_player(cmd):
                return False

            self.display_map()

            if self._win:
                print('Felicitations ! Vous avez gagné !')
                return True
        return False
