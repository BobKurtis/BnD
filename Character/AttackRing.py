import pygame

from values.config import *
import math
import random


class AttackRing(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.font = pygame.font.Font('OpenSans.ttf', 16)
        self.game = game
        self._layer = PLAYER_LAYER
        # add display to the all_sprites group and set its group to blocks
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = TILE_SIZE
        self.height = TILE_SIZE

        self.image = pygame.Surface((32, 32), pygame.SRCALPHA)
        self.mask = pygame.mask.from_surface(self.image)
        pygame.draw.circle(self.image, (255, 0, 0, 255), (16, 16), 10, 1)

        self.rect = self.image.get_rect()
        self.rect.x = self.game.active_player.x
        self.rect.y = self.game.active_player.y

    def update(self):

        width = (self.game.active_player.attack_range * (TILE_SIZE/5))  # a tile is 5 feet
        self.image = pygame.Surface((width, width), pygame.SRCALPHA)

        print(f"Active x: {self.game.active_player.rect.x} y: {self.game.active_player.rect.y} and width: {width}")
        pygame.draw.circle(self.image, (255, 0, 0, 255), (width/2, width/2), width/2, 2)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()

        self.rect.center = self.game.active_player.rect.center

