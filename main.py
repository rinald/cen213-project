from engine import *

from enemy import Enemy
from player import Player, frames

FPS = 60
WINDOW_SIZE = (800, 480)
TITLE = 'Shovel Knight'

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
        self.player = Player(
            sprite_sheet='assets/images/shovel_knight.png',
            rect=frames['idle'],
            scale=(2, 2),
            pos=[300, 415-29],
        )
        self.enemy = Enemy(pos=[64, 480-64-30])
        self.add_listener(self.player)

        pg_mixer.music.set_volume(0.5)
        pg_mixer.music.load('assets/sounds/music.ogg')
        pg_mixer.music.play()

    def draw(self):
        self.screen.blit(sprite_sheet.tile(
            'background', size=WINDOW_SIZE), (0, 0))
        for i in range(20):
            if i == 0:
                self.screen.blit(sprite_sheet.tile('ground0'), (32*i, 480-64))
                self.screen.blit(sprite_sheet.tile('ground4'), (32*i, 480-32))
            elif i == 19:
                self.screen.blit(sprite_sheet.tile('ground2'), (32*i, 480-64))
                self.screen.blit(sprite_sheet.tile('ground5'), (32*i, 480-32))
            else:
                self.screen.blit(sprite_sheet.tile('ground1'), (32*i, 480-64))
                self.screen.blit(sprite_sheet.tile('ground3'), (32*i, 480-32))

        for i in range(2):
            self.screen.blit(sprite_sheet.tile('spikes'), (640+32*i, 480-32))

        for i in range(3):
            self.screen.blit(sprite_sheet.tile(
                'ground6'), (640+64+32*i, 480-32))
            self.screen.blit(sprite_sheet.tile(
                'ground6'), (640+64+32*i, 480-2*32))
            if i == 0:
                self.screen.blit(sprite_sheet.tile(
                    'ground4'), (640+64+32*i, 480-3*32))
                self.screen.blit(sprite_sheet.tile(
                    'ground0'), (640+64+32*i, 480-4*32))
            elif i == 2:
                self.screen.blit(sprite_sheet.tile(
                    'ground5'), (640+64+32*i, 480-3*32))
                self.screen.blit(sprite_sheet.tile(
                    'ground2'), (640+64+32*i, 480-4*32))
            else:
                self.screen.blit(sprite_sheet.tile(
                    'ground3'), (640+64+32*i, 480-3*32))
                self.screen.blit(sprite_sheet.tile(
                    'ground1'), (640+64+32*i, 480-4*32))

        self.player.draw(self.screen)
        self.enemy.draw(self.screen)

    def update(self):
        self.player.move()
        self.player.animate()
        self.enemy.move()
        self.enemy.animate()


game = ShovelKnight(TITLE, WINDOW_SIZE, fps=FPS)
game.run()
