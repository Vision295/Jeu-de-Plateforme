import pygame
from game import Game
from Terrain.block_info import BlockInfo

screen = pygame.display.set_mode((1280, 800))


# pierres en forme de rectangle
class Block:

    """
        Classe qui permet de créer des blocs de tous les types. On y trouve une fonction
        qui permet de l'afficher (blit). On trouve une fonction pour trouver le bon block
        à afficher (block_info)
    """

    # fonction qui renvoie la position d'un type de block
    @staticmethod
    def block_coord(materiau, forme, matiere='roc', rotation=False):
        if materiau == 'stone':
            if forme == 'rect':
                return BlockInfo.blocks['stone'][forme][rotation][matiere]
            else:
                return BlockInfo.blocks['stone'][forme][matiere]
        else:
            return BlockInfo.blocks[materiau][forme]

    # fonction pour créer un block
    def __init__(self, x, y, block_coord):

        # nombre total de block
        Game.nb_block += 1

        # coordonées du block sur l'écran
        self.x = x
        self.y = y

        # coordonée qui représente le block sur l'image terrain
        self.block_coord = block_coord[0]

        # taille du block
        self.taille = block_coord[1]

        # surface du block
        self.surf = pygame.Surface(self.taille)

        # on ajoute le block à l'ensemble des positions relatives
        Game.positions[Game.nb_block] = (self.x, self.y, self.x + self.taille[0], self.y + self.taille[1])

    # fonction pour afficher les blocks
    def blit(self):
        self.surf.blit(pygame.image.load('Assets/Terrain/Terrain (16x16).png'), self.block_coord)
        screen.blit(self.surf, (self.x, self.y))
