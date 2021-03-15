import pygame
from Background.main import Background as Bg

screen = pygame.display.set_mode((1056, 792))


# classe pour afficher le joueur lorsqu'il est inactif
class Fall:

    @staticmethod
    def fall(x, y):
        Bg.Load.lvl_1()
        image = pygame.image.load('Assets/Main-Characters/Ninja-Frog/Fall (32x32).png')
        screen.blit(image, (x, y), (0, 0, 32, 32))
        return x, x + 32, y, y + 32
