import pygame as pg
from Main_Character.main import NinjaFrog
from Dynamics.var import var

screen = pg.display.set_mode((1056, 792))


def idle():

    if not var.fall and not var.jump and not var.run:
        NinjaFrog.Idle.idle(var.x, var.y, var.i)
        pg.time.wait(40)
