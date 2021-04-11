import pygame


class Game:
    """
    Classe qui permet de stocker les variables propres au jeu en lui même.
    C'est une classe génériques les valeurs dedant peuvent ainsi être manipulés
    facilement.
    """

    # dictionnaire qui stocke les différents inputs (touches pressées)
    pressed = {}

    # groupe (pour l'instant inutil) qui stocke tous les objets sprite du jeu
    all_sprites = pygame.sprite.Group()

    # horloge controlant les fps (frame per second)
    clock = pygame.time.Clock()
    FPS = 20

    # dictionnaire stockant les différentes positions relatives des sprites du jeu
    positions = {}

    # le nombre de blocks total
    nb_block = 0
