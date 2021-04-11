import pygame
from game import Game

screen = pygame.display.set_mode((1280, 800))


# pierres en forme de rectangle
class Rect:

    """
        Classe qui permet de créer des blocs du type: Rect. On y trouve une fonction
        qui permet de l'afficher. Il peut être de quatres matériaux différents en
        fonction d'une rotation de 90° ou pas:
            - roc
            - iron
            - gold
            - bronze
    """

    # positions relatives à l'image Terrain (16*16).png de chaques éléments de pierre rectangulaire
    positions = {
        'rotation': {'roc': (-240, 0), 'iron': (-240, -64), 'bronze': (-240, -128), 'gold': (-272, -128)},
        'normal': {'roc': (-192, 0), 'iron': (-192, -64), 'bronze': (-192, -128), 'gold': (-320, -128)}
    }

    # taille des rectanges
    taille = {
        'rotation': (16, 48),
        'normal': (48, 16)
    }

    # fonction pour créer un block
    def __init__(self, x, y, rotation, materiau='roc'):

        Game.nb_block += 1

        # coordonées du block
        self.x = x
        self.y = y

        # variable pour savoir s'il faut tourner le rectangle de 90°
        self.rotation = rotation

        # materiau du block
        self.materiau = materiau

        # Si l'utilisateur souhaite faire tourner le rectangle de 90°
        if self.rotation:

            # surface du block
            self.surf = pygame.Surface(Rect.taille['rotation'])

            # on ajoute le block à l'ensemble des positions relatives
            Game.positions[Game.nb_block] = (self.x, self.y, self.x + Rect.taille['rotation'][0], self.y + Rect.taille['rotation'][1])

            # materiaux possibles pour le block
            if self.materiau == 'roc':
                self.position = Rect.positions['rotation']['roc']
            elif self.materiau == 'iron':
                self.position = Rect.positions['rotation']['iron']
            elif self.materiau == 'bronze':
                self.position = Rect.positions['rotation']['bronze']
            elif self.materiau == 'gold':
                self.position = Rect.positions['rotation']['gold']

        # Si l'utilisateur souhaite faire tourner le rectangle de 90°
        elif not self.rotation:

            # surface du block
            self.surf = pygame.Surface(Rect.taille['normal'])

            # on ajoute le block à l'ensemble des positions relatives
            Game.positions[Game.nb_block] = (self.x, self.y, self.x + Rect.taille['normal'][0], self.y + Rect.taille['rotation'][1])

            # materiaux possibles pour le block
            if self.materiau == 'roc':
                self.position = Rect.positions['normal']['roc']
            elif self.materiau == 'iron':
                self.position = Rect.positions['normal']['iron']
            elif self.materiau == 'bronze':
                self.position = Rect.positions['normal']['bronze']
            elif self.materiau == 'gold':
                self.position = Rect.positions['normal']['gold']

    # fonction pour afficher les blocks
    def blit(self):
        self.surf.blit(pygame.image.load('Assets/Terrain/Terrain (16x16).png'), self.position)
        screen.blit(self.surf, (self.x, self.y))

