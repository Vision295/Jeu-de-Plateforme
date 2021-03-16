import pygame
from Dynamics.jump import jump
from Dynamics.idle import idle
from Dynamics.fall import fall
from Dynamics.run import run

screen = pygame.display.set_mode((1056, 792))


class Dynamics:

    @staticmethod
    def jump():
        jump()

    @staticmethod
    def idle():
        idle()

    @staticmethod
    def run():
        run()

    @staticmethod
    def fall():
        fall()