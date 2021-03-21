import pygame
from random import *
from Background.stone import Stone
from Background.wood import Wood
from Terrain.main import Terrain
from Dynamics.var import Var


# On charge l'écran
screen = pygame.display.set_mode((1280, 800))


# class utilisée pour charger les images de décore du fond d'écran
class Background:

    # Differentes images chargées avec pygame pour le background
    blue = pygame.image.load('Assets/Background/Blue.png')
    brown = pygame.image.load('Assets/Background/Brown.png')
    gray = pygame.image.load('Assets/Background/Gray.png')
    green = pygame.image.load('Assets/Background/Green.png')
    pink = pygame.image.load('Assets/Background/Pink.png')
    purple = pygame.image.load('Assets/Background/Purple.png')
    yellow = pygame.image.load('Assets/Background/Yellow.png')

    # Fonction pour charger le fond d'écran aléatoirement
    @staticmethod
    def load_random_background():
        random_list = [
            Background.blue,
            Background.brown,
            Background.gray,
            Background.green,
            Background.pink,
            Background.purple,
            Background.yellow,
        ]
        a = random_list[randint(0, 6)]
        for x in range(0, 1280, 64):
            for y in range(0, 896, 64):
                screen.blit(a, (x, y))

    class Load:
        # Fonction pour charger le fond d'écran aléatoirement
        @staticmethod
        def lvl_1():
            for x in range(0, 1280, 64):
                for y in range(0, 896, 64):
                    screen.blit(Background.yellow, (x, y))
            for i in range(24):
                Var.collision[i] = Terrain.Grass.green(i * 44, 660)

    Stone = Stone()

    Wood = Wood()
