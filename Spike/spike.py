import pygame

screen = pygame.display.set_mode((1280, 800))


class Spike:

    position = (0, 0)

    taille = (32, 16)

    # affiche à l'écran un pique aux coordonnées (x, y)
    @staticmethod
    def spike(x, y):
        screen.blit(pygame.image.load('Assets/Traps/Spikes/Idle.png'), (x, y))
        return x, x + 32, y, y + 16
