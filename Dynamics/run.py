import pygame as pg
from Main_Character.main import NinjaFrog
from Dynamics.var import var

screen = pg.display.set_mode((1056, 792))


def run():

    # Si dans le dictionnaire on trouve l'input correspondant à la flèche de droite à True

    # Si l'utilisateur a appuyé sur la flèche de droite et pas celle de gauche
    if var.pressed.get(pg.K_RIGHT) and not var.pressed.get(pg.K_LEFT):

        # Si le joueur n'est ni en train de tomber, ni en train de sauter
        if not (var.jump or var.fall):

            # On cours
            var.run = True
            var.left = False
            var.step_run += 1
            NinjaFrog.Run.run_right(var.x, 100, var.step_run)
            pg.display.flip()

            # Petit lag pour rendre le jeu plus fluide
            pg.time.wait(40)

        # Si l'utilisateur dépasse l'écran
        if var.x > 1024:
            var.x = 0
        else:
            var.x += 5

    # Si dans le dictionnaire on trouve l'input correspondant à la flèche de gauche à True

    # Si l'utilisateur a appuyé sur la flèche de gauche et pas celle de droite
    if var.pressed.get(pg.K_LEFT) and not var.pressed.get(pg.K_RIGHT):

        # Si le joueur n'est ni en train de tomber, ni en train de sauter
        if not (var.jump or var.fall):

            # On cours
            var.run = True
            var.left = True
            var.step_run += 1
            NinjaFrog.Run.run_left(var.x, 100, var.step_run)
            pg.display.flip()

            # Petit lag pour rendre le jeu plus fluide
            pg.time.wait(40)

        # Si l'utilisateur dépasse l'écran
        if var.x < 0:
            var.x = 1024
        else:
            var.x -= 5

    # Si l'utilisateur ne cours pas ou bien appuie sur les deux f=touches (flèche droite et gauche)
    elif not var.pressed.get(pg.K_RIGHT) and not var.pressed.get(pg.K_LEFT) or not (
            not var.pressed.get(pg.K_RIGHT) or not var.pressed.get(pg.K_LEFT)):
        var.run = False
        var.step_run = 0
