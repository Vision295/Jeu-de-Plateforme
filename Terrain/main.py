import pygame
from Terrain.dirt import Dirt
from Terrain.grass import Grass
from Terrain.stone.main import Stone
from Terrain.brick import Brick

# On charge l'écran dans la variable screen
screen = pygame.display.set_mode((1280, 800))


# class utilisée pour charger les images de terrains
class Terrain:

    # On importe les classes correspondantes aux classes allant dans la classe Terrain
    Dirt = Dirt()

    Grass = Grass()

    Stone = Stone()

    Brick = Brick()
