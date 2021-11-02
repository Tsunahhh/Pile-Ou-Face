"""
    Auteur: Tsunahhh
    Date: 02/11/21
    Desc: Petit pile ou face de famille made in Tsuna
    Entrée: Choix du joueur
    Sortie: Victoire ou défaite
"""

# J'importe choice du module random
from random import choice
import os
import platform


def clearsystm():
    """
    Fonction qui permet de clear la console au début et à la fin du jeu
    :return: Le clear de la console
    """
    if platform.system() == "Linux":
        os.system("clear")
    elif platform.system() == "Windows":
        os.system("cls")


def affichage(pf):
    """
    Fonction destinée à afficher le résultat de la partie
    :param pf: Décision de l'IA destiné à choisir pile ou face
    :return: affiche un print de la piece
    """
    if pf == "Pile":
        print("""
                xxxxxx
             xxx      xxx
           x              x
           x     Pile     x
           x              x
             xxx      xxx
                xxxxxx
        """)
    else:
        print("""
                xxxxxx
             xxx      xxx
           x              x
           x     Face     x
           x              x
             xxx      xxx
                xxxxxx
        """)


def inselect():
    """
    Fonction destinée à demander à choix au joueur sous le bon format
    :return: Choix du joueur
    """
    result = False
    while result is False:
        s = input("Pile ou Face ?: ")
        if s.isalpha():
            if s in ["Pile", "Face"]:
                result = True
    return s


def piece():
    """
    Fonction destinée à définir quel face de la piece est tirée
    :return: renvoie Pile ou Face
    """
    return choice(["Pile", "Face"])


def main():
    """
    Corps du code, permet de selectionner les étapes du jeu dans l'ordre selon les règles
    :return: Le vainqueur ou le perdant
    """
    choix = inselect()
    ia = piece()
    affichage(ia)
    if choix == ia:
        print('Vous avez Gagné !!')
    else:
        print('Trop nul, perdu !')


clearsystm()
print("Appuyez sur \"Entrer\" pour démarrer le pile ou face")
res = str(input())
while res != "gamme" and res != "stop":
    main()
    print("Appuyez sur \"Entrer\" pour rejouer ou stop pour arrêter")
    res = str(input())
    clearsystm()

# Easter Eggs de Tsuna
if res == "gamme":
    print("""
    x     xxxxxxx
    x     x
    xxxxxxxxxxxxx
          x     x
    xxxxxxx     x
    """)
    input()
clearsystm()