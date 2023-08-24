import json

import pygame
import map.SpriteSheet as SpriteSheet
import map.maps.FirstWorld
import values

# size multiplier so we can pick sprites as numbers
spriteHeight = 32
spriteWidth = 32


class MapSurfaceGenerator(pygame.sprite.Sprite):

    def __init__(self):
        super(MapSurfaceGenerator, self).__init__()
        self.surf = pygame.Surface((200, 400))
        # self.surf.fill((0, 0, 0))
        # self.surf.blit(self.text_surf, self.text_surf.get_rect(center=self.surf.get_rect().center))
        self.rect = self.surf.get_rect()
        self.rect.right = values.constants.SCREEN_WIDTH / 2
        self.rect.top = 0
        self.generate(self, 1, './images/tilesets/1.png')

    def generate(self, map_file, sprite_file):
        map_sheet = SpriteSheet.SpriteSheet(sprite_file)
        if map_file == 1:
            # use firstWorld
            map_file = map.maps.FirstWorld
        # create a sheet to store everything

        # get the map file in coords
        map.coords = map_file.map_cords
        # build a line at a time
        for entry in map.coords:
            # cycle through each entry and get each set of sprites
            for index, coord in enumerate(entry):
                # get the sprite
                # loaded_image = SpriteSheet.SpriteSheet.image_at((0, 0, coord + spriteWidth,
                #                                                 coord + spriteHeight), None)
                rect = pygame.Rect
                loaded_image_as_a_surface = SpriteSheet.SpriteSheet.image_at(self, (rect(0, 0, (coord + spriteWidth),
                                                                         (coord + spriteHeight))), None)
                # self.surf.fill((255,0,255))
                # x y offset on where to draw the image we just loaded
                self.surf.blit(loaded_image_as_a_surface, (500, 500))
                self.rect = self.surf.get_rect()

                return self.surf
