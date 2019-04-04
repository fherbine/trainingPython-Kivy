# -*-coding:Utf-8 -*

"""Ce fichier contient le code principal du jeu.

Exécutez-le avec Python pour lancer le jeu.

"""

import os

from carte import Carte
from labyrinthe import Labyrinthe

# On charge les cartes existantes
cartes = []
for nom_fichier in os.listdir("cartes"):
    if nom_fichier.endswith(".txt"):
        chemin = os.path.join("cartes", nom_fichier)
        nom_carte = nom_fichier[:-3].lower()
        with open(chemin, "r") as fichier:
            contenu = fichier.read()
            cartes.append(Carte(nom_fichier, contenu))

# On affiche les cartes existantes
print("Labyrinthes existants :")
for i, carte in enumerate(cartes):
    print("\t{} - {}.".format(i + 1, carte.nom))

# Si il y a une partie sauvegardée, on l'affiche, à compléter

global_commands = 'QNESO'

# affiche le prompt, attend une commande et retourne la commande + arguments
def prompt(cmds=global_commands):
    args = input('> ')
    if args[0].upper() not in cmds:
        print ('Argument \'{}\' not in commands {}'.format(args[0], cmds))
        return prompt(cmds)
    else:
        try:
            argint = 1
            if len(args) > 1:
                argint = int(args[1:])
            return args[0].upper(), argint
        except:
            prompt(cmds)

# on verifie le numéro du labyrinthe entrer
try:
    selected_map = cartes[int(input(
        'Entrez le numero du labyrinthe pour commencer à jouer : '
    )) - 1]
except:
    raise Exception('invalid map or typing, exiting...')

labyrinthe = Labyrinthe(selected_map)
labyrinthe.display_map()

win = False

while not win:
    cmd, argint = prompt()
    win = labyrinthe.move_player(cmd, argint)
