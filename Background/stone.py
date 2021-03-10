import pygame

# On charge l'écran
screen = pygame.display.set_mode((1280, 800))


# Classe pour les contours en pierre grise
class Stone:

    # dictionnaire avec toutes les positions des images dans Terrain (16*16).png
    positions = {
        'rect': (0, 0),
        'rectR': (0, -16),
        'square': (0, -8),
        'small_square':  (-8, -33)
    }

    # dictionnaire avec toutes les tailles des blocs
    taille = {
        'rect': (16, 8),
        'rectR': (8, 16),
        'square': (8, 8),
        'small_square': (6, 6)
    }

    # fonction pour afficher les rectangles en pierre grise
    @staticmethod
    def rect(x, y, rotation=False):
        if rotation:
            surf = pygame.Surface((9, 17))
            surf.blit(pygame.image.load('Assets/Terrain/Terrain (16x16).png'), (0, -16))
            screen.blit(surf, (x, y))
        else:
            surf = pygame.Surface((17, 9))
            surf.blit(pygame.image.load('Assets/Terrain/Terrain (16x16).png'), (0, 0))
            screen.blit(surf, (x, y))
        return 0

    # fonction pour afficher les grands carrés en pierre grise
    @staticmethod
    def square(x, y):
        surf = pygame.Surface((9, 9))
        surf.blit(pygame.image.load('Assets/Terrain/Terrain (16x16).png'), (0, -8))
        screen.blit(surf, (x, y))
        return 0

    # fonction pour afficher les petits carrés en pierre grise
    @staticmethod
    def small_square(x, y):
        surf = pygame.Surface((7, 7))
        surf.blit(pygame.image.load('Assets/Terrain/Terrain (16x16).png'), (-8, -33))
        screen.blit(surf, (x, y))
        return 0
