import pygame
from values.config import *
import math
import random


class Spritesheet:
    def __init__(self, file):
        self.sheet = pygame.image.load(file).convert()

    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface([width, height])
        # what we are drawing, where to start drawing it, and the selected cutout
        sprite.blit(self.sheet, (0, 0), (x, y, width, height))
        sprite.set_colorkey(BLACK)
        return sprite


# class Player(pygame.sprite.Sprite):
#     def __init__(self, game, x, y, stats, selected_character):
#         self.game = game
#         self._layer = PLAYER_LAYER
#         # add in the player to the all sprites group
#         self.groups = self.game.all_sprites
#         # call the init method of inherited class
#         pygame.sprite.Sprite.__init__(self, self.groups)
#
#         self.x = x * TILE_SIZE
#         self.y = y * TILE_SIZE
#         self.width = TILE_SIZE
#         self.height = TILE_SIZE
#
#         self.x_change = 0
#         self.y_change = 0
#
#         self.facing = 'down'
#         self.health = stats[0]
#         self.wisdom = stats[1]
#         self.stress = stats[2]
#         self.selected_character = selected_character
#
#         # draw stats
#         # StatusDisplay(40, 10, 100, 30, self.game, self)
#         self.animation_loop = 1
#
#         # image_to_load = pygame.image.load("img/d20.png")
#
#         # set surface as player's image or what it looks like
#         # self.image = pygame.Surface([self.width, self.height])
#         #self.image = self.game.character_spritesheet.get_sprite(3, 2, self.width, self.height)
#         self.image = self.game.character_spritesheet[self.selected_character].get_sprite(3, 2, self.width, self.height)
#         # self.image.fill(RED) instead of filling with red we are going to place an image
#         # select image and where to draw it on the surface
#         # self.image.blit(image_to_load, (0, 0))
#         # self.image.set_colorkey(BLACK)
#         # rect is where its positioned and size like a hitbox
#         self.rect = self.image.get_rect()  # setting hitbox to same size as image
#         # tell pygame the coords of our rectangle
#         self.rect.x = self.x
#         self.rect.y = self.y
#         # set our animations
#         self.down_animations = [self.game.character_spritesheet[self.selected_character].get_sprite(3, 2, self.width, self.height),
#                                 self.game.character_spritesheet[self.selected_character].get_sprite(35, 2, self.width, self.height),
#                                 self.game.character_spritesheet[self.selected_character].get_sprite(68, 2, self.width, self.height)]
#
#         self.left_animations = [self.game.character_spritesheet[self.selected_character].get_sprite(3, 34, self.width, self.height),
#                               self.game.character_spritesheet[self.selected_character].get_sprite(35, 34, self.width, self.height),
#                               self.game.character_spritesheet[self.selected_character].get_sprite(68, 34, self.width, self.height)]
#
#         self.up_animations = [self.game.character_spritesheet[self.selected_character].get_sprite(3, 98, self.width, self.height),
#                                 self.game.character_spritesheet[self.selected_character].get_sprite(35, 98, self.width, self.height),
#                                 self.game.character_spritesheet[self.selected_character].get_sprite(68, 98, self.width, self.height)]
#
#         self.right_animations = [self.game.character_spritesheet[self.selected_character].get_sprite(3, 66, self.width, self.height),
#                                  self.game.character_spritesheet[self.selected_character].get_sprite(35, 66, self.width, self.height),
#                                  self.game.character_spritesheet[self.selected_character].get_sprite(68, 66, self.width, self.height)]
#
#         self.status = {'health': 8, 'wisdom': 7, 'stress': 6, 'speed': 50}
#         # pass game, x y coords and the status to apply
#         StatusDisplay(self.game, 10, 5, self.status)
#     def update(self):
#         self.movement()
#         self.animate()
#         self.collide_enemy()
#         self.rect.x += self.x_change
#         # check for collision along x-axis
#         self.collide_blocks('x')
#         self.rect.y += self.y_change
#         # check for collision along y-axis
#         self.collide_blocks('y')
#
#         self.x_change = 0
#         self.y_change = 0
#
#     def movement(self):
#         keys = pygame.key.get_pressed()
#         if keys[pygame.K_LEFT]:
#             # simulate camera by keeping player in the middle
#             if FOLLOW_CAM:
#                 for sprite in self.game.all_sprites:
#                     sprite.rect.x += PLAYER_SPEED
#             self.x_change -= PLAYER_SPEED
#             self.facing = 'left'
#         if keys[pygame.K_RIGHT]:
#             if FOLLOW_CAM:
#                 for sprite in self.game.all_sprites:
#                     sprite.rect.x -= PLAYER_SPEED
#             self.x_change += PLAYER_SPEED
#             self.facing = 'right'
#         if keys[pygame.K_UP]:
#             if FOLLOW_CAM:
#                 for sprite in self.game.all_sprites:
#                     sprite.rect.y += PLAYER_SPEED
#             self.y_change -= PLAYER_SPEED
#             self.facing = 'up'
#         if keys[pygame.K_DOWN]:
#             if FOLLOW_CAM:
#                 for sprite in self.game.all_sprites:
#                     sprite.rect.y -= PLAYER_SPEED
#             self.y_change += PLAYER_SPEED
#             self.facing = 'down'
#
#     def collide_blocks(self, direction):
#         if direction == "x":
#             hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
#             if hits:
#                 if self.x_change > 0:  # if moving right
#                     self.rect.x = hits[0].rect.left - self.rect.width
#                     if FOLLOW_CAM:
#                         for sprite in self.game.all_sprites:
#                             sprite.rect.x += PLAYER_SPEED  # dont let the camera move when colliding
#                 if self.x_change < 0:  # if moving left
#                     self.rect.x = hits[0].rect.right
#                     if FOLLOW_CAM:
#                         for sprite in self.game.all_sprites:
#                             sprite.rect.x -= PLAYER_SPEED
#         if direction == "y":
#             hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
#             if hits:
#                 if self.y_change > 0:  # if moving down
#                     self.rect.y = hits[0].rect.top - self.rect.height
#                     if FOLLOW_CAM:
#                         for sprite in self.game.all_sprites:
#                             sprite.rect.y += PLAYER_SPEED
#                 if self.y_change < 0:  # if moving up
#                     self.rect.y = hits[0].rect.bottom
#                     if FOLLOW_CAM:
#                         for sprite in self.game.all_sprites:
#                             sprite.rect.y -= PLAYER_SPEED
#
#     def collide_enemy(self):
#         hits = pygame.sprite.spritecollide(self, self.game.enemies, False)
#         if hits:
#             self.kill()
#             self.game.playing = False
#
#     def animate(self):
#
#         if self.facing == "down":
#             if self.y_change == 0:  # if we are standing still
#                 self.image = self.game.character_spritesheet[self.selected_character].get_sprite(3, 2, self.width, self.height)
#             else:
#                 self.image = self.down_animations[math.floor(self.animation_loop)]
#                 self.animation_loop += 0.1  # go to the next image in the list every 10 loops/frames
#                 if self.animation_loop >= 3:
#                     self.animation_loop = 1
#         if self.facing == "up":
#             if self.y_change == 0:  # if we are standing still
#                 self.image = self.game.character_spritesheet[self.selected_character].get_sprite(3, 98, self.width, self.height)
#             else:
#                 self.image = self.up_animations[math.floor(self.animation_loop)]
#                 self.animation_loop += 0.1
#                 if self.animation_loop >= 3:
#                     self.animation_loop = 1
#         if self.facing == "left":
#             if self.x_change == 0:  # if we are standing still
#                 self.image = self.game.character_spritesheet[self.selected_character].get_sprite(3, 34, self.width, self.height)
#             else:
#                 self.image = self.left_animations[math.floor(self.animation_loop)]
#                 self.animation_loop += 0.1
#                 if self.animation_loop >= 3:
#                     self.animation_loop = 1
#         if self.facing == "right":
#             if self.x_change == 0:  # if we are standing still
#                 self.image = self.game.character_spritesheet[self.selected_character].get_sprite(3, 66, self.width, self.height)
#             else:
#                 self.image = self.right_animations[math.floor(self.animation_loop)]
#                 self.animation_loop += 0.1
#                 if self.animation_loop >= 3:
#                     self.animation_loop = 1


