from config import *
from engine import *

from camera import Camera
from enemy import Beeto
from player import Knight

HALF_WINDOW_SIZE = tuple((i//2 for i in WINDOW_SIZE))

sprite_sheet = SpriteSheet('assets/images/plains.png', {
    'background': (0, 20, 150, 90),
    'ground0': (144, 224, 16, 16),
    'ground1': (160, 224, 16, 16),
    'ground2': (192, 224, 16, 16),
    'ground3': (96, 224, 16, 16),
    'ground4': (304, 240, 16, 16),
    'ground5': (368, 240, 16, 16),
    'ground6': (352, 176, 16, 16),
    'ladder': (80, 224, 16, 16),
    'spikes': (352, 240, 16, 16),
})


class ShovelKnight(Game):
    def init(self):
        self.knight = Knight(pos=[16, 240-63])
        self.beeto = Beeto(pos=[12*16, 240-47])

        self.level = Level('assets/levels/level_1.txt', [
            sprite_sheet.tile('ground0'),  # left
            sprite_sheet.tile('ground1'),  # middle
            sprite_sheet.tile('ground2'),  # right
            sprite_sheet.tile('ground3'),  # down
            sprite_sheet.tile('ground6'),  # blank
            sprite_sheet.tile('spikes'),
            sprite_sheet.tile('ladder'),
        ])
        self.camera = Camera(pos=[0, 0])

        self.add_listener(self.knight)

        # pg_mixer.music.set_volume(0.5)
        # pg_mixer.music.load('assets/sounds/music.ogg')
        # pg_mixer.music.play(loops=-1)

    def draw(self):
        self.surface.blit(sprite_sheet.tile(
            'background', size=HALF_WINDOW_SIZE), (0, 0))

        view = self.level.map.subsurface(
            tuple(self.camera.pos) + HALF_WINDOW_SIZE)

        self.surface.blit(view, (0, 0))

        self.knight.draw(self.surface, offset=(self.camera.pos[0], 0))
        self.beeto.draw(self.surface, offset=(self.camera.pos[0], 0))

        self.screen.blit(pg_transform.scale(self.surface, WINDOW_SIZE), (0, 0))

    def update(self):
        self.camera.move(self.knight)
        self.knight.move()
        self.knight.animate()
        self.beeto.move()
        self.beeto.animate()


game = ShovelKnight(TITLE, WINDOW_SIZE, fps=FPS)
game.run()
