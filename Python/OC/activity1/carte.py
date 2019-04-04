# -*-coding:Utf-8 -*

"""Ce module contient la classe Carte, ainsi que la fonction
creer_labyrinthe_depuis_chaine(chaine) permettant de parser le fichier reçu"""


from element_carte import (
    Arrivee,
    Mur,
    Personnage,
    Porte,
)

element = {'O': Mur, 'X': Personnage, '.': Porte, 'U': Arrivee, ' ': None}

def creer_labyrinthe_depuis_chaine(chaine):
    """Cette fonction permet de transformer la chaine de caractère lue du
    fichier, en dict():
    de la façon suivante:
        {'Personnage': obj, 'Mur': [...], 'Porte': [...], 'arrivee': obj}
    """

    lines = chaine.split('\n')
    labyrinthe = dict()

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char in element and callable(element[char]):
                new_elem = element[char]((x, y))
                class_name = new_elem.__class__.__name__

                if labyrinthe.get(class_name, False):
                    if type(labyrinthe[class_name]) != list:
                        labyrinthe[class_name] = [labyrinthe[class_name]]
                    labyrinthe[class_name].append(new_elem)
                else:
                    labyrinthe[class_name] = new_elem

    return labyrinthe

class Carte:

    """Objet de transition entre un fichier et un labyrinthe."""

    def __init__(self, nom, chaine):
        """Constructeur d'une carte prend en compte, le nom de la carte, ainsi
        que son contenu (chaine)."""

        self.nom = nom.split('.')[0]
        self.labyrinthe = creer_labyrinthe_depuis_chaine(chaine)

    def __repr__(self):
        return "<Carte {}>".format(self.nom)
