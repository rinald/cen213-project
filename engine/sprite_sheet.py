from . import pg_image, pg_transform


class SpriteSheet:
    def __init__(self, image_path, tiles):
        self.image = pg_image.load(image_path)
        self.tiles = tiles

    def tile(self, tile_id, size=(32, 32)):
        image = self.image.subsurface(self.tiles[tile_id])

        # if flip:
        #     image = pg_transform.flip(image, 1, 0)
        image = pg_transform.scale(image, size)

        return image

    def animation_tiles(self, tile_id, size=(32, 32)):
        images = []
        for rect in self.tiles[tile_id]:
            image = self.image.subsurface(rect)

            # if flip:
            #     image = pg_transform.flip(image, 1, 0)
            image = pg_transform.scale(image, size)

            images.append(image)

        return images
