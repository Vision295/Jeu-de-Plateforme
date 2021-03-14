import pygame
from Background.main import Background as Bg

screen = pygame.display.set_mode((1056, 792))


# classe pour afficher le joueur lorsqu'il est inactif
class Idle:

    # fonction qui afficher le joueur lorsque ce dernier ne bouge pas
    @staticmethod
    def idle(x, y, step):

        # Si on est à l'étape 1 de l'inactivité du personnage
        if step % 11 == 0:
            image = pygame.image.load('Assets/Main-Characters/Ninja-Frog/Idle (32x32).png')
            screen.blit(image, (x, y), (0, 0, 32, 32))
            return x, x + 32, y, y + 32

        # Si on est à l'étape 2 de l'inactivité du personnage
        if step % 11 == 1:
            image = pygame.image.load('Assets/Main-Characters/Ninja-Frog/Idle (32x32).png')
            screen.blit(image, (x, y), (32, 0, 32, 32))
            return x, x + 32, y, y + 32

        # Si on est à l'étape 3 de l'inactivité du personnage
        if step % 11 == 2:
            image = pygame.image.load('Assets/Main-Characters/Ninja-Frog/Idle (32x32).png')
            screen.blit(image, (x, y), (64, 0, 32, 32))
            return x, x + 32, y, y + 32

        # Si on est à l'étape 4 de l'inactivité du personnage
        if 11 % step == 3:
            image = pygame.image.load('Assets/Main-Characters/Ninja-Frog/Idle (32x32).png')
            screen.blit(image, (x, y), (96, 0, 32, 32))
            return x, x + 32, y, y + 32

        # Si on est à l'étape 5 de l'inactivité du personnage
        if 11 % step == 4:
            image = pygame.image.load('Assets/Main-Characters/Ninja-Frog/Idle (32x32).png')
            screen.blit(image, (x, y), (128, 0, 32, 32))
            return x, x + 32, y, y + 32

        # Si on est à l'étape 6 de l'inactivité du personnage
        if 11 % step == 5:
            image = pygame.image.load('Assets/Main-Characters/Ninja-Frog/Idle (32x32).png')
            screen.blit(image, (x, y), (160, 0, 32, 32))
            return x, x + 32, y, y + 32

        # Si on est à l'étape 7 de l'inactivité du personnage
        if 11 % step == 6:
            image = pygame.image.load('Assets/Main-Characters/Ninja-Frog/Idle (32x32).png')
            screen.blit(image, (x, y), (192, 0, 32, 32))
            return x, x + 32, y, y + 32

        # Si on est à l'étape 8 de l'inactivité du personnage
        if 11 % step == 7:
            image = pygame.image.load('Assets/Main-Characters/Ninja-Frog/Idle (32x32).png')
            screen.blit(image, (x, y), (224, 0, 32, 32))
            return x, x + 32, y, y + 32

        # Si on est à l'étape 9 de l'inactivité du personnage
        if 11 % step == 8:
            image = pygame.image.load('Assets/Main-Characters/Ninja-Frog/Idle (32x32).png')
            screen.blit(image, (x, y), (256, 0, 32, 32))
            return x, x + 32, y, y + 32

        # Si on est à l'étape 10 de l'inactivité du personnage
        if 11 % step == 9:
            image = pygame.image.load('Assets/Main-Characters/Ninja-Frog/Idle (32x32).png')
            screen.blit(image, (x, y), (288, 0, 32, 32))
            return x, x + 32, y, y + 32

        # Si on est à l'étape 11 de l'inactivité du personnage
        if 11 % step == 10:
            image = pygame.image.load('Assets/Main-Characters/Ninja-Frog/Idle (32x32).png')
            screen.blit(image, (x, y), (320, 0, 32, 32))
            return x, x + 32, y, y + 32

    # fonction pour afficher le personnage bouger lorsqu'il est inactif
    @staticmethod
    def loop_idle(nbloop=1):
        for j in range(nbloop):
            for i in range(11):
                Idle.idle(10, 100, i)
                pygame.display.flip()
                pygame.time.wait(10)
            Bg.load_background()
