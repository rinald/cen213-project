from engine import *

from config import FPS

frames = {
    'idle': (2, 2, 34, 32),
    'down_thrust': (2, 223, 24, 36),
    'walk': [(2+42*i, 77, 40, 35) for i in range(5)],
    'jump': (2, 114, 31, 34),
    'fall': (2, 150, 33, 34),
    'slash': [(2+56*i, 186, 54, 35) for i in range(5)],
    'shine': [(2+36*i, 323, 34, 32) for i in range(3)],
}

_sprites = SpriteSheet('assets/images/knight.png', frames)


class Knight:
    def __init__(self, rect=None):
        self.flip = False
        self.grounded = True
        self.falling = False
        self.down_attack = False
        self.animation = None
        self.animations = {
            'walk': Animation(_sprites.animation_sprites('walk'), duration=0.5, repeat=True),
            'slash': Animation(_sprites.animation_sprites('slash'), duration=0.5, repeat=False, flip_offset=(20, 0)),
        }
        self.sprite = _sprites.sprite('idle')
        self.rect = rect
        self.vx = 0
        self.vy = 0
        self.slash_sound = pg_mixer.Sound('assets/sounds/knight_slash.ogg')
        self.jump_sound = pg_mixer.Sound('assets/sounds/knight_jump.ogg')
        self.land_sound = pg_mixer.Sound('assets/sounds/knight_land.ogg')

    def draw(self, surface, offset=(0, 0)):
        pos = [self.rect.x-offset[0], self.rect.y-offset[1]]

        if self.flip == True and self.animation is not None:
            if self.animation.i != 0:
                pos[0] -= self.animation.flip_offset[0]

        surface.blit(self.sprite, pos)

    def set_sprite(self, sprite=None):
        if sprite is None:
            sprite = self.animation.frame()

        if self.flip:
            sprite = pg_transform.flip(sprite, 1, 0)

        self.sprite = sprite

    def collisions(self, tiles):
        hit_list = []

        for tile in tiles:
            if self.rect.colliderect(tile):
                hit_list.append(tile)
        return hit_list

    def animate(self):
        if self.animation is not None:
            self.animation.tick()
            self.set_sprite()

            if self.animation.stopped == True:
                self.animation = None
                self.set_sprite(_sprites.sprite('idle'))

    def set_animation(self, animation_id):
        self.animation = self.animations[animation_id]
        self.animation.reset()

    def on_event(self, event):
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                self.flip = True
                self.vx = -10
                if self.grounded:
                    self.set_animation('walk')
            if event.key == K_RIGHT:
                self.flip = False
                self.vx = 10
                if self.grounded:
                    self.set_animation('walk')
            if event.key == K_UP:
                if self.grounded:
                    self.jump_sound.play()
                    self.vy = -40
                    self.grounded = False
                    self.animation = None
                    self.set_sprite(_sprites.sprite('jump'))
            if event.key == K_DOWN:
                if not self.grounded:
                    self.down_attack = True
                    self.set_sprite(_sprites.sprite('down_thrust'))
            if event.key == K_SPACE:
                self.slash_sound.play()
                self.set_animation('slash')
        if event.type == KEYUP:
            if event.key in (K_LEFT, K_RIGHT):
                self.animation = None
                self.vx = 0
                if self.grounded:
                    self.set_sprite(_sprites.sprite('idle'))

    def move(self, tiles):
        collisions = {'left': False, 'right': False,
                      'top': False, 'bottom': False}

        if self.vx != 0:
            self.rect.x += self.vx*dt
            hit_list = self.collisions(tiles)

            for tile in hit_list:
                if self.vx > 0:
                    self.rect.right = tile.left
                    collisions['right'] = True
                elif self.vx < 0:
                    self.rect.left = tile.right
                    collisions['left'] = True

        if not self.grounded:
            self.rect.y += self.vy*dt
            self.vy += 0.5*g*dt**2

            hit_list = self.collisions(tiles)

            for tile in hit_list:
                if self.vy > 0:
                    self.rect.bottom = tile.top
                    collisions['bottom'] = True
                elif self.vy < 0:
                    self.rect.top = tile.bottom
                    collisions['top'] = True

            if not self.falling and self.vy > 0:
                if not self.down_attack:
                    self.set_sprite(_sprites.sprite('fall'))
                self.falling = True

        if collisions['bottom'] == True:
            self.vy = 0
            self.land_sound.play()
            self.grounded = True
            self.falling = False
            self.down_attack = False
            self.set_sprite(_sprites.sprite('idle'))

        if collisions['top'] == True:
            self.vy = 0
        if collisions['left'] or collisions['right']:
            self.vx = 0
        print(self.grounded)

    def update(self, tiles):
        self.move(tiles)
        self.animate()
