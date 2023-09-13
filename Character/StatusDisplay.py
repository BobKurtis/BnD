import pygame

from values.config import *
import math
import random


class StatusDisplay(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
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

        self.image = pygame.Surface((WIN_WIDTH, 100))
        self.image.fill(BLACK)  # draw the blackness first
        self.mask = pygame.mask.from_surface(self.image)

        self.text = self.font.render(self.game.status_screen_text, True, (255, 255, 255))
        self.text_rect = self.text.get_rect(x=0, y=0)
        self.image.blit(self.text, self.text_rect)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.image.fill(BLACK)  # draw the blackness first
        self.text = self.font.render(self.game.status_screen_text, True, (255, 255, 255))
        self.text_rect = self.text.get_rect(x=0, y=0)
        self.image.blit(self.text, self.text_rect)

        #another chunk of text to display on status screen
        self.text_2 = self.font.render("Remaining Travel Distance: "+str(math.floor(self.game.active_player.max_travel -
                                                                                    self.game.active_player.distance_travelled)), True, (255, 255, 255))

        self.text_rect_2 = self.text_2.get_rect(x=100, y=0)
        self.image.blit(self.text_2, self.text_rect_2)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.mask = pygame.mask.from_surface(self.image)