class Enemy(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = ENEMY_LAYER
        self.groups = self.game.all_sprites, self.game.enemies
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = TILE_SIZE
        self.height = TILE_SIZE

        self.x_change = 0
        self.y_change = 0

        self.facing = random.choice(['left', 'right'])
        self.animation_loop = 1
        self.movement_loop = 0
        self.max_travel = random.randint(7, 30)

        self.image = self.game.enemy_spritesheet.get_sprite(3, 2, self.width, self.height)

        self.image.set_colorkey(BLACK)  # removes black from the background of the image

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.movement()
        self.animate()
        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.y_change = 0
        self.x_change = 0

    def movement(self):
        # this makes them walk back and forth
        if self.facing == 'left':
            self.x_change -= ENEMY_SPEED
            self.movement_loop -= 1
            if self.movement_loop <= -self.max_travel:
                self.facing = 'right'
        if self.facing == 'right':
            self.x_change += ENEMY_SPEED
            self.movement_loop += 1
            if self.movement_loop >= self.max_travel:
                self.facing = 'left'

    def animate(self):
        down_animations = [self.game.enemy_spritesheet.get_sprite(3, 2, self.width, self.height),
                           self.game.enemy_spritesheet.get_sprite(35, 2, self.width, self.height),
                           self.game.enemy_spritesheet.get_sprite(68, 2, self.width, self.height)]

        up_animations = [self.game.enemy_spritesheet.get_sprite(3, 34, self.width, self.height),
                         self.game.enemy_spritesheet.get_sprite(35, 34, self.width, self.height),
                         self.game.enemy_spritesheet.get_sprite(68, 34, self.width, self.height)]

        left_animations = [self.game.enemy_spritesheet.get_sprite(3, 98, self.width, self.height),
                           self.game.enemy_spritesheet.get_sprite(35, 98, self.width, self.height),
                           self.game.enemy_spritesheet.get_sprite(68, 98, self.width, self.height)]

        right_animations = [self.game.enemy_spritesheet.get_sprite(3, 66, self.width, self.height),
                            self.game.enemy_spritesheet.get_sprite(35, 66, self.width, self.height),
                            self.game.enemy_spritesheet.get_sprite(68, 66, self.width, self.height)]
        if self.facing == "down":
            if self.y_change == 0:  # if we are standing still
                self.image = self.game.enemy_spritesheet.get_sprite(3, 2, self.width, self.height)
            else:
                self.image = down_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1  # go to the next image in the list every 10 loops/frames
                if self.animation_loop >= 3:
                    self.animation_loop = 1
        if self.facing == "up":
            if self.y_change == 0:  # if we are standing still
                self.image = self.game.enemy_spritesheet.get_sprite(3, 34, self.width, self.height)
            else:
                self.image = up_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1
        if self.facing == "left":
            if self.x_change == 0:  # if we are standing still
                self.image = self.game.enemy_spritesheet.get_sprite(3, 98, self.width, self.height)
            else:
                self.image = left_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1
        if self.facing == "right":
            if self.x_change == 0:  # if we are standing still
                self.image = self.game.enemy_spritesheet.get_sprite(3, 66, self.width, self.height)
            else:
                self.image = right_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1


class Block(pygame.sprite.Sprite):
    def __init__(self, game, x, y, tile_id):
        self.game = game
        self._layer = BLOCK_LAYER
        # add blocks to the all_sprites group and set its group to blocks
        self.groups = self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = TILE_SIZE
        self.height = TILE_SIZE

        match tile_id:
            case "T":
                self.image = self.game.terrain_spritesheet[1].get_sprite(0, 0, self.width*2, self.height*2)
            case '1':
                self.image = self.game.terrain_spritesheet[2].get_sprite(5*self.width, 6*self.height, self.width, self.height)
            case '2':
                self.image = self.game.terrain_spritesheet[2].get_sprite(0, 0, self.width, self.height)
            case '3':
                self.image = self.game.terrain_spritesheet[2].get_sprite(0, 0, self.width, self.height)
            case '4':
                self.image = self.game.terrain_spritesheet[2].get_sprite(0, 0, self.width, self.height)
            case '5':
                self.image = self.game.terrain_spritesheet[2].get_sprite(0, 0, self.width, self.height)
            case '6':
                self.image = self.game.terrain_spritesheet[2].get_sprite(0, 0, self.width, self.height)
            case '7':
                self.image = self.game.terrain_spritesheet[2].get_sprite(0, 0, self.width, self.height)
            case '8':
                self.image = self.game.terrain_spritesheet[2].get_sprite(0, 0, self.width, self.height)
            case _:
                self.image = self.game.terrain_spritesheet[0].get_sprite(960, 448, self.width, self.height)




        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


# class StatusDisplay(pygame.sprite.Sprite):
#     def __init__(self, game, x, y, status):
#         self.font = pygame.font.Font('OpenSans.ttf', 16)
#         self.game = game
#         self._layer = BLOCK_LAYER
#         # add display to the all_sprites group and set its group to blocks
#         self.groups = self.game.all_sprites, self.game.blocks
#         pygame.sprite.Sprite.__init__(self, self.groups)
#
#         self.x = x * TILE_SIZE
#         self.y = y * TILE_SIZE
#         self.width = TILE_SIZE
#         self.height = TILE_SIZE
#
#         self.image = pygame.Surface((100, 100))
#         self.image.fill(BLACK)  # draw the blackness first
#
#         self.text = self.font.render("Health: " + str(status['health']) + "\nWisdom: " + str(status['wisdom']) +
#                                      "\nStress: " + str(status['stress']), True, (255, 255, 255))
#         self.text_rect = self.text.get_rect(x=0, y=0)
#         self.image.blit(self.text, self.text_rect)
#         self.rect = self.image.get_rect()
#         self.rect.x = self.x
#         self.rect.y = self.y


class Ground(pygame.sprite.Sprite):
    def __init__(self, game, x, y, sprite_to_grab):
        self.game = game
        self._layer = GROUND_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = TILE_SIZE
        self.height = TILE_SIZE
        # self.image = self.game.terrain_spritesheet.get_sprite(64, 352, self.width, self.height)
        match sprite_to_grab:
            case '.':
                self.image = self.game.terrain_spritesheet[0].get_sprite(64, 352, self.width, self.height)
            case _:  # default case
                self.image = self.game.terrain_spritesheet[0].get_sprite(64, 352, self.width, self.height)
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


class Button:
    def __init__(self, x, y, width, height, fg, bg, content, fontsize):
        self.font = pygame.font.Font('OpenSans.ttf', fontsize)
        self.content = content

        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.fg = fg
        self.bg = bg

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.bg)
        self.rect = self.image.get_rect()

        self.rect.x = self.x
        self.rect.y = self.y

        self.text = self.font.render(self.content, True, self.fg)
        self.text_rect = self.text.get_rect(center=(self.width / 2, self.height / 2))
        self.image.blit(self.text, self.text_rect)

    def is_pressed(self, pos, pressed):
        # get position of mouse
        if self.rect.collidepoint(pos):  # see if it collides with our button
            if pressed[0]:  # 0 is left mouse click 1 is right and 2 is scroll click
                return True
            return False
        return False

    def is_clicked(self, pos, pressed):
        if self.rect.collidepoint(pos):  # see if it collides with our button
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return True
                return False
        return False

