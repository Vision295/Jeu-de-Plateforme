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
# Variable utilisée pour faire tourner le jeu en boucle
running = True

# BOUCLE DE JEU
while running:

    for i in range(12, 24):
        Terrain.Grass.green(i * 44, 748)

    NinjaFrog.Run.loop_run(100, 100)
    NinjaFrog.Jump.loop_jump(100, 100)
    NinjaFrog.Fall.loop_fall(100, 100)
    NinjaFrog.Idle.loop_idle(100, 100)

    # On utilise les inputs avec pygame
    for event in pg.event.get():

        # Si l'utilisateur ferme la fenêtre
        if event.type == pg.QUIT:
            running = False
            pg.quit()
