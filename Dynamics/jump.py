import pygame as pg
from Main_Character.main import NinjaFrog
from Dynamics.var import var

screen = pg.display.set_mode((1056, 792))


def jump():

    # Si dans le dictionnaire on trouve l'input correspondant à la barre d'espace à True

    # Si l'utilisateur appuie sur la barre d'espace ou bien qu'il est déjà en train de sauter
    if var.pressed.get(pg.K_SPACE) or var.jump:

        # Si le joueur n'est pas en train de tomber
        if not var.fall:

            # On fait sauter le joueur
            var.y -= 5
            var.jump = True
            var.height += 5

            # Si le joueur a sauté jusqu'au maximum de ses capacités
            if var.height == 40:
                var.jump = False
                var.fall = True
                var.height = 0

            # On affiche le joueur
            if not var.left:
                NinjaFrog.Jump.jump_right(var.x, var.y)
            else:
                NinjaFrog.Jump.jump_left(var.x, var.y)
            pg.display.flip()

            # Petit lag de 40 ms pour rendre le jeu plus fluide
            pg.time.wait(40)

        # Si le joueur cours en même temps qu'il saute alors il avance légèrement
        if var.run and var.jump:
            if var.left:
                var.x -= 3
                var.run = False
            else:
                var.x += 3
                var.run = False
