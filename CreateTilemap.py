from sprites import Ground, Block, Enemy
from values.config import *


class CreateTileMap:

    def createTilemap(self):
        for i, row in enumerate(intmap):
            for j, column in enumerate(row):
                # always place a ground so that nothing is ever floating
                Ground(self, j, i, column)
                if column in [1, 31, 32, 33, 34, 13, 14, 15, 16, 17, 18, 19, 20, 21]:
                    Block(self, j, i, column)
                if column == "T":
                    Block(self, j, i, column)
                if column == "E":
                    Enemy(self, j, i)
