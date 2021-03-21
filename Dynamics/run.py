import pygame as pg
from Main_Character.main import NinjaFrog
from Dynamics.var import Var

screen = pg.display.set_mode((1056, 792))


def run():

    # Si dans le dictionnaire on trouve l'input correspondant à la flèche de droite à True

    # Si l'utilisateur a appuyé sur la flèche de droite et pas celle de gauche
    if Var.pressed.get(pg.K_RIGHT) and not Var.pressed.get(pg.K_LEFT):

        # Si le joueur n'est ni en train de tomber, ni en train de sauter
        if not (Var.jump or Var.fall):

            # On cours
            Var.run = True
            Var.left = False
            Var.step_run += 1
            NinjaFrog.Run.run_right(Var.x, 100, Var.step_run)
            pg.display.flip()

            # Petit lag pour rendre le jeu plus fluide
            pg.time.wait(40)

            # Si l'utilisateur dépasse l'écran
            if Var.x > 1024:
                Var.x = 0
            else:
                Var.x += 5
        else:
            # On cours
            Var.run = True
            Var.left = False

    # Si dans le dictionnaire on trouve l'input correspondant à la flèche de gauche à True

    # Si l'utilisateur a appuyé sur la flèche de gauche et pas celle de droite
    if Var.pressed.get(pg.K_LEFT) and not Var.pressed.get(pg.K_RIGHT):

        # Si le joueur n'est ni en train de tomber, ni en train de sauter
        if not (Var.jump or Var.fall):

            # On cours
            Var.run = True
            Var.left = True
            Var.step_run += 1
            NinjaFrog.Run.run_left(Var.x, 100, Var.step_run)
            pg.display.flip()

            # Petit lag pour rendre le jeu plus fluide
            pg.time.wait(40)

            # Si l'utilisateur dépasse l'écran
            if Var.x < 0:
                Var.x = 1024
            else:
                Var.x -= 5

        else:
            # On cours
            Var.run = True
            Var.left = True

    # Si l'utilisateur ne cours pas ou bien appuie sur les deux f=touches (flèche droite et gauche)
    elif not Var.pressed.get(pg.K_RIGHT) and not Var.pressed.get(pg.K_LEFT) or not (
            not Var.pressed.get(pg.K_RIGHT) or not Var.pressed.get(pg.K_LEFT)):
        Var.run = False
        Var.step_run = 0
