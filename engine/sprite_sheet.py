from . import pg_image


class SpriteSheet:
    def __init__(self, image_path, tiles):
        self.image = pg_image.load(image_path)
        self.tiles = tiles

    def tile(self, tile_id):
        return self.image.subsurface(self.tiles[tile_id])
