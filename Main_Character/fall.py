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

    # fonction pour afficher le personnage bouger lorsqu'il est inactif
    @staticmethod
    def loop_fall(x, y, nbloop=1):
        for j in range(nbloop):
            for i in range(4):
                Bg.Load.lvl_1()
                Fall.fall(x, y - 40)
                y += 10
                pygame.display.flip()
                pygame.time.wait(50)
        Bg.Load.lvl_1()
