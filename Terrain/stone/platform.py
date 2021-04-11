import pygame
from game import Game

screen = pygame.display.set_mode((1280, 800))


# classe avec toutes les plateformes
class Platform:

    """
        Classe qui permet de créer des blocs du type: Platform. On y trouve une fonction
        qui permet de l'afficher. Il peut être de quatres matériaux différents :
            - roc
            - gold
            - bronze
    """

    # dictionnaire avec les positions des différentes images sur Terrain (16*16).png
    positions = {
        'roc': (-272, -16),
        'gold': (-272, 0),
        'iron': (-272, -32)
    }

    # taille des plateformes
    taille = (48, 4)

    # fonction pour créer un block
    def __init__(self, x, y, materiau='roc'):

        Game.nb_block += 1

        # coordonées du block
        self.x = x
        self.y = y

        # on ajoute le block à l'ensemble des positions relatives
        Game.positions[Game.nb_block] = (self.x, self.y, self.x + Platform.taille[0], self.y + Platform.taille[1])

        # materiau du block
        self.materiau = materiau

        # surface du block
        self.surf = pygame.Surface(Platform.taille)

        # materiaux possibles pour le block
        if self.materiau == 'roc':
            self.position = Platform.positions['roc']
        elif self.materiau == 'iron':
            self.position = Platform.positions['iron']
        elif self.materiau == 'gold':
            self.position = Platform.positions['gold']

    # fonction pour afficher les blocks
    def blit(self):
        self.surf.blit(pygame.image.load('Assets/Terrain/Terrain (16x16).png'), self.position)
        screen.blit(self.surf, (self.x, self.y))
