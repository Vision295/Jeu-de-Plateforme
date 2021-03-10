import pygame

# On charge l'écran
screen = pygame.display.set_mode((1280, 800))


# Classe pour les contours en bois
class Wood:

    # dictionnaire avec toutes les positions des images dans Terrain (16*16).png
    positions = {
        'rect': (0, -72),
        'rectR': (-8, -64),
        'small_rect': (-8, -72),
        'small_rectR': (-8, -100),
        'square': (0, -64)
    }

    # dictionnaire avec toutes les tailles des blocs
    taille = {
        'rect': (9, 32),
        'rectR': (32, 9),
        'small_rect': (4, 8),
        'small_rectR': (8, 4),
        'square': (9, 9)
    }

    # fonction pour afficher les long rectangles en bois
    @staticmethod
    def rect(x, y, rotation=False):
        if not rotation:
            surf = pygame.Surface((32, 9))
            surf.blit(pygame.image.load('Assets/Terrain/Terrain (16x16).png'), (-8, -64))
            screen.blit(surf, (x, y))
        else:
            surf = pygame.Surface((9, 32))
            surf.blit(pygame.image.load('Assets/Terrain/Terrain (16x16).png'), (0, -72))
            screen.blit(surf, (x, y))

    # fonction pour afficher le petit rectangle en bois
    @staticmethod
    def small_rect(x, y, rotation=False):
        if not rotation:
            surf = pygame.Surface((8, 4))
            surf.blit(pygame.image.load('Assets/Terrain/Terrain (16x16).png'), (-8, -100))
            screen.blit(surf, (x, y))
        else:
            surf = pygame.Surface((4, 8))
            surf.blit(pygame.image.load('Assets/Terrain/Terrain (16x16).png'), (-8, -72))
            screen.blit(surf, (x, y))

    # foction pour afficher le carré en bois
    @staticmethod
    def square(x, y):
        surf = pygame.Surface((9, 9))
        surf.blit(pygame.image.load('Assets/Terrain/Terrain (16x16).png'), (0, -64))
        screen.blit(surf, (x, y))
