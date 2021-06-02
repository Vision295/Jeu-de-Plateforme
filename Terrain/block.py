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
    def block_coord(materiau, forme_ou_couleur, matiere_ou_rotation='roc', rotation=False):
        if materiau == 'stone':
            if forme_ou_couleur == 'rect':
                return BlockInfo.blocks['stone'][forme_ou_couleur][rotation][matiere_ou_rotation]
            else:
                return BlockInfo.blocks['stone'][forme_ou_couleur][matiere_ou_rotation]
        elif materiau == 'stone2' or materiau == 'wood':
            if forme_ou_couleur == 'rect' or forme_ou_couleur == 'small_rect':
                return BlockInfo.blocks[materiau][forme_ou_couleur][matiere_ou_rotation]
            else:
                return BlockInfo.blocks[materiau][forme_ou_couleur]
        else:
            return BlockInfo.blocks[materiau][forme_ou_couleur]

    # fonction pour créer un block
    def __init__(self, x, y, block_coord, spike=False):

        # nombre total de block
        Game.nb_block += 1

        # coordonées du block sur l'écran
        self.x = x
        self.y = y
        self.spike = spike

        # coordonée qui représente le block sur l'image terrain
        self.block_coord = block_coord[0]

        # taille du block
        self.taille = block_coord[1]

        # surface du block
        self.surf = pygame.Surface(self.taille)

        # on ajoute le block à l'ensemble des positions relatives
        if block_coord != ((0, 0), (16, 8)) or block_coord != ((0, -16), (8, 16)) or block_coord != ((0, -8), (8, 8)) or block_coord != ((-8, -33), (6, 6)) or block_coord != ((-8, -64), (32, 9)) or block_coord != ((0, -72), (9, 32)) or block_coord != ((-8, -100), (8, 4)) or block_coord != ((-8, -72), (4, 8)) or block_coord != ((0, -64), (9, 9)):
            Game.positions[Game.nb_block] = (self.x, self.y, self.x + self.taille[0], self.y + self.taille[1], self.spike)

    # fonction pour afficher les blocks
    def blit(self):
        self.surf.blit(pygame.image.load('Assets/Terrain/Terrain (16x16).png'), self.block_coord)
        screen.blit(self.surf, (self.x, self.y))
