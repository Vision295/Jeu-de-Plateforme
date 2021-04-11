import pygame
from game import Game

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

    # fonction pour créer un block
    def __init__(self, x, y, materiau='roc'):

        Game.nb_block += 1

        # coordonées du block
        self.x = x
        self.y = y

        # on ajoute le block à l'ensemble des positions relatives
        Game.positions[Game.nb_block] = (self.x, self.y, self.x + 32, self.y + 32)

        # materiau du block
        self.materiau = materiau

        # surface du block
        self.surf = pygame.Surface((32, 32))

        # materiaux possibles pour le block
        if self.materiau == 'roc':
            self.position = (-208, -16)
        elif self.materiau == 'iron':
            self.position = (-208, -80)
        elif self.materiau == 'bronze':
            self.position = (-208, -144)
        elif self.materiau == 'gold':
            self.position = (-288, -144)

        # fonction pour afficher les blocks

    def blit(self):
        self.surf.blit(pygame.image.load('Assets/Terrain/Terrain (16x16).png'), self.position)
        screen.blit(self.surf, (self.x, self.y))

