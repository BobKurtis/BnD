import pygame

import values.constants
# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards

from values import constants


# Define a player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Status(pygame.sprite.Sprite):

    def __init__(self):
        super(Status, self).__init__()

        self.font = pygame.font.SysFont(None, 80)
        self.text_surf = self.font.render('', True, (255, 255, 255))

        self.surf = pygame.Surface((200, 400))
        self.surf.fill((0, 0, 0))
        self.surf.blit(self.text_surf, self.text_surf.get_rect(center=self.surf.get_rect().center))
        self.rect = self.surf.get_rect()
        self.rect.right = values.constants.SCREEN_WIDTH
        self.rect.top = 0

    def update(self, stats):
        self.text_surf = self.font.render("Health: " + str(stats['health']) + "\n"
                                          "Wisdom: " + str(stats['wisdom']) + "\n"
                                          "Stress: " + str(stats['stress']) + "\n", True, (255, 255, 255))
        self.surf = pygame.Surface((400, 400))
        self.surf.fill((0, 0, 0))
        # center the text
        self.surf.blit(self.text_surf, self.text_surf.get_rect(center=self.surf.get_rect().center))
        # set size of status screen
        self.rect = self.surf.get_rect(width=400, height=400)
        # set status screen position
        self.rect.right = constants.SCREEN_WIDTH
        self.rect.top = 0
