import pygame
screen = pygame.display.set_mode((1280, 800))


# BLOC DE BRIQUE
class Brick:
    # positions relatives à l'image Terrain (16*16).png de chaques éléments de pierre rectangulaire
    positions = {
        'big_brick': (-272, -64),
        'small_brick': (-319, -64),
    }

    # dictionnaire pour connaitre la taille des différents blocs
    taille = {
        'big_brick': (48, 48),
        'small_brick': (32, 32)
    }

    # affiche à l'écran un gros bloc de brique aux coordonnées (x, y)
    @staticmethod
    def big(x, y):
        surf = pygame.Surface((48, 48))
        surf.blit(pygame.image.load('Assets/Terrain/Terrain (16x16).png'), (-272, -64))
        screen.blit(surf, (x, y))
        return x, x + 48, y, y + 48

    # affiche à l'écran un petit bloc de brique aux coordonnées (x, y)
    @staticmethod
    def small(x, y):
        surf = pygame.Surface((34, 33))
        surf.blit(pygame.image.load('Assets/Terrain/Terrain (16x16).png'), (-319, -64))
        screen.blit(surf, (x, y))
        return x, x + 32, y, y + 32
