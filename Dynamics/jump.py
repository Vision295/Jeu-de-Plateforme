import pygame as pg
from Main_Character.main import NinjaFrog
from Dynamics.var import var

screen = pg.display.set_mode((1056, 792))


def jump():
    # Si dans le dictionnaire on trouve l'input correspondant à la barre d'espace à True
    if var.pressed.get(pg.K_SPACE) or var.jump:
        if not var.fall:
            var.y -= 5
            var.jump = True
            var.height += 5
            if var.height == 40:
                var.jump = False
                var.fall = True
                var.height = 0
            NinjaFrog.Jump.jump(var.x, var.y)
            pg.display.flip()
            pg.time.wait(40)
        if var.run and var.jump:
            var.x += 2
            var.run = False
