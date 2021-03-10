import pygame as pg
from Background.main import Background as Bg

# INITIALISATION DE PYGAME
pg.init()

# On charge l'écran dans la variable screen
screen = pg.display.set_mode((768, 576))
# 576 = 3 * 3 * 2 * 2 * 2 * 2
# 576 = 48 * 12 et 576 = 64 * 9
# 768 = 3 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2
# 768 = 48 * 16 et 768 = 64 * 12
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

print('je test GitHub')

# BOUCLE DE JEU
while running:

    pg.display.flip()

    # On utilise les inputs avec pygame
    for event in pg.event.get():

        # Si l'utilisateur ferme la fenêtre
        if event.type == pg.QUIT:
            running = False
            runningGeneral = False
            pg.quit()
