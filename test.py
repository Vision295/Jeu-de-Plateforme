import pygame as pg
from Background.main import Background as Bg
from Terrain.main import Terrain
from Dynamics.var import var
from Dynamics.main import Dynamics

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

    Bg.Load.lvl_1()
    Dynamics.jump()
    Dynamics.run()
    Dynamics.fall()
    Dynamics.idle()
    var.step_run += 1
    var.step_idle += 1

    for i in range(12, 24):
        Terrain.Grass.green(i * 44, 748)

    pg.display.flip()

    # On utilise les inputs avec pygame
    for event in pg.event.get():

        # Si l'utilisateur ferme la fenêtre
        if event.type == pg.QUIT:
            running = False
            pg.quit()

        # Si l'utilisateur maintiens une touche appuyée
        elif event.type == pg.KEYDOWN:
            # On met la valeur de clé correspondante à l'input entré à True
            var.pressed[event.key] = True

        # Si l'utilisateur lève une touche
        elif event.type == pg.KEYUP:
            # On met la valeur de clé correspondante à l'input entré à False
            var.pressed[event.key] = False
