import pygame as pg
from Main_Character.main import NinjaFrog
from Dynamics.var import var

screen = pg.display.set_mode((1056, 792))


def fall():
    if var.fall:
        var.y += 10
        var.height -= 10
        NinjaFrog.Fall.fall(var.x, var.y)
        pg.display.flip()
        pg.time.wait(40)
        if var.height == - 40:
            var.fall = False
            var.height = 0