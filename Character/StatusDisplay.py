import pygame

from values.config import *
import math
import random


class StatusDisplay(pygame.sprite.Sprite):
    def __init__(self, game, x, y, status):
        self.font = pygame.font.Font('OpenSans.ttf', 16)
        self.game = game
        self._layer = BLOCK_LAYER
        # add display to the all_sprites group and set its group to blocks
        self.groups = self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = TILE_SIZE
        self.height = TILE_SIZE

        self.image = pygame.Surface((100, 100))
        self.image.fill(BLACK)  # draw the blackness first

        self.text = self.font.render("Health: " + str(status['health']) + "\nWisdom: " + str(status['wisdom']) +
                                     "\nStress: " + str(status['stress']), True, (255, 255, 255))
        self.text_rect = self.text.get_rect(x=0, y=0)
        self.image.blit(self.text, self.text_rect)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
