import pygame
screen = pygame.display.set_mode((1280, 800))


class Grass:

    # dictionnaire pour connaitre la taille des différents blocs
    taille = (48, 48)

    # positions relatives à l'image Terrain (16*16).png de chaques éléments de terre
    positions = {
        'green': (-96, 0),
        'orange': (-96, -64),
        'pink': (-96, -128),
    }

    # BLOC D'HERBE
    # affiche sur l'écran un bloc d'herbe verte aux coordonnées (x, y)
    @staticmethod
    def green(x, y):
        surf = pygame.Surface((48, 48))
        surf.blit(pygame.image.load('Assets/Terrain/Terrain (16x16).png'), (-96, 0))
        screen.blit(surf, (x, y))
        return x, x + 48, y, y + 48

    # affiche sur l'écran un bloc d'herbe orange aux coordonnées (x, y)
    @staticmethod
    def orange(x, y):
        surf = pygame.Surface((48, 48))
        surf.blit(pygame.image.load('Assets/Terrain/Terrain (16x16).png'), (-96, -64))
        screen.blit(surf, (x, y))
        return x, x + 48, y, y + 48

    # affiche sur l'écran un bloc d'herbe rose aux coordonnées (x, y)
    @staticmethod
    def pink(x, y):
        surf = pygame.Surface((48, 48))
        surf.blit(pygame.image.load('Assets/Terrain/Terrain (16x16).png'), (-96, -128))
        screen.blit(surf, (x, y))
        return x, x + 48, y, y + 48
