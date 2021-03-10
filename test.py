import pygame as pg
from Background.main import Background as Bg

# INITIALISATION DE PYGAME
pg.init()

# On charge l'écran dans la variable screen
screen = pg.display.set_mode((1280, 800))
Bg.load_random_background()

# INITIALISATION DE TOUTES LES VARIABLES
# Variable utilisée pour faire tuourner le jeu en boucle
running = True

# BOUCLE DE JEU
while running:

    Bg.Outline.stone(100, 100, True)


    pg.display.flip()

    # On utilise les inputs avec pygame
    for event in pg.event.get():

        # Si l'utilisateur ferme la fenêtre
        if event.type == pg.QUIT:
            running = False
            pg.quit()
