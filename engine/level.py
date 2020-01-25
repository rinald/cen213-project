from engine import pg, Surface


class Level:
    def __init__(self, data_file, tiles):
        self.map = Surface((50*16, 15*16), pg.SRCALPHA)

        with open(data_file) as file:
            self.array = file.read().split('\n')

        self.tiles = tiles
        self.build_map()

    def build_map(self):
        for i in range(15):
            for j in range(50):
                k = int(self.array[i][j])

                if k != 0:
                    self.map.blit(self.tiles[k-1], (j*16, i*16))
