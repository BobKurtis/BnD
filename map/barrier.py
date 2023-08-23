import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_h,
    K_m,
    K_w,
    RLEACCEL
)


class Barrier(pygame.sprite.Sprite):
    def __init__(self):
        super(Barrier, self).__init__()
        self.surf = pygame.image.load("images/missile.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        # The starting position is randomly generated, as is the speed
        self.rect = self.surf.get_rect(
            center=(
                200, 20
            )
        )

