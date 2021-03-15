import pygame
from Background.main import Background as Bg

screen = pygame.display.set_mode((1056, 792))


# classe pour afficher le joueur lorsqu'il est inactif
class Run:

    # fonction qui afficher le joueur lorsque ce dernier ne bouge pas
    @staticmethod
    def run(x, y, step):

        # Si on est à l'étape 1 de l'inactivité du personnage
        if step % 12 == 0:
            image = pygame.image.load('Assets/Main-Characters/Ninja-Frog/Run (32x32).png')
            screen.blit(image, (x, y), (0, 0, 32, 32))
            return x, x + 32, y, y + 32

        # Si on est à l'étape 2 de l'inactivité du personnage
        if step % 12 == 1:
            image = pygame.image.load('Assets/Main-Characters/Ninja-Frog/Run (32x32).png')
            screen.blit(image, (x, y), (32, 0, 32, 32))
            return x, x + 32, y, y + 32

        # Si on est à l'étape 3 de l'inactivité du personnage
        if step % 12 == 2:
            image = pygame.image.load('Assets/Main-Characters/Ninja-Frog/Run (32x32).png')
            screen.blit(image, (x, y), (64, 0, 32, 32))
            return x, x + 32, y, y + 32

        # Si on est à l'étape 4 de l'inactivité du personnage
        if step % 12 == 3:
            image = pygame.image.load('Assets/Main-Characters/Ninja-Frog/Run (32x32).png')
            screen.blit(image, (x, y), (96, 0, 32, 32))
            return x, x + 32, y, y + 32

        # Si on est à l'étape 5 de l'inactivité du personnage
        if step % 12 == 4:
            image = pygame.image.load('Assets/Main-Characters/Ninja-Frog/Run (32x32).png')
            screen.blit(image, (x, y), (128, 0, 32, 32))
            return x, x + 32, y, y + 32

        # Si on est à l'étape 6 de l'inactivité du personnage
        if step % 12 == 5:
            image = pygame.image.load('Assets/Main-Characters/Ninja-Frog/Run (32x32).png')
            screen.blit(image, (x, y), (160, 0, 32, 32))
            return x, x + 32, y, y + 32

        # Si on est à l'étape 7 de l'inactivité du personnage
        if step % 12 == 6:
            image = pygame.image.load('Assets/Main-Characters/Ninja-Frog/Run (32x32).png')
            screen.blit(image, (x, y), (192, 0, 32, 32))
            return x, x + 32, y, y + 32

        # Si on est à l'étape 8 de l'inactivité du personnage
        if step % 12 == 7:
            image = pygame.image.load('Assets/Main-Characters/Ninja-Frog/Run (32x32).png')
            screen.blit(image, (x, y), (224, 0, 32, 32))
            return x, x + 32, y, y + 32

        # Si on est à l'étape 9 de l'inactivité du personnage
        if step % 12 == 8:
            image = pygame.image.load('Assets/Main-Characters/Ninja-Frog/Run (32x32).png')
            screen.blit(image, (x, y), (256, 0, 32, 32))
            return x, x + 32, y, y + 32

        # Si on est à l'étape 10 de l'inactivité du personnage
        if step % 12 == 9:
            image = pygame.image.load('Assets/Main-Characters/Ninja-Frog/Run (32x32).png')
            screen.blit(image, (x, y), (288, 0, 32, 32))
            return x, x + 32, y, y + 32

        # Si on est à l'étape 11 de l'inactivité du personnage
        if step % 12 == 10:
            image = pygame.image.load('Assets/Main-Characters/Ninja-Frog/Run (32x32).png')
            screen.blit(image, (x, y), (320, 0, 32, 32))
            return x, x + 32, y, y + 32

        # Si on est à l'étape 12 de l'inactivité du personnage
        if step % 12 == 11:
            image = pygame.image.load('Assets/Main-Characters/Ninja-Frog/Run (32x32).png')
            screen.blit(image, (x, y), (352, 0, 32, 32))
            return x, x + 32, y, y + 32

    # fonction pour afficher le personnage bouger lorsqu'il est inactif
    @staticmethod
    def loop_run(x, y, nbloop=1):
        for j in range(nbloop):
            for i in range(11):
                Bg.Load.lvl_1()
                Run.run(x, y, i)
                x += 5
                pygame.display.flip()
                pygame.time.wait(50)
        Bg.Load.lvl_1()

