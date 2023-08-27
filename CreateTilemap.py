from sprites import Ground, Block, Enemy
from values.config import *


class CreateTileMap:

    def createTilemap(self):
        for i, row in enumerate(tilemap):
            for j, column in enumerate(row):
                Ground(self, j, i, column)

                if column in ["B", "1", "2", "3", "4", "5", "6", "7", "8"]:
                    Block(self, j, i, column)
                if column == "T":
                    Block(self, j, i, column)
                if column == "E":
                    Enemy(self, j, i)
