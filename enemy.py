from engine import *

_sprites = SpriteSheet('assets/images/beeto.png', {
    'walk': [(2+28*i, 2, 26, 16) for i in range(4)],
    'flip': (2, 20, 26, 16),
})


class Beeto:
    def __init__(self, rect=None, bounds=None):
        self.flip = False
        self.animation = Animation(
            _sprites.animation_sprites('walk'), 1, repeat=True)
        self.rect = rect
        self.bounds = bounds
        self.vx = 5

    def animate(self):
        self.animation.tick()

    def draw(self, surface, offset=(0, 0)):
        frame = self.animation.frame()
        if self.flip:
            frame = pg_transform.flip(frame, 1, 0)

        surface.blit(frame, (self.rect.x-offset[0], self.rect.y-offset[1]))

    def move(self, tiles):
        self.rect.x += self.vx * dt

        if self.rect.x > self.bounds[1] or self.rect.x < self.bounds[0]:
            self.vx *= -1
            self.flip = not self.flip

    def update(self, tiles):
        self.move(tiles)
        self.animate()
