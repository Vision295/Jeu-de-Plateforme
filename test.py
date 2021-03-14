import pygame as pg
from Background.main import Background as Bg
from Terrain.main import Terrain
from Main_Character.main import NinjaFrog

# INITIALISATION DE PYGAME
pg.init()

# On charge l'écran dans la variable screen
screen = pg.display.set_mode((1056, 704))
Bg.load_random_background()

# INITIALISATION DE TOUTES LES VARIABLES
# Variable utilisée pour faire tuourner le jeu en boucle
running = True

# BOUCLE DE JEU
while running:

    for i in range(12, 24):
        Terrain.Grass.green(i * 44, 748)

    for y in range(1000):
        NinjaFrog.Idle.loop_idle(1)
        pg.display.flip()

    # On utilise les inputs avec pygame
    for event in pg.event.get():

        # Si l'utilisateur ferme la fenêtre
        if event.type == pg.QUIT:
            running = False
            pg.quit()
