from engine import *

FPS = 60

frames = {
    'idle': (2, 2, 34, 32),
    'downward_thrust': (2, 223, 24, 36),
    'walk': [(2+42*i, 77, 40, 35) for i in range(5)],
    'jump': (2, 114, 31, 34),
    'fall': (2, 150, 33, 34),
    'dig': [(2+56*i, 186, 54, 35) for i in range(5)],
    'shine': [(2+36*i, 323, 34, 32) for i in range(3)]
}

scale = (2, 2)
vx = 20

dt = 0.2
g = 60


class Player:
    def __init__(self, sprite_sheet=None, rect=None, scale=None, pos=None, spf=2):
        self.animating = False
        self.animation = None
        self.grounded = True
        self.animations = {
            'walk': Animation(frames['walk'], 0.8, repeat=True),
            'dig': Animation(frames['dig'], 0.8),
            'shine': Animation(frames['shine'], 0.5),
        }
        self.right = True
        self.vx, self.vy = 0, 0
        self.sprites = pg.image.load(sprite_sheet)
        self.pos = pos
        self.set_sprite(rect=rect, scale=scale)

    def set_sprite(self, rect=None, scale=None):
        self.rect = rect
        self.scale = scale
        w, h = rect[2], rect[3]
        image = self.sprites.subsurface(rect)
        self.image = pg_transform.scale(image, (w*scale[0], h*scale[1]))
        if not self.right:
            self.image = pg_transform.flip(self.image, 1, 0)

    def draw(self, surface):
        surface.blit(self.image, self.pos)

    def on_event(self, event):
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                self.pos[1] -= 4
                self.right = False
                if self.grounded:
                    self.animating = True
                    self.animation = self.animations['walk']
                self.vx = -vx
            elif event.key == K_RIGHT:
                self.pos[1] -= 4
                self.right = True
                if self.grounded:
                    self.animating = True
                    self.animation = self.animations['walk']
                self.vx = vx
            elif event.key == K_DOWN:
                self.animating = False
                if not self.grounded:
                    self.set_sprite(
                        rect=frames['downward_thrust'], scale=scale)
            elif event.key == K_UP:
                if self.grounded:
                    self.vy = -35

                self.animating = False
                self.grounded = False
                self.set_sprite(rect=frames['jump'], scale=scale)

            elif event.key == K_SPACE:
                self.animating = True
                self.animation = self.animations['dig']
            elif event.key == K_f:
                self.animating = True
                self.animation = self.animations['shine']
        if event.type == KEYUP:
            if event.key == K_LEFT or event.key == K_RIGHT:
                self.pos[1] += 4
                self.vx = 0
            if event.key != K_f:
                self.animating = False
            if self.animating:
                self.animation.reset()
            if event.key != K_UP and event.key != K_DOWN:
                self.set_sprite(rect=frames['idle'], scale=scale)

    def animate(self):
        if self.animating:
            self.animation.tick()
            self.set_sprite(rect=self.animation.frame(), scale=scale)

            if self.animation.i == 0 and self.animation.repeat == False:
                self.set_sprite(rect=frames['idle'], scale=scale)
                self.animating = False
                self.animation.reset()

    def move(self):
        if self.pos[0] < 0:
            self.pos[0] = 0

        self.pos[0] += self.vx*dt

        if self.pos[0] > 640-64:
            self.pos[0] = 640-64

        self.pos[1] += self.vy*dt

        if self.pos[1] > 415-29:
            self.pos[1] = 415-29
            self.vy = 0
            self.grounded = True
            self.set_sprite(frames['idle'], scale=scale)

        if not self.grounded:
            self.vy += 0.5*g*dt**2
