import pygame as pg
from pygame.locals import *


frames = {
    'idle': (2, 2, 34, 32),
    'downward_thrust': (2, 223, 24, 36),
    'walk': [(2+42*i, 77, 40, 35) for i in range(5)],
    'jump': (2, 114, 31, 34),
    'fall': (2, 150, 33, 34),
    'dig': [(2+56*i, 186, 54, 35) for i in range(5)],
}

scale = (2, 2)
speed = 4


class Player:
    def __init__(self, sprite_sheet=None, rect=None, scale=None, pos=None, spf=2):
        self.anim = False
        self.animation = ''
        self.spf = spf
        self.i = 0
        self.j = 0
        self.right = True
        self.dx, self.dy = 0, 0
        self.sprites = pg.image.load(sprite_sheet)
        self.pos = pos
        self.set_sprite(rect=rect, scale=scale)

    def set_sprite(self, rect=None, scale=None):
        self.rect = rect
        self.scale = scale
        w, h = rect[2], rect[3]
        image = self.sprites.subsurface(rect)
        self.image = pg.transform.scale(image, (w*scale[0], h*scale[1]))
        if not self.right:
            self.image = pg.transform.flip(self.image, 1, 0)

    def draw(self, surface):
        surface.blit(self.image, self.pos)

    def update(self, event):
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                self.right = False
                self.anim = True
                self.animation = 'walk'
                self.dx, self.dy = -speed, 0
                # self.image = pg.transform.flip(self.image, 1, 0)
            elif event.key == K_RIGHT:
                self.right = True
                self.anim = True
                self.animation = 'walk'
                self.dx, self.dy = speed, 0
            elif event.key == K_DOWN:
                self.anim = False
                self.set_sprite(rect=frames['downward_thrust'], scale=scale)
            elif event.key == K_SPACE:
                self.anim = True
                self.animation = 'dig'
        if event.type == KEYUP:
            self.anim = False
            self.j = 0
            self.i = 0
            self.dx, self.dy = 0, 0
            self.set_sprite(rect=frames['idle'], scale=scale)

    def animate(self):
        if self.anim:
            self.j %= 60 / self.spf / 2
            self.i %= 5

            if self.j == 0:
                self.set_sprite(
                    rect=frames[self.animation][self.i], scale=scale)
                self.i += 1
            self.j += 1

    def move(self):
        if self.pos[0] < 0:
            self.pos[0] = 0

        self.pos[0] += self.dx

        if self.pos[0] > 640-64:
            self.pos[0] = 640-64

        self.pos[1] += self.dy
