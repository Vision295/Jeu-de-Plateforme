import pygame
from game import Game
screen = pygame.display.set_mode((1280, 800))


# pierres en forme de petit carré
class SmallSquare:
    """
        Classe qui permet de créer des blocs du type: SmallSquare. On y trouve une fonction
        qui permet de l'afficher. Il peut être de quatres matériaux différents :
            - roc
            - iron
            - gold
            - bronze
    """

    # positions relatives à l'image Terrain (16*16).png de chaques éléments de pierre rectangulaire
    positions = {
        'roc': (-192, -16),
        'iron': (-192, -80),
        'bronze': (-192, -144),
        'gold': (-272, -144),
    }

    # taille du petit carré
    taille = (16, 16)

    # fonction pour créer un block
    def __init__(self, x, y, materiau='roc'):

        Game.nb_block += 1

        # coordonées du block
        self.x = x
        self.y = y

        # on ajoute le block à l'ensemble des positions relatives
        Game.positions[Game.nb_block] = (self.x, self.y, self.x + SmallSquare.taille[0], self.y + SmallSquare.taille[1])

        # materiau du block
        self.materiau = materiau

        # surface du block
        self.surf = pygame.Surface(SmallSquare.taille)

        # materiaux possibles pour le block
        if self.materiau == 'roc':
            self.position = SmallSquare.positions['roc']
        elif self.materiau == 'iron':
            self.position = SmallSquare.positions['iron']
        elif self.materiau == 'bronze':
            self.position = SmallSquare.positions['bronze']
        elif self.materiau == 'gold':
            self.position = SmallSquare.positions['gold']

        # fonction pour afficher les blocks

    def blit(self):
        self.surf.blit(pygame.image.load('Assets/Terrain/Terrain (16x16).png'), self.position)
        screen.blit(self.surf, (self.x, self.y))
