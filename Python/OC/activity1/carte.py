# -*-coding:Utf-8 -*

"""Ce module contient la classe Carte, ainsi que la fonction
creer_labyrinthe_depuis_chaine(chaine) permettant de parser le fichier reçu"""


def creer_labyrinthe_depuis_chaine(chaine):
    pass

class Carte:

    """Objet de transition entre un fichier et un labyrinthe."""

    def __init__(self, nom, chaine):
        """Constructeur d'une carte prend en compte, le nom de la carte, ainsi
        que son contenu (chaine)."""

        self.nom = nom.split('.')[0]
        self.labyrinthe = creer_labyrinthe_depuis_chaine(chaine)

    def __repr__(self):
        return "<Carte {}>".format(self.nom)
