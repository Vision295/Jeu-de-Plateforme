import pygame
from game import Game

screen = pygame.display.set_mode((3, 3))


# classe pour gérer le(s) personnage(s) principal(aux) todo: spawn points, win and lose (death and checkpoints, ...)
class Player(pygame.sprite.Sprite):

    """
    Classe utilisée pour gérer le joueur. Dans cette classe on trouve les différents
    mouvements que peut effectuer le joueur :
        - falling
        - jumping
        - running
        - idle
    On retrouve aussi des fonctions pour récupérer certaines valeurs et les modifier:
        - get_falling (permet de savoir si le joueur est en train de tomber)
        - set_right
        - set_left
        - set_jump
        - set_stop
        - set_position (permet de mettre à jour la position du joueur dans le dictionnarie position de la classe Game)
    """

    # fonction pour créer un personnage
    def __init__(self, x=100, y=100, choix_perso=1):

        # On instancie le personnage en tant que sprite pygame
        pygame.sprite.Sprite.__init__(self)

        # choix du personnage
        # 1 <=> Ninja_frog
        # 2 <=> Mask Dude
        # 3 <=> Pink Man
        # 4 <=> Vitrual Guys
        self.choix_perso = choix_perso
        if self.choix_perso == 1:
            self.idle = pygame.image.load('Assets/Main-Characters/Ninja-Frog/Idle (32x32).png')
            self.run = pygame.image.load('Assets/Main-Characters/Ninja-Frog/Run (32x32).png')
            self.jump = pygame.image.load('Assets/Main-Characters/Ninja-Frog/Jump (32x32).png')
            self.fall = pygame.image.load('Assets/Main-Characters/Ninja-Frog/Fall (32x32).png')
        elif self.choix_perso == 2:
            self.idle = pygame.image.load('Assets/Main-Characters/Mask Dude/Idle (32x32).png')
            self.run = pygame.image.load('Assets/Main-Characters/Mask Dude/Run (32x32).png')
            self.jump = pygame.image.load('Assets/Main-Characters/Mask Dude/Jump (32x32).png')
            self.fall = pygame.image.load('Assets/Main-Characters/Mask Dude/Fall (32x32).png')
        elif self.choix_perso == 3:
            self.idle = pygame.image.load('Assets/Main-Characters/Pink Man/Idle (32x32).png')
            self.run = pygame.image.load('Assets/Main-Characters/Pink Man/Run (32x32).png')
            self.jump = pygame.image.load('Assets/Main-Characters/Pink Man/Jump (32x32).png')
            self.fall = pygame.image.load('Assets/Main-Characters/Pink Man/Fall (32x32).png')
        elif self.choix_perso == 4:
            self.idle = pygame.image.load('Assets/Main-Characters/Virtual Guy/Idle (32x32).png')
            self.run = pygame.image.load('Assets/Main-Characters/Virtual Guy/Run (32x32).png')
            self.jump = pygame.image.load('Assets/Main-Characters/Virtual Guy/Jump (32x32).png')
            self.fall = pygame.image.load('Assets/Main-Characters/Virtual Guy/Fall (32x32).png')

        # rectangle correspondant à la hitbox du personnage
        self.rect = pygame.Rect(0, 0, 32, 32)

        # avancée de la course ou bien dans l'inactivité
        self.step = 0

        # coordonnées du joueur (du coin suppérieur droit du rectangle)
        self.x = x
        self.y = y

        # le joueur est en train de sauter
        self.jumping = False
        # le joueur est en train de tomber
        self.falling = False
        # le joueur est inactif
        self.stop = False

        # le nombre de block en dessous du joueur
        self.block_dessous = 1

        # la direction du joueur
        self.direction = 'NONE'

        # la hauteur du saut
        self.height = 0

    # fonction pour animer le joueur lorsqu'il est inactif
    def idle(self, step=1):

        # si le joueur ne bouge pas et ne saute pas mais est orienté vers la droite ou bien l'objet vient d'être créé
        if (self.stop and self.height == 0 and self.direction == 'RIGHT') or self.direction == 'NONE':

            # on affiche le joueur en fonction de l'anvancement de son inactivité
            self.step += step
            screen.blit(self.idle, (self.x, self.y), ((self.step % 11) * 32, 0, 32, 32))

        # si le joueur ne bouge pas et ne saute pas mais est orienté vers la gauche
        elif self.stop and self.height == 0 and self.direction == 'LEFT':

            # on affiche le joueur en fonction de l'anvancement de son inactivité
            self.step += step
            screen.blit(pygame.transform.flip(self.idle, True, False), (self.x, self.y),
                        ((self.step % 11) * 32, 0, 32, 32))

    # fonction pour animer le joueur tout en le faisant courrir
    def running(self, step=1):
        # avancement de la course
        self.step += step

        # si le joueur court vers la droite
        if self.direction == 'RIGHT' and not self.stop:

            # si le joueur saute pendant qu'il essaie de courrir
            if self.jumping or self.falling:
                self.x += 4

            # si le joueur court simplement
            else:
                screen.blit(self.run, (self.x, self.y), ((self.step % 12) * 32, 0, 32, 32))
                self.x += 5

            # On parcours le dictionnaire à la recherche d'un obstacle
            for i in range(Game.nb_block):
                if self.x + 15 < Game.positions[i + 1][0] <= self.x + 25 and (self.y < Game.positions[i + 1][1] < self.y + 32 or self.y < Game.positions[i + 1][3] < self.y + 32):
                    if self.jumping or self.falling:
                        self.x -= 4
                    else:
                        self.x -= 5

        # si le joueur court vers la gauche
        elif self.direction == 'LEFT' and not self.stop:

            # si le joueur saute pendant qu'il essaie de courrir
            if self.jumping or self.falling:
                self.x -= 4

            # si le joueur court simplement
            else:
                screen.blit(pygame.transform.flip(self.run, True, False), (self.x, self.y), ((self.step % 12) * 32, 0, 32, 32))
                self.x -= 5

            # On parcours le dictionnaire à la recherche d'un obstacle
            for i in range(Game.nb_block):
                if self.x + 8 <= Game.positions[i + 1][2] <= self.x + 12 and (self.y < Game.positions[i + 1][1] < self.y + 32 or self.y < Game.positions[i + 1][3] < self.y + 32):
                    if self.jumping or self.falling:
                        self.x += 4
                    else:
                        self.x += 5

    # fonction pour animer le joueur tout en le faisant sauter
    def jumping(self):

        # si le joueur saute vers la droite
        if (self.direction == 'RIGHT' or self.direction == 'NONE') and self.jumping:

            # on affiche le joueur en train de sauter
            screen.blit(self.jump, (self.x, self.y), (0, 0, 32, 32))
            self.y -= 8

            # on mesure l'avancement de son saut (sa hauteur)
            self.height += 8

        # si le joueur saute vers la gauche
        elif (self.direction == 'LEFT' or self.direction == 'NONE') and self.jumping:

            # on affiche le joueur en train de sauter
            screen.blit(pygame.transform.flip(self.jump, True, False), (self.x, self.y), (0, 0, 32, 32))
            self.y -= 8

            # on mesure l'avancement de son saut (sa hauteur)
            self.height += 8

        # On parcours le dictionnaire à la recherche d'un obstacle
        for i in range(Game.nb_block):
            if self.y > Game.positions[i + 1][1] >= self.y - 8 and (Game.positions[i + 1][0] <= self.x + 8 <= Game.positions[i + 1][2] or Game.positions[i + 1][0] <= self.x + 24 <= Game.positions[i + 1][2] or (self.x + 8 <= Game.positions[i + 1][0] and self.x + 24 >= Game.positions[i + 1][2])):
                self.jumping = False
                self.height = 80

    # fonction qui permet d'animer le joueur tout en le faisant sauter
    def falling(self):

        if self.block_dessous == 0 and not self.falling and not self.jumping:
            self.falling = True
            self.jumping = False
            self.stop = False
            self.height += 8
        else:
            self.block_dessous = 0

        # On parcours le dictionnaire à la recherche d'un obstacle
        for i in range(Game.nb_block):
            if self.y + 24 < Game.positions[i + 1][1] <= self.y + 32 and (Game.positions[i + 1][0] <= self.x + 8 <= Game.positions[i + 1][2] or Game.positions[i + 1][0] <= self.x + 24 <= Game.positions[i + 1][2] or (self.x + 8 <= Game.positions[i + 1][0] and self.x + 24 >= Game.positions[i + 1][2])):
                self.block_dessous += 1
                self.height = 0

        # si le joueur tombe vers la droite
        if (self.direction == 'RIGHT' or self.direction == 'NONE') and self.falling and self.height > 0:

            # on affiche le joueur en train de tomber
            screen.blit(self.fall, (self.x, self.y), (0, 0, 32, 32))
            self.y += 8
            self.height -= 8

        # si le joueur tombe vers la gauche
        elif self.direction == 'LEFT' and self.falling and self.height > 0:

            # on affiche le joueur en train de tomber
            screen.blit(pygame.transform.flip(self.fall, True, False), (self.x, self.y), (0, 0, 32, 32))
            self.y += 8
            self.height -= 8

        # si le joueur a atteint la hauteur maximum de son saut alors il tombe
        if self.height == 80:
            self.falling = True
            self.jumping = False

        # si le joueur a atteint la fin de sa chut
        if self.height == 0:
            self.jumping = False
            self.falling = False
            self.stop = True

    # fonction qui fixe la position du joueur
    def set_position(self):

        if self.choix_perso == 1:
            # ajout des positions à la liste des positions
            Game.positions['player'] = (self.x, self.y, self.x + 32, self.y + 32)
        elif self.choix_perso == 2:
            # ajout des positions à la liste des positions
            Game.positions['player2'] = (self.x, self.y, self.x + 32, self.y + 32)
        elif self.choix_perso == 3:
            # ajout des positions à la liste des positions
            Game.positions['player3'] = (self.x, self.y, self.x + 32, self.y + 32)
        elif self.choix_perso == 4:
            # ajout des positions à la liste des positions
            Game.positions['player4'] = (self.x, self.y, self.x + 32, self.y + 32)

    # fonction pour changer la direction du joueur en LEFT
    def set_left(self):
        self.direction = 'LEFT'
        self.stop = False

    # fonction pour changer la direction du joueur en RIGHT
    def set_right(self):
        self.direction = 'RIGHT'
        self.stop = False

    # fonction pour changer la direction du joueur en NONE
    def set_stop(self):
        self.stop = True

    # fonction pour changer l'état de saut du joueur à True
    def set_jump(self):
        if self.block_dessous > 0:
            self.jumping = True

    # fonction pour savoir si le joueur est en train de tomber
    def get_falling(self):
        return self.falling
