import pygame

screen = pygame.display.set_mode((1280, 800))


# pierres en forme de rectangle
class Rect:
    # positions relatives à l'image Terrain (16*16).png de chaques éléments de pierre rectangulaire
    positions = {
        'roc': (-192, 0),
        'rocR': (-240, 0),
        'iron': (-192, -64),
        'ironR': (-240, -64),
        'bronze': (-192, -128),
        'bronzeR': (-240, -128),
        'gold': (-320, -128),
        'goldR': (-272, -128)
    }

    # taille des rectanges
    taille = {
        'rotation': (16, 48),
        'none': (48, 16)
    }

    # affiche sur l'écran un bloc de pierre en pierre aux coordonnées (x, y)
    # qui peut tourner de 90° (rotate = True)
    @staticmethod
    def roc(x, y, rotation=False):
        if rotation:
            surf = pygame.Surface((16, 48))
            surf.blit(pygame.image.load('Assets/Terrain/Terrain (16x16).png'), (-240, 0))
            screen.blit(surf, (x, y))
            return x, x + 16, y, y + 48
        else:
            surf = pygame.Surface((48, 16))
            surf.blit(pygame.image.load('Assets/Terrain/Terrain (16x16).png'), (-192, 0))
            screen.blit(surf, (x, y))
            return x, x + 48, y, y + 48

    # affiche sur l'écran un bloc de pierre en fer aux coordonnées (x, y)
    # qui peut tourner de 90° (rotate = True)
    @staticmethod
    def iron(x, y, rotation=False):
        if rotation:
            surf = pygame.Surface((16, 48))
            surf.blit(pygame.image.load('Assets/Terrain/Terrain (16x16).png'), (-240, -64))
            screen.blit(surf, (x, y))
            return x, x + 16, y, y + 48
        else:
            surf = pygame.Surface((48, 16))
            surf.blit(pygame.image.load('Assets/Terrain/Terrain (16x16).png'), (-192, -64))
            screen.blit(surf, (x, y))
            return x, x + 48, y, y + 48

    # affiche sur l'écran un bloc de pierre en bronze aux coordonnées (x, y)
    # qui peut tourner de 90° (rotate = True)
    @staticmethod
    def bronze(x, y, rotation=False):
        if rotation:
            surf = pygame.Surface((16, 48))
            surf.blit(pygame.image.load('Assets/Terrain/Terrain (16x16).png'), (-240, -128))
            screen.blit(surf, (x, y))
            return x, x + 16, y, y + 48
        else:
            surf = pygame.Surface((48, 16))
            surf.blit(pygame.image.load('Assets/Terrain/Terrain (16x16).png'), (-192, -128))
            screen.blit(surf, (x, y))
            return x, x + 48, y, y + 16

    # affiche sur l'écran un bloc de pierre en or aux coordonnées (x, y)
    # qui peut tourner de 90° (rotate = True)
    @staticmethod
    def gold(x, y, rotation=False):
        if rotation:
            surf = pygame.Surface((16, 48))
            surf.blit(pygame.image.load('Assets/Terrain/Terrain (16x16).png'), (-320, -128))
            screen.blit(surf, (x, y))
            return x, x + 16, y, y + 48
        else:
            surf = pygame.Surface((48, 16))
            surf.blit(pygame.image.load('Assets/Terrain/Terrain (16x16).png'), (-272, -128))
            screen.blit(surf, (x, y))
            return x, x + 48, y, y + 16
