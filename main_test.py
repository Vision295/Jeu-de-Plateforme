import pygame as pg
from Background.main import Background as Bg
from Dynamics.var import Var
from Dynamics.main import Dynamics
# INITIALISATION DE PYGAME
pg.init()

# On charge l'écran dans la variable screen
screen = pg.display.set_mode((1056, 704))
# 792 = 3 * 3 * 2 * 2 * 2 * 11
# 792 = 44 * 18
# 1056 = 3 * 2 * 2 * 2 * 2 * 2 * 11
# 1056 = 11 * 96 et 768 = 64 * 16.5
Bg.load_random_background()

# INITIALISATION DE TOUTES LES VARIABLES
# Variable utilisée pour faire tuourner le jeu en boucle
running = True

"""
rotation = True ==> |
rotation = False ==> ---

ARBORESCENCE DES CLASSES :
Général, Utilité > Matériau > (forme / Forme) > (couleur)

Ex:
Background > Wood > square
Terrain > Stone > Rect/Platform > gold
"""
# BOUCLE DE JEU
while running:

    # On utilise les inputs avec pygame
    for event in pg.event.get():

        # Si l'utilisateur ferme la fenêtre
        if event.type == pg.QUIT:
            running = False
            runningGeneral = False
            pg.quit()
