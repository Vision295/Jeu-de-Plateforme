import pygame as pg
from Main_Character.main import NinjaFrog
from Dynamics.var import Var

screen = pg.display.set_mode((1056, 792))


def jump():

    # Si dans le dictionnaire on trouve l'input correspondant à la barre d'espace à True

    # Si l'utilisateur appuie sur la barre d'espace ou bien qu'il est déjà en train de sauter
    if Var.pressed.get(pg.K_SPACE) or Var.jump:

        # Si le joueur n'est pas en train de tomber
        if not Var.fall:

            # On fait sauter le joueur
            Var.y -= 5
            Var.jump = True
            Var.height += 5

            # Si le joueur a sauté jusqu'au maximum de ses capacités
            if Var.height == 40:
                Var.jump = False
                Var.fall = True
                Var.height = 0

            # On affiche le joueur
            if not Var.left:
                NinjaFrog.Jump.jump_right(Var.x, Var.y)
            else:
                NinjaFrog.Jump.jump_left(Var.x, Var.y)
            pg.display.flip()

            # Petit lag de 40 ms pour rendre le jeu plus fluide
            pg.time.wait(20)

        # Si le joueur cours en même temps qu'il saute alors il avance légèrement
        if Var.run and Var.jump:
            if Var.left:
                Var.x -= 3
                Var.run = False
            else:
                Var.x += 3
                Var.run = False
