import pygame
from Main_Character.idle import Idle
from Main_Character.jump import Jump

screen = pygame.display.set_mode((1056, 792))


class NinjaFrog:

    Idle = Idle()

    Jump = Jump()
