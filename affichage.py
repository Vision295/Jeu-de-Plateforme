import pygame as pg
from Background.main import Background as Bg
from main import Terrain
from Spike.spike import Spike

# INITIALISATION DE PYGAME
pg.init()

# On charge l'écran dans la variable screen
screen = pg.display.set_mode((900, 600))
Bg.load_random_background()

# INITIALISATION DE TOUTES LES VARIABLES
# Variable utilisée pour faire tuourner le jeu en boucle
running = True

# BOUCLE DE JEU
while running:

    # LES PICS
    Spike.spike(100, 50)

    # LES OUTLINES DU BACKGROUND
    # Le bois
    Bg.Wood.rect(100, 100, True)
    Bg.Wood.rect(100, 150)
    Bg.Wood.small_rect(100, 200, True)
    Bg.Wood.small_rect(100, 250)
    Bg.Wood.square(100, 300)

    # la pierre
    Bg.Stone.rect(100, 350, True)
    Bg.Stone.rect(100, 400)
    Bg.Stone.square(100, 450)
    Bg.Stone.small_square(100, 500)

    # BLOC DE TERRAIN
    # Les blocs de pierres
    # Les blocs de pierres rectangulaires
    Terrain.Stone.Rect.roc(200, 50, True)
    Terrain.Stone.Rect.roc(200, 100)
    Terrain.Stone.Rect.iron(200, 150, True)
    Terrain.Stone.Rect.iron(200, 200)
    Terrain.Stone.Rect.bronze(200, 250, True)
    Terrain.Stone.Rect.bronze(200, 300)
    Terrain.Stone.Rect.gold(200, 350, True)
    Terrain.Stone.Rect.gold(200, 400)

    # Les blocs de pierres en grand carré
    Terrain.Stone.BigSquare.roc(300, 50)
    Terrain.Stone.BigSquare.iron(300, 100)
    Terrain.Stone.BigSquare.bronze(300, 150)
    Terrain.Stone.BigSquare.gold(300, 200)

    # Les blocs de pierres en petit carré
    Terrain.Stone.SmallSquare.roc(400, 50)
    Terrain.Stone.SmallSquare.iron(400, 100)
    Terrain.Stone.SmallSquare.bronze(400, 150)
    Terrain.Stone.SmallSquare.gold(400, 200)

    # Les blocs de pierres en plateforme
    Terrain.Stone.Platform.roc(500, 50)
    Terrain.Stone.Platform.iron(500, 100)
    Terrain.Stone.Platform.gold(500, 150)

    # Les blocs de terre
    Terrain.Dirt.green(600, 50)
    Terrain.Dirt.pink(600, 100)
    Terrain.Dirt.orange(600, 150)

    # Les blocs d'herbe
    Terrain.Grass.green(700, 50)
    Terrain.Grass.pink(700, 100)
    Terrain.Grass.orange(700, 150)

    pg.display.flip()

    # On utilise les inputs avec pygame
    for event in pg.event.get():

        # Si l'utilisateur ferme la fenêtre
        if event.type == pg.QUIT:
            running = False
            runningGeneral = False
            pg.quit()