class Attack(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites, self.game.attacks
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x
        self.y = y
        self.width = TILE_SIZE
        self.height = TILE_SIZE

        self.animation_loop = 0

        self.image = self.game.attack_spritesheet.get_sprite(0, 0, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.animate()
        self.collide()

    def collide(self):
        hits = pygame.sprite.spritecollide(self, self.game.enemies, True)

    def animate(self):
        direction = self.game.player.facing
        right_animations = [self.game.attack_spritesheet.get_sprite(0, 64, self.width, self.height),
                            self.game.attack_spritesheet.get_sprite(32, 64, self.width, self.height),
                            self.game.attack_spritesheet.get_sprite(64, 64, self.width, self.height),
                            self.game.attack_spritesheet.get_sprite(96, 64, self.width, self.height),
                            self.game.attack_spritesheet.get_sprite(128, 64, self.width, self.height)]

        down_animations = [self.game.attack_spritesheet.get_sprite(0, 32, self.width, self.height),
                           self.game.attack_spritesheet.get_sprite(32, 32, self.width, self.height),
                           self.game.attack_spritesheet.get_sprite(64, 32, self.width, self.height),
                           self.game.attack_spritesheet.get_sprite(96, 32, self.width, self.height),
                           self.game.attack_spritesheet.get_sprite(128, 32, self.width, self.height)]

        left_animations = [self.game.attack_spritesheet.get_sprite(0, 96, self.width, self.height),
                           self.game.attack_spritesheet.get_sprite(32, 96, self.width, self.height),
                           self.game.attack_spritesheet.get_sprite(64, 96, self.width, self.height),
                           self.game.attack_spritesheet.get_sprite(96, 96, self.width, self.height),
                           self.game.attack_spritesheet.get_sprite(128, 96, self.width, self.height)]

        up_animations = [self.game.attack_spritesheet.get_sprite(0, 0, self.width, self.height),
                         self.game.attack_spritesheet.get_sprite(32, 0, self.width, self.height),
                         self.game.attack_spritesheet.get_sprite(64, 0, self.width, self.height),
                         self.game.attack_spritesheet.get_sprite(96, 0, self.width, self.height),
                         self.game.attack_spritesheet.get_sprite(128, 0, self.width, self.height)]

        if direction == 'up':
            self.image = up_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.5  # chaning the attack image every 2 loops
            if self.animation_loop >= 5:
                self.kill()  # end animation cause we only have 5 frames
        if direction == 'down':
            self.image = down_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.5  # chaning the attack image every 2 loops
            if self.animation_loop >= 5:
                self.kill()  # end animation cause we only have 5 frames
        if direction == 'left':
            self.image = left_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.5  # chaning the attack image every 2 loops
            if self.animation_loop >= 5:
                self.kill()  # end animation cause we only have 5 frames
        if direction == 'right':
            self.image = right_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.5  # chaning the attack image every 2 loops
            if self.animation_loop >= 5:
                self.kill()  # end animation cause we only have 5 frames
