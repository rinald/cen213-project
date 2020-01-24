from engine import *

enemy_sprites = SpriteSheet('assets/images/beeto.png', tiles={
    'walk': [(2+28*i, 2, 26, 16) for i in range(4)],
    'flip': (2, 20, 26, 16),
})

scale = (2, 2)
vx = 10

dt = 0.2


class Enemy:
    def __init__(self, pos=None):
        self.flip = False
        self.animation = Animation(
            enemy_sprites.animation_tiles('walk', size=(52, 32)), 1, repeat=True)
        self.pos = pos
        self.vx = vx

    def animate(self):
        self.animation.tick()

    def draw(self, surface):
        frame = self.animation.frame()
        if self.flip:
            frame = pg_transform.flip(frame, 1, 0)

        surface.blit(frame, self.pos)

    def move(self):
        self.pos[0] += self.vx * dt

        if self.pos[0] > 640 - 52 or self.pos[0] < 0:
            self.vx *= -1
            self.flip = not self.flip
