from engine import *

_sprites = SpriteSheet('assets/images/beeto.png', {
    'walk': [(2+28*i, 2, 26, 16) for i in range(4)],
    'flip': (2, 20, 26, 16),
})


class Beeto:
    def __init__(self, pos=None):
        self.flip = False
        self.animation = Animation(
            _sprites.animation_tiles('walk'), 1, repeat=True)
        self.pos = pos
        self.vx = 2

    def animate(self):
        self.animation.tick()

    def draw(self, surface, offset=(0, 0)):
        frame = self.animation.frame()
        if self.flip:
            frame = pg_transform.flip(frame, 1, 0)

        surface.blit(frame, (self.pos[0]-offset[0], self.pos[1]-offset[1]))

    def move(self):
        self.pos[0] += self.vx * dt

        if self.pos[0] > 25*16-26 or self.pos[0] < 0:
            self.vx *= -1
            self.flip = not self.flip
