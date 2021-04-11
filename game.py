import pygame


class Game:

    pressed = {}
    all_sprites = pygame.sprite.Group()
    clock = pygame.time.Clock()
    FPS = 20
    positions = {}
