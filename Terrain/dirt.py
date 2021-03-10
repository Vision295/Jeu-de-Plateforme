import pygame
screen = pygame.display.set_mode((1280, 800))


class Dirt:

    # dictionnaire pour connaitre la taille des différents blocs
    taille = (48, 32)

    # positions relatives à l'image Terrain (16*16).png de chaques éléments de terre
    positions = {
        'green': (-96, -15),
        'orange': (-96, -79),
        'pink': (-96, -143)
    }

    # BLOC DE TERRE
    # affiche sur l'écran un bloc de terre verte aux coordonnées (x, y)
    @staticmethod
    def green(x, y):
        surf = pygame.Surface((48, 33))
        surf.blit(pygame.image.load('Assets/Terrain/Terrain (16x16).png'), (-96, -15))
        screen.blit(surf, (x, y))
        return x, x + 48, y, y + 32

    # affiche sur l'écran un bloc de terre orange aux coordonnées (x, y)
    @staticmethod
    def orange(x, y):
        surf = pygame.Surface((48, 33))
        surf.blit(pygame.image.load('Assets/Terrain/Terrain (16x16).png'), (-96, -79))
        screen.blit(surf, (x, y))
        return x, x + 48, y, y + 32

    # affiche sur l'écran un bloc de terre rose aux coordonnées (x, y)
    @staticmethod
    def pink(x, y):
        surf = pygame.Surface((48, 33))
        surf.blit(pygame.image.load('Assets/Terrain/Terrain (16x16).png'), (-96, -143))
        screen.blit(surf, (x, y))
        return x, x + 48, y, y + 32
