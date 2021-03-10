import pygame
from Terrain.stone.smallSquare import SmallSquare
from Terrain.stone.rect import Rect
from Terrain.stone.bigSquare import BigSquare
from Terrain.stone.platform import Platform

screen = pygame.display.set_mode((1280, 800))


# BLOC DE PIERRE
class Stone:

    # On importe les classes correspondantes dans cette classe Stone
    Rect = Rect()

    SmallSquare = SmallSquare()

    BigSquare = BigSquare()

    Platform = Platform()
