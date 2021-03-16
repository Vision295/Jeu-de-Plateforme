import pygame as pg
from Main_Character.main import NinjaFrog
from Dynamics.var import var

screen = pg.display.set_mode((1056, 792))


def run():
    # Si dans le dictionnaire on trouve l'input correspondant à la flèche de droite à True
    if var.pressed.get(pg.K_RIGHT):
        if not (var.jump or var.fall):
            # On cours
            var.run = True
            var.j += 1
            NinjaFrog.Run.run(var.x, 100, var.j)
            pg.display.flip()
            pg.time.wait(40)

        # Si l'utilisateur dépasse l'écran
        if var.x > 1024:
            var.x = 0
        else:
            var.x += 5

    # Si dans le dictionnaire on trouve l'input correspondant à la flèche de droite à False
    elif not var.pressed.get(pg.K_RIGHT):
        var.run = False
        var.j = 0
