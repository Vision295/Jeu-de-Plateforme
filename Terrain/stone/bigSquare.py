import pygame

screen = pygame.display.set_mode((1280, 800))


# pierres en formes de grands carrés
class BigSquare:

    # positions relatives à l'image Terrain (16*16).png de chaques éléments de pierre rectangulaire
    positions = {
        'roc': (-208, -16),
        'iron': (-208, -80),
        'bronze': (-208, -144),
        'gold': (-288, -144),
    }

    # taille du grand carré
    taille = (32, 32)

    # affiche sur l'écran un grand bloc de pierre en pierre aux coordonnées (x, y)
    @staticmethod
    def roc(x, y):
        surf = pygame.Surface((32, 32))
        surf.blit(pygame.image.load('Assets/Terrain/Terrain (16x16).png'), (-208, -16))
        screen.blit(surf, (x, y))
        return x, x + 32, y, y + 32

    # affiche sur l'écran un grand bloc de pierre en fer aux coordonnées (x, y)
    @staticmethod
    def iron(x, y):
        surf = pygame.Surface((32, 32))
        surf.blit(pygame.image.load('Assets/Terrain/Terrain (16x16).png'), (-208, -80))
        screen.blit(surf, (x, y))
        return x, x + 32, y, y + 32

    # affiche sur l'écran un grand bloc de pierre en bronze aux coordonnées (x, y)
    @staticmethod
    def bronze(x, y):
        surf = pygame.Surface((32, 32))
        surf.blit(pygame.image.load('Assets/Terrain/Terrain (16x16).png'), (-208, -144))
        screen.blit(surf, (x, y))
        return x, x + 32, y, y + 32

    # affiche sur l'écran un grand bloc de pierre en or aux coordonnées (x, y)
    @staticmethod
    def gold(x, y):
        surf = pygame.Surface((32, 32))
        surf.blit(pygame.image.load('Assets/Terrain/Terrain (16x16).png'), (-288, -144))
        screen.blit(surf, (x, y))
        return x, x + 32, y, y + 32
