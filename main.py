import pygame
from game import Game
from player import Player
from Terrain.block import Block

""" COLLISION :
    
"""

# INITIALISATION DE PYGAME
pygame.init()

# On charge l'écran dans la variable screen
screen = pygame.display.set_mode((1056, 704))
background = pygame.Surface((1056, 704))
background.fill((0, 0, 0))

# INITIALISATION DE TOUTES LES VARIABLES
# Variable utilisée pour faire tourner le jeu en boucle
running = True
player = Player(100, 500, 1)
player2 = Player(600, 500, 2)
player3 = Player(700, 500, 3)
player4 = Player(800, 500, 4)
Game.all_sprites.add(player)
liste = [Block(300, 500, Block.block_coord('stone', 'smallSquare', 'roc')), Block(350, 450, Block.block_coord('stone', 'smallSquare', 'roc'))]

for i in range(22):
    liste.append(Block((i + 1) * 44, 532, Block.block_coord('grass', 'green')))
# BOUCLE DE JEU
while running:
    # Petit lag pour rendre le jeu fluide
    Game.clock.tick(Game.FPS)
    print(player.y + 25, player.y + 35, player.x, player.x + 32, player.block_dessous)
    # On affiche le fond d'écran en premier
    screen.blit(background, (0, 0))
    for i in range(len(liste)):
        liste[i].blit()
    # On parcours toutes les fonctions de déplacement du joueur 1
    Player.running(player)
    Player.idle(player)
    Player.jumping(player)
    Player.falling(player)

    # On parcours toutes les fonctions de déplacement du joueur 2
    Player.running(player2)
    Player.idle(player2)
    Player.jumping(player2)
    Player.falling(player2)

    # On parcours toutes les fonctions de déplacement du joueur 3
    Player.running(player3)
    Player.idle(player3)
    Player.jumping(player3)
    Player.falling(player3)

    # On parcours toutes les fonctions de déplacement du joueur 4
    Player.running(player4)
    Player.idle(player4)
    Player.jumping(player4)
    Player.falling(player4)

    # on change les positions des joueurs sur l'écran
    Player.set_position(player)
    Player.set_position(player2)
    Player.set_position(player3)
    Player.set_position(player4)

    # On met à jour l'écran
    pygame.display.flip()

    # On gère les touches pour le joueur 1
    if Game.pressed.get(pygame.K_RIGHT):
        Player.set_right(player)
    elif Game.pressed.get(pygame.K_LEFT):
        Player.set_left(player)
    else:
        Player.set_stop(player)
    if Game.pressed.get(pygame.K_UP) and not Player.get_falling(player):
        Player.set_jump(player)

    # On gère les touches pour le joueur 2
    if Game.pressed.get(pygame.K_d):
        Player.set_right(player2)
    elif Game.pressed.get(pygame.K_q):
        Player.set_left(player2)
    else:
        Player.set_stop(player2)
    if Game.pressed.get(pygame.K_z) and not Player.get_falling(player2):
        Player.set_jump(player2)

    # On gère les touches pour le joueur 3
    if Game.pressed.get(pygame.K_h):
        Player.set_right(player3)
    elif Game.pressed.get(pygame.K_f):
        Player.set_left(player3)
    else:
        Player.set_stop(player3)
    if Game.pressed.get(pygame.K_t) and not Player.get_falling(player3):
        Player.set_jump(player3)

    # On gère les touches pour le joueur 4
    if Game.pressed.get(pygame.K_l):
        Player.set_right(player4)
    elif Game.pressed.get(pygame.K_j):
        Player.set_left(player4)
    else:
        Player.set_stop(player4)
    if Game.pressed.get(pygame.K_i) and not Player.get_falling(player4):
        Player.set_jump(player4)

    # On utilise les inputs avec pygame
    for event in pygame.event.get():

        # Si l'utilisateur ferme la fenêtre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        # Si l'utilisateur maintiens une touche appuyée
        elif event.type == pygame.KEYDOWN:
            # On met la valeur de clé correspondante à l'input entré à True
            Game.pressed[event.key] = True

        # Si l'utilisateur lève une touche
        elif event.type == pygame.KEYUP:
            # On met la valeur de clé correspondante à l'input entré à False
            Game.pressed[event.key] = False
