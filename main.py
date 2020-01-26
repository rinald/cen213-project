from config import *
from engine import *

from engine.level import sprites

from camera import Camera
from enemy import Beeto
from player import Knight

HALF_WINDOW_SIZE = tuple((i//2 for i in WINDOW_SIZE))


class ShovelKnight(Game):
    def init(self):
        self.entity_pool = [
            Knight(rect=Rect(16, 240-63, 34, 31)),
            Beeto(rect=Rect(5*16, 240-47, 26, 16), bounds=(0, 10*16-26)),
            # Beeto(rect=Rect(5*16, 240-47, 26, 16), bounds=(23*16, 31*16-26)),
        ]

        self.add_listener(0)

        self.level = Level('assets/levels/level_1.txt')

        self.camera = Camera()

        pg_mixer.music.set_volume(0.5)
        pg_mixer.music.load('assets/sounds/music.ogg')
        pg_mixer.music.play(loops=-1)

    def draw(self):
        self.surface.blit(sprites.sprite(
            'bg', size=HALF_WINDOW_SIZE), (0, 0))

        view = self.level.map.subsurface(
            tuple(self.camera.pos) + HALF_WINDOW_SIZE)

        self.surface.blit(view, (0, 0))

        for entity in self.entity_pool:
            entity.draw(self.surface, offset=(self.camera.pos[0], 0))

        self.screen.blit(pg_transform.scale(self.surface, WINDOW_SIZE), (0, 0))

    def update(self):
        self.camera.move(self.entity_pool[0])

        for entity in self.entity_pool:
            entity.update(self.level.tiles)


game = ShovelKnight(TITLE, WINDOW_SIZE, fps=FPS)
game.run()
