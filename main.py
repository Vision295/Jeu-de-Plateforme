import pygame
from game import Game
from player import Player
from Terrain.block import Block


# INITIALISATION DE PYGAME
pygame.init()

# On charge l'écran dans la variable screen
screen = pygame.display.set_mode((1056, 704))
background = pygame.Surface((1056, 704))
background.fill((0, 0, 0))

# INITIALISATION DE TOUTES LES VARIABLES
# Variable utilisée pour faire tourner le jeu en boucle
running = True
player = Player(1, 628, 1)
Game.all_sprites.add(player)
liste = [
    Block(0, 660, Block.block_coord('grass', 'green')),
    Block(44, 616, Block.block_coord('grass', 'green')),
    Block(44, 660, Block.block_coord('dirt', 'green')),
    Block(44, 680, Block.block_coord('dirt', 'green')),
    Block(88, 384, Block.block_coord('grass', 'green')),
    Block(132, 192, Block.block_coord('grass', 'green')),
]
for i in range(12):
    liste.append(Block(88, 372 + 26 * (i + 1), Block.block_coord('dirt', 'green')),)
for i in range(24):
    liste.append(Block(132, 192 + 26 * (i + 1), Block.block_coord('dirt', 'green')),)

liste.append(Block(72, 600, Block.block_coord('stone', 'rect', 'roc')))
liste.append(Block(72, 552, Block.block_coord('stone', 'rect', 'roc', True)))
liste.append(Block(88, 568, Block.block_coord('stone', 'bigSquare', 'roc')))
liste.append(Block(72, 520, Block.block_coord('stone', 'smallSquare', 'roc')))
liste.append(Block(72, 536, Block.block_coord('stone', 'smallSquare', 'roc')))
liste.append(Block(72, 504, Block.block_coord('stone', 'smallSquare', 'roc')))
liste.append(Block(104, 504, Block.block_coord('stone', 'smallSquare', 'roc', True)))
liste.append(Block(72, 488, Block.block_coord('stone', 'rect', 'roc')))
liste.append(Block(0, 544, Block.block_coord('stone', 'platform', 'roc')))
liste.append(Block(0, 448, Block.block_coord('stone', 'platform', 'roc')))
liste.append(Block(40, 400, Block.block_coord('stone', 'platform', 'roc')))
liste.append(Block(116, 368, Block.block_coord('stone', 'smallSquare', 'roc')))
liste.append(Block(0, 320, Block.block_coord('stone', 'bigSquare', 'roc')))
liste.append(Block(32, 336, Block.block_coord('stone', 'bigSquare', 'roc')))
liste.append(Block(0, 304, Block.block_coord('stone', 'rect', 'roc')))
liste.append(Block(48, 320, Block.block_coord('stone', 'rect', 'roc')))
liste.append(Block(48, 304, Block.block_coord('stone', 'smallSquare', 'roc')))
liste.append(Block(48, 256, Block.block_coord('stone', 'rect', 'roc', True)))
liste.append(Block(116, 272, Block.block_coord('stone', 'rect', 'roc')))
liste.append(Block(100, 240, Block.block_coord('stone', 'bigSquare', 'roc')))
liste.append(Block(84, 224, Block.block_coord('stone', 'rect', 'roc')))
# BOUCLE DE JEU
while running:
    # Petit lag pour rendre le jeu fluide
    Game.clock.tick(Game.FPS)
    # On affiche le fond d'écran en premier
    Game.lvl(1)
    for i in range(len(liste)):
        liste[i].blit()

    # On parcours toutes les fonctions de déplacement du joueur 1
    Player.running(player)
    Player.idle(player)
    Player.jumping(player)
    Player.falling(player)
    Player.limits(player)
    Player.spike(player)

    # on change les positions des joueurs sur l'écran
    Player.set_position(player)

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
