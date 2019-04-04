# -*-coding:Utf-8 -*

"""Ce module contient la classe Labyrinthe."""

import os

# dict() faisant correspondre les direction a des mouvement en tuples
# de coordonnees cartesiennes & dict() faisant correspondres des noms de classes
# (element_carte.py) a des caracteres ASCII

moves = {'N': (0, -1), 'E': (1, 0), 'S': (0, 1), 'O': (-1, 0)}
static_elems = {'Porte': '.', 'Mur': 'O', 'Arrivee': 'U'}

class Labyrinthe:

    """Classe représentant un labyrinthe."""

    def __init__(self, map_elem):
        """Constructeur de la classe Labyrinthe en prends en compte:
            - map_objects, labyrinthe de l' objet Carte (map_elem)
            - map_name, le nom de la carte
            - les dimensions de la map extraite de map_elem.labyrinthe
            - player pointe vers l'objet Personnage de map_objects
            - win, un attribut permettant de connaitre le moment où l'on gagne
        """
        if 'Arrivee' not in map_elem.labyrinthe or 'Personnage' not in map_elem.labyrinthe:
            raise Exception('Pas de personnage ou d\'arrivée dans le labyrinthe\
             séléctionné :(')
        self._map_dimensions = map_elem.labyrinthe['dimensions']
        del map_elem.labyrinthe['dimensions']
        self._map_objects = map_elem.labyrinthe
        self._player = self._map_objects['Personnage'][0]
        self._win = False
        self._map_name = map_elem.nom

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
        """Methode permettant de chainer les mouvements.
        Peut importe l'issue du déplacement on sauvegarde la partie"""
        for _ in range(n_moves):
            if not self._single_move_player(cmd):
                self.save()
                return False

            self.display_map()

            if self._win:
                print('Felicitations ! Vous avez gagné !')
                self.destroy_saved_game()
                return True
        self.save()
        return False

    def destroy_saved_game(self):
        """On detruit la sauvegarde si le joueur gagne."""

        if 'save' in self._map_name:
            filename = '{}.txt'.format(self._map_name)
        else:
            filename = 'save-{}.txt'.format(self._map_name)
        path = os.path.join('cartes', filename)

        os.remove(path)

    def save(self):
        """Cette methode nous permet d'effectuer une sauvegarde."""
        if 'save' in self._map_name:
            filename = '{}.txt'.format(self._map_name)
        else:
            filename = 'save-{}.txt'.format(self._map_name)
        path = os.path.join('cartes', filename)

        # on ecrase la sauvegarde si une meme sauvegarde (meme partie) existe

        with open(path, 'w+') as save_file:
            save_file.write(self._from_map_to_str())
