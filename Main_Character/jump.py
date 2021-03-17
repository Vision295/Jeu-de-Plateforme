import pygame
from Background.main import Background as Bg

screen = pygame.display.set_mode((1056, 792))


# classe pour afficher le joueur lorsqu'il saute
class Jump:

    # fonction pour afficher le joueur en train de sauter
    @staticmethod
    def jump_right(x, y):
        Bg.Load.lvl_1()
        image = pygame.image.load('Assets/Main-Characters/Ninja-Frog/Jump (32x32).png')
        screen.blit(image, (x, y), (0, 0, 32, 32))
        return x, x + 32, y, y + 32

    # fonction pour afficher le joueur en train de sauter
    @staticmethod
    def jump_left(x, y):
        Bg.Load.lvl_1()
        image = pygame.transform.flip(pygame.image.load('Assets/Main-Characters/Ninja-Frog/Jump (32x32).png'), True, False)
        screen.blit(image, (x, y), (0, 0, 32, 32))
        return x, x + 32, y, y + 32

    # boucle qui affiche toute l'animation de saut
    @staticmethod
    def loop_jump(x, y, nbloop=1):
        for j in range(nbloop):
            for i in range(8):
                Bg.Load.lvl_1()
                Jump.jump_right(x, y)
                y -= 5
                pygame.display.flip()
                pygame.time.wait(50)
        Bg.Load.lvl_1()
