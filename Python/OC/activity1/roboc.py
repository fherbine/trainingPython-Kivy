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

unsaved_maps = [carte for carte in cartes if 'save' not in carte.nom]
saved_maps = [carte for carte in cartes if 'save' in carte.nom]

for i, carte in enumerate(unsaved_maps):
    print("\t{} - {}.".format(i + 1, carte.nom))

# Si il y a une partie sauvegardée, on l'affiche, à compléter

global_commands = 'QNESO'

def get_previous_saved_game(selected_map):
    """Recupere la derniere sauvegarde."""
    ans = ''
    for saved_map in saved_maps:
        if selected_map.nom in saved_map.nom:
            ans = input('Une sauvegarde existe pour cette carte, voulez vous reprendre la partie (o/N): ')
            print('Oui' if ans.upper() == 'O' else 'Non')
            print('\n')
            break

    # onconsidere que toute reponses differente de (o/O) est equivalente
    # a la reponse par defaut, Non (n/N)
    return selected_map if ans.upper() != 'O' else saved_map

# affiche le prompt, attend une commande et retourne la commande + arguments
def prompt(cmds=global_commands):
    """Affiche le prompt"""
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
            return prompt(cmds)

print('\n')

# on verifie le numéro du labyrinthe entrer
try:
    selected_map = unsaved_maps[int(input(
        'Entrez le numero du labyrinthe pour commencer à jouer : '
    )) - 1]
except:
    raise Exception('invalid map or typing, exiting...')

print('\n')

selected_map = get_previous_saved_game(selected_map)
labyrinthe = Labyrinthe(selected_map)
labyrinthe.display_map()

win = False

def quit_game():
    print('Bye bye ... :)')
    labyrinthe.save()

while not win:
    cmd, argint = prompt()

    if cmd == 'Q':
        quit_game()
        break
    else:
        win = labyrinthe.move_player(cmd, argint)
