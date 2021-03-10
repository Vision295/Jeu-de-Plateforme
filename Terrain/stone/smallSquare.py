import pygame
screen = pygame.display.set_mode((1280, 800))


# pierres en forme de petit carré
class SmallSquare:

    # positions relatives à l'image Terrain (16*16).png de chaques éléments de pierre rectangulaire
    positions = {
        'roc': (-192, -16),
        'iron': (-192, -80),
        'bronze': (-192, -144),
        'gold': (-272, -144),
    }

    # taille du petit carré
    taille = (16, 16)

    # affiche sur l'écran un petit bloc de pierre en pierre aux coordonnées (x, y)
    @staticmethod
    def roc(x, y):
        surf = pygame.Surface((16, 16))
        surf.blit(pygame.image.load('Assets/Terrain/Terrain (16x16).png'), (-192, -16))
        screen.blit(surf, (x, y))
        return x, x + 16, y, y + 16

    # affiche sur l'écran un petit bloc de pierre en fer aux coordonnées (x, y)
    @staticmethod
    def iron(x, y):
        surf = pygame.Surface((16, 16))
        surf.blit(pygame.image.load('Assets/Terrain/Terrain (16x16).png'), (-192, -80))
        screen.blit(surf, (x, y))
        return x, x + 16, y, y + 16

    # affiche sur l'écran un petit bloc de pierre en broner aux coordonnées (x, y)
    @staticmethod
    def bronze(x, y):
        surf = pygame.Surface((16, 16))
        surf.blit(pygame.image.load('Assets/Terrain/Terrain (16x16).png'), (-192, -144))
        screen.blit(surf, (x, y))
        return x, x + 16, y, y + 16

    # affiche sur l'écran un petit bloc de pierre en or aux coordonnées (x, y)
    @staticmethod
    def gold(x, y):
        surf = pygame.Surface((16, 16))
        surf.blit(pygame.image.load('Assets/Terrain/Terrain (16x16).png'), (-272, -144))
        screen.blit(surf, (x, y))
        return x, x + 16, y, y + 16
