import pygame as pg
from Main_Character.main import NinjaFrog
from Dynamics.var import var

screen = pg.display.set_mode((1056, 792))


def fall():

    # Si le joueur est en train de tomber
    if var.fall:

        # le joueur poursuit sa chute
        var.y += 10
        var.height -= 10

        if not var.left:
            NinjaFrog.Fall.fall_right(var.x, var.y)
        else:
            NinjaFrog.Fall.fall_left(var.x, var.y)
        pg.display.flip()

        # petit lag pour rendre le jeu plus fluide
        pg.time.wait(40)

        # Si le joueur a fini sa chute
        if var.height == - 40:
            var.fall = False
            var.height = 0

        # Si le joueur cours en même temps qu'il saute alors il avance légèrement
        if var.run and var.fall:
            if var.left:
                var.x -= 6
                var.run = False
            else:
                var.x += 6
                var.run = False
