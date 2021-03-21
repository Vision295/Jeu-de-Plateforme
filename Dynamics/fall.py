import pygame as pg
from Main_Character.main import NinjaFrog
from Dynamics.var import Var

screen = pg.display.set_mode((1056, 792))


def fall():

    # Si le joueur est en train de tomber
    if Var.fall:

        # le joueur poursuit sa chute
        Var.y += 10
        Var.height -= 10

        if not Var.left:
            NinjaFrog.Fall.fall_right(Var.x, Var.y)
        else:
            NinjaFrog.Fall.fall_left(Var.x, Var.y)
        pg.display.flip()

        # petit lag pour rendre le jeu plus fluide
        pg.time.wait(20)

        # Si le joueur a fini sa chute
        if Var.height == - 40:
            Var.fall = False
            Var.height = 0

        # Si le joueur cours en même temps qu'il saute alors il avance légèrement
        if Var.run and Var.fall:
            if Var.left:
                Var.x -= 6
                Var.run = False
            else:
                Var.x += 6
                Var.run = False
