import pygame as pg
from Background.main import Background as Bg
from Terrain.main import Terrain
from Main_Character.idle import Idle

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

    #Idle.ninja_frog(100, 100, 1)
    Idle.ninja_frog(100, 100, 2)
    #Idle.ninja_frog(100, 100, 3)
    #Idle.ninja_frog(100, 100, 4)
    #Idle.ninja_frog(100, 100, 5)
    #Idle.ninja_frog(100, 100, 6)
    #Idle.ninja_frog(100, 100, 7)
    #Idle.ninja_frog(100, 100, 8)
    #Idle.ninja_frog(100, 100, 9)
    #Idle.ninja_frog(100, 100, 10)
    #Idle.ninja_frog(100, 100, 11)
    pg.display.flip()

    # On utilise les inputs avec pygame
    for event in pg.event.get():

        # Si l'utilisateur ferme la fenêtre
        if event.type == pg.QUIT:
            running = False
            pg.quit()
