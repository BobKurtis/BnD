import math
import numpy
import pygame
import sprites
from Character.StatusDisplay import StatusDisplay
from values.config import *


class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y, player):
        self.game = game
        self._layer = PLAYER_LAYER
        # add in the player to the all sprites group
        self.groups = self.game.all_sprites
        # call the init method of inherited class
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = TILE_SIZE
        self.height = TILE_SIZE

        self.x_change = 0
        self.y_change = 0
        self.is_active_player = False
        self.distance_travelled = 0

        self.facing = 'down'
        self.health = player.get('health')
        self.wisdom = player.get('wisdom')
        self.stress = player.get('stress')
        self.speed = player.get('speed')
        self.attack_range = player.get('attackRange')
        self.max_travel = ((self.speed*TILE_SIZE)/2)
        self.selected_character = player
        self.selected_character_spritesheet = (sprites.Spritesheet(self.selected_character.get('sprite_file')))

        # draw stats
        # StatusDisplay(40, 10, 100, 30, self.game, self)
        self.animation_loop = 1

        # image_to_load = pygame.image.load("img/d20.png")

        # set surface as player's image or what it looks like
        # self.image = pygame.Surface([self.width, self.height])
        # self.image = self.game.character_spritesheet.get_sprite(3, 2, self.width, self.height)
        # self.image = self.game.character_spritesheet[self.selected_character.get('sprite_file')].get_sprite(3, 2, self.width, self.height)
        self.image = self.selected_character_spritesheet.get_sprite(3, 2, self.width, self.height)
        self.image_facing_down = self.image
        self.image_facing_up = self.selected_character_spritesheet.get_sprite(3, 98, self.width, self.height)
        self.image_facing_left = self.selected_character_spritesheet.get_sprite(3, 34, self.width, self.height)
        self.image_facing_right = self.selected_character_spritesheet.get_sprite(3, 66, self.width, self.height)
        # self.image.fill(RED) instead of filling with red we are going to place an image
        # select image and where to draw it on the surface
        # self.image.blit(image_to_load, (0, 0))
        self.image.set_colorkey(BLACK)
        # rect is where its positioned and size like a hitbox
        self.rect = self.image.get_rect()  # setting hitbox to same size as image
        # tell pygame the coords of our rectangle
        self.rect.x = self.x
        self.rect.y = self.y
        self.beginning_location = (self.rect.x, self.rect.y)
        # set up mask for pixel perfect collision detection
        self.mask = pygame.mask.from_surface(self.image)
        # self.mask = pygame.mask.from_surface(self.image)
        # mask -> surface
        # self.image = self.mask.to_surface()

        # self.mask_size = self.mask.get_size()
        # set our animations
        self.down_animations = [
            self.selected_character_spritesheet.get_sprite(0, 0, self.width, self.height),
            self.selected_character_spritesheet.get_sprite(32, 0, self.width, self.height),
            self.selected_character_spritesheet.get_sprite(64, 0, self.width, self.height)]

        self.left_animations = [
            self.selected_character_spritesheet.get_sprite(0, 32, self.width, self.height),
            self.selected_character_spritesheet.get_sprite(32, 32, self.width, self.height),
            self.selected_character_spritesheet.get_sprite(64, 32, self.width, self.height)]

        self.right_animations = [
            self.selected_character_spritesheet.get_sprite(0, 64, self.width, self.height),
            self.selected_character_spritesheet.get_sprite(32, 64, self.width, self.height),
            self.selected_character_spritesheet.get_sprite(64, 64, self.width, self.height)]

        self.up_animations = [
            self.selected_character_spritesheet.get_sprite(0, 96, self.width, self.height),
            self.selected_character_spritesheet.get_sprite(32, 96, self.width, self.height),
            self.selected_character_spritesheet.get_sprite(64, 96, self.width, self.height)]

        self.status = {'health': self.health, 'wisdom': self.wisdom, 'stress': self.stress, 'speed': 50}
        # StatusDisplay(self.game, 10, 5)
        # pass game, x y coords and the status to apply

    def update(self):
        # don't do any updates if not the active player
        if self.is_active_player:
            # StatusDisplay(self.game, 10, 5, self.status)
            self.movement()
            # validate movement before animations

            self.collide_enemy()
            self.collide_block_bool()
            self.rect.x += self.x_change
            # check for collision along x-axis
            # self.collide_blocks('x')
            self.rect.y += self.y_change

            # pygame.draw.ellipse(self.image, BLUE, self.rect, width=15)
            # calculate distance travelled

            self.distance_travelled = math.dist(self.beginning_location, (self.rect.x, self.rect.y))

            if self.distance_travelled > self.max_travel:
                # we've walked the max amount so undo the changes
                while (self.max_travel - self.distance_travelled) < 0:
                    self.rect.x -= numpy.sign(self.x_change)*1
                    self.rect.y -= numpy.sign(self.y_change)*1
                    self.distance_travelled = math.dist(self.beginning_location, (self.rect.x, self.rect.y))
                    print(f"Distance travelled: {self.distance_travelled}")



            # check for collision along y-axis
            # self.collide_blocks('y')
            self.animate()
            # self.mask = pygame.mask.from_surface(self.image)
            # self.image = self.mask.to_surface(unsetcolor=BLUE, setcolor=BLACK)
            self.x_change = 0
            self.y_change = 0

    def movement(self):
        keys = pygame.key.get_pressed()
        # limit travel based on speed
        if keys[pygame.K_LEFT]:
            # simulate camera by keeping player in the middle
            if FOLLOW_CAM:
                for sprite in self.game.all_sprites:
                    sprite.rect.x += PLAYER_SPEED
            self.x_change -= PLAYER_SPEED
            self.facing = 'left'
        if keys[pygame.K_RIGHT]:
            if FOLLOW_CAM:
                for sprite in self.game.all_sprites:
                    sprite.rect.x -= PLAYER_SPEED
            self.x_change += PLAYER_SPEED
            self.facing = 'right'
        if keys[pygame.K_UP]:
            if FOLLOW_CAM:
                for sprite in self.game.all_sprites:
                    sprite.rect.y += PLAYER_SPEED
            self.y_change -= PLAYER_SPEED
            self.facing = 'up'
        if keys[pygame.K_DOWN]:
            if FOLLOW_CAM:
                for sprite in self.game.all_sprites:
                    sprite.rect.y -= PLAYER_SPEED
            self.y_change += PLAYER_SPEED
            self.facing = 'down'

    def collide_block_bool(self):
        hits = pygame.sprite.spritecollide(self, self.game.blocks, False, pygame.sprite.collide_mask)
        if hits:
            for idx, x in enumerate(hits):
                offset_x = hits[idx].rect.x - self.rect.x
                offset_y = hits[idx].rect.y - self.rect.y
                dx = self.mask.overlap_area(hits[idx].mask, (offset_x + 1, offset_y)) - self.mask.overlap_area(hits[idx].mask, (offset_x - 1, offset_y))
                dy = self.mask.overlap_area(hits[idx].mask, (offset_x, offset_y + 1)) - self.mask.overlap_area(hits[idx].mask, (offset_x, offset_y - 1))

                print(f"Dx:{dx} and Dy:{dy}")

                if dx < 0:
                    # jitter to the left
                    print("Jitter left")
                    self.x_change -= 1  # maybe jitter the x offset?
                if dx > 0:
                    # jitter to the right
                    print("Jitter right")
                    self.x_change += 1
                if dy < 0:
                    # jitter up
                    print("Jitter up")
                    self.y_change -= 1
                if dy > 0:
                    # jitter down
                    print("Jitter down")
                    self.y_change += 1


    def collide_blocks(self, direction):
        if direction == "x":
            # if self.mask.overlap(self.game.blocks, (0, 0)):
            #     print("Masks collide")
            # do retangle collision first to save memeory
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False, pygame.sprite.collide_mask)
            if hits:
                # now see if the masks intersect and where

                try:
                    self.overlap_x, self.overlap_y = hits[0].mask.overlap(self.mask, (0, 0))
                    # print(self.overlap_x+", "+self.overlap_y)
                    # (self.overlap_x, self.overlap_y) = self.mask.overlap(hits[0].mask, (0, 0))
                    if self.x_change > 0:  # if moving right
                        self.rect.x = hits[0].rect.left - hits[0].mask.x
                        if FOLLOW_CAM:
                            for sprite in self.game.all_sprites:
                                sprite.rect.x += PLAYER_SPEED  # don't let the camera move when colliding
                    if self.x_change < 0:  # if moving left
                        self.rect.x = hits[0].rect.right + 15
                        if FOLLOW_CAM:
                            for sprite in self.game.all_sprites:
                                sprite.rect.x -= PLAYER_SPEED
                except Exception:
                    pass

        if direction == "y":
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False, pygame.sprite.collide_mask)
            if hits:
                if self.y_change > 0:  # if moving down
                    self.rect.y = hits[0].rect.top - self.rect.height
                    if FOLLOW_CAM:
                        for sprite in self.game.all_sprites:
                            sprite.rect.y += PLAYER_SPEED
                if self.y_change < 0:  # if moving up
                    self.rect.y = hits[0].rect.bottom
                    if FOLLOW_CAM:
                        for sprite in self.game.all_sprites:
                            sprite.rect.y -= PLAYER_SPEED

    def collide_enemy(self):
        hits = pygame.sprite.spritecollide(self, self.game.enemies, False)
        if hits:
            self.kill()
            self.game.playing = False

    def animate(self):

        if self.facing == "down":
            if self.y_change == 0:  # if we are standing still
                self.image = self.image_facing_down
            else:
                self.image = self.down_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1  # go to the next image in the list every 10 loops/frames
                if self.animation_loop >= 3:
                    self.animation_loop = 1
                    self.check_distance = True
        if self.facing == "up":
            if self.y_change == 0:  # if we are standing still
                self.image = self.image_facing_up
            else:
                self.image = self.up_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1
                    self.check_distance = True

        if self.facing == "left":
            if self.x_change == 0:  # if we are standing still
                self.image = self.image_facing_left
            else:
                self.image = self.left_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1
                    self.check_distance = True

        if self.facing == "right":
            if self.x_change == 0:  # if we are standing still
                self.image = self.image_facing_right
            else:
                self.image = self.right_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1
                    self.check_distance = True

        # self.mask = pygame.mask.from_surface(self.image)
        # self.image = self.mask.to_surface()


# structure to represent a co-ordinate
# point


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Function to print pair of points at
# distance 'l' and having a slope 'm'
# from the source


def print_points(source, l, m):
    # m is the slope of line, and the
    # required Point lies distance l
    # away from the source Point
    a = Point(0, 0)
    b = Point(0, 0)

    # slope is 0
    if m == 0:
        a.x = source.x + l
        a.y = source.y

        b.x = source.x - l
        b.y = source.y

    # if slope is infinite
    elif math.isfinite(m) is False:
        a.x = source.x
        a.y = source.y + l

        b.x = source.x
        b.y = source.y - l
    else:
        dx = (l / math.sqrt(1 + (m * m)))
        dy = m * dx
        a.x = source.x + dx
        a.y = source.y + dy
        b.x = source.x - dx
        b.y = source.y - dy

    # print the first Point positive distance
    print(f"{a.x}, {a.y}")

    # print the second Point negative distance
    print(f"{b.x}, {b.y}")
    # may dictionary of points
    d = dict()
    d['neg'] = b
    d['pos'] = a
    return d
