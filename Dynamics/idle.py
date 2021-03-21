import pygame as pg
from Main_Character.main import NinjaFrog
from Dynamics.var import Var

screen = pg.display.set_mode((1056, 792))


def idle():

    if not Var.fall and not Var.jump and not Var.run:
        NinjaFrog.Idle.idle(Var.x, Var.y, Var.step_idle)
        pg.time.wait(40)
