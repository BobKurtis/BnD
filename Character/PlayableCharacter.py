import pygame

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_h,
    K_m,
    K_w
)

import StatsDisplay
import values.PlayerOne
from values import constants

DEFAULT_IMAGE_SIZE = (100, 100)


# Define a player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):

    def __init__(self, stats_to_apply):

        super(Player, self).__init__()

        # load image onto a surface (aka what I'm drawing)
        self.surf = pygame.image.load("images/d20.png").convert_alpha()

        # scale the surface to our "default" size
        self.surf = pygame.transform.scale(self.surf, DEFAULT_IMAGE_SIZE)

        # get bounding rectangle (aka where I'm drawing it)
        self.rect = self.surf.get_rect()

        # self.move_up_sound = pygame.mixer.Sound("music/Rising_putter.ogg")
        # self.move_down_sound = pygame.mixer.Sound("music/Falling_putter.ogg")
        self.status = {'health': stats_to_apply[0], 'wisdom': stats_to_apply[1], 'stress': stats_to_apply[2]}

        # init status display to show player stats
        self.status_display = StatsDisplay.Status()

    # Move the sprite based on user keypresses
    def update(self, pressed_keys):
        if pressed_keys[K_UP] and pressed_keys[K_m]:
            self.rect.move_ip(0, -5)
            # self.move_up_sound.play()
        if pressed_keys[K_DOWN] and pressed_keys[K_m]:
            self.rect.move_ip(0, 5)
            # self.move_down_sound.play()
        if pressed_keys[K_LEFT] and pressed_keys[K_m]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT] and pressed_keys[K_m]:
            self.rect.move_ip(5, 0)
        # health adjustments
        if pressed_keys[K_h] and pressed_keys[K_DOWN]:
            self.status['health'] = self.status.get('health') - 1
            self.status_display.update(self.status)
            # wait so that the numbers don't go super fast
            pygame.time.wait(values.constants.ADJUSTMENT_CYCLE_IN_MILLIS)
        if pressed_keys[K_h] and pressed_keys[K_UP]:
            self.status['health'] = self.status.get('health') + 1
            self.status_display.update(self.status)
            pygame.time.wait(values.constants.ADJUSTMENT_CYCLE_IN_MILLIS)
        # wisdom adjustments
        if pressed_keys[K_w] and pressed_keys[K_DOWN]:
            self.status['wisdom'] = self.status.get('wisdom') - 1
            self.status_display.update(self.status)
            pygame.time.wait(values.constants.ADJUSTMENT_CYCLE_IN_MILLIS)
        if pressed_keys[K_w] and pressed_keys[K_UP]:
            self.status['wisdom'] = self.status.get('wisdom') + 1
            self.status_display.update(self.status)
            pygame.time.wait(values.constants.ADJUSTMENT_CYCLE_IN_MILLIS)

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > constants.SCREEN_WIDTH:
            self.rect.right = constants.SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= constants.SCREEN_HEIGHT:
            self.rect.bottom = constants.SCREEN_HEIGHT

    def get_status(self):
        return self.status
