from engine import pg, Surface, SpriteSheet, Rect
import os

path = os.path.dirname(__file__)
path = os.path.join(path, '../assets/images/plains.png')

sprites = SpriteSheet(path, {
    'bg': (0, 20, 150, 90),
    'g0': (144, 224, 16, 16),
    'g1': (160, 224, 16, 16),
    'g2': (192, 224, 16, 16),
    'g3': (96, 224, 16, 16),
    'g4': (304, 240, 16, 16),
    'g5': (368, 240, 16, 16),
    'g6': (352, 176, 16, 16),
    'ld': (80, 224, 16, 16),
    'sp': (352, 240, 16, 16),
})

sprite_mapping = {
    '[': sprites.sprite('g0'),
    '=': sprites.sprite('g1'),
    ']': sprites.sprite('g2'),
    '|': sprites.sprite('g3'),
    '.': sprites.sprite('g6'),
    'M': sprites.sprite('sp'),
    'H': sprites.sprite('ld'),
}


class Level:
    def __init__(self, data):
        self.map = Surface((50*16, 15*16), pg.SRCALPHA)
        self.tiles = []

        with open(data) as file:
            self.array = file.read().split('\n')

        self.build_map()

    def build_map(self):
        for i in range(15):
            for j in range(50):
                k = self.array[i][j]

                if k != ' ':
                    self.map.blit(sprite_mapping[k], (j*16, i*16))
                    self.tiles.append(Rect(j*16, i*16, 16, 16))
