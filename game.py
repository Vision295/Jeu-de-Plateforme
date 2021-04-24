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

    screen = pygame.display.set_mode((1280, 800))

    # Differentes images chargées avec pygame pour le background
    blue = pygame.image.load('Assets/Background/Blue.png')
    brown = pygame.image.load('Assets/Background/Brown.png')
    gray = pygame.image.load('Assets/Background/Gray.png')
    green = pygame.image.load('Assets/Background/Green.png')
    pink = pygame.image.load('Assets/Background/Pink.png')
    purple = pygame.image.load('Assets/Background/Purple.png')
    yellow = pygame.image.load('Assets/Background/Yellow.png')

    list = [blue, brown, gray, green, pink, purple, yellow]

    # Fonction pour charger le fond d'écran aléatoirement
    @staticmethod
    def lvl(level):
        for x in range(0, 1280, 64):
            for y in range(0, 896, 64):
                Game.screen.blit(Game.list[level], (x, y))
