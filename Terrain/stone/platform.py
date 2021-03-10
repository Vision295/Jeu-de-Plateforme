import pygame

screen = pygame.display.set_mode((1280, 800))


# classe avec toutes les plateformes
class Platform:

    # dictionnaire avec les positions des différentes images sur Terrain (16*16).png
    positions = {
        'roc': (-272, -16),
        'gold': (-272, 0),
        'iron': (-272, -32)
    }

    # taille des plateformes
    taille = (48, 4)

    # affiche sur l'écran une plateforme en pierre aux coordonnées (x, y)
    @staticmethod
    def roc(x, y):
        surf = pygame.Surface((48, 5))
        surf.blit(pygame.image.load('Assets/Terrain/Terrain (16x16).png'), (-272, -16))
        screen.blit(surf, (x, y))
        return x, x + 48, y, y + 5

    # affiche sur l'écran une plateforme en or aux coordonnées (x, y)
    @staticmethod
    def gold(x, y):
        surf = pygame.Surface((48, 5))
        surf.blit(pygame.image.load('Assets/Terrain/Terrain (16x16).png'), (-272, 0))
        screen.blit(surf, (x, y))
        return x, x + 48, y, y + 5

    # affiche sur l'écran une plateforme en pierre aux coordonnées (x, y)
    @staticmethod
    def iron(x, y):
        surf = pygame.Surface((48, 5))
        surf.blit(pygame.image.load('Assets/Terrain/Terrain (16x16).png'), (-272, -32))
        screen.blit(surf, (x, y))
        return x, x + 48, y, y + 5
