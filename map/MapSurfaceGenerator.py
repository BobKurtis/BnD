import json

import pygame
import SpriteSheet
import map.maps.FirstWorld


class MapSurfaceGenerator:
    def __init__(self):
        # size multiplier so we can pick sprites as numbers
        self.spriteHeight = 32
        self.spriteWidth = 32

    def generate(self, map_file, sprite_file):
        # get the map file in coords
        self.map.coords = json.loads(map.maps.FirstWorld.map_cords)
