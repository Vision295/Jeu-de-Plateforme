import pygame
from Background.main import Background

screen = pygame.display.set_mode((1056, 792))


class Var:

    # Variables utilisées pour le déplacement du joueur (stockée dans un fichier à part pour pouvoir y
    # accéder facilement depuis un autre fichier)
    step_run = 0
    step_idle = 0

    # Booléens pour connaitre l'etat du joueur
    run = False
    left = False
    jump = False
    fall = False

    # coordonées x et y du joueur
    x = 0
    y = 100

    # hauteur utilisée pour le saut du joueur
    height = 0

    # dico utilisée pour stocker les inputs
    pressed = {}

    # dico utilisé pour stocker toutes les collisions de la map
    collision = {}
