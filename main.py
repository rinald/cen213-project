import pygame as pg
import pygame.image as pg_image
import pygame.transform as pg_transform
import pygame.mixer as pg_mixer

from game import Game
from player import Player, frames
from sprite_sheet import SpriteSheet

RED = (255, 0, 0)

sprite_sheet = SpriteSheet('plains.png', {
    'background': (161, 35, 80, 60),
    'ground': (175, 224, 16, 16)
})

background = sprite_sheet.tile('background')
background = pg_transform.scale(background, (640, 480))
ground = sprite_sheet.tile('ground')
ground = pg_transform.scale(ground, (32, 32))


class ShovelKnight(Game):
    def init(self):
        self.player = Player(
            sprite_sheet='shovel_knight.png',
            rect=frames['idle'],
            scale=(2, 2),
            pos=[300, 415-29],
            spf=5
        )
        self.add_listener(self.player)

    def draw(self):
        self.screen.blit(background, (0, 0))
        for i in range(20):
            self.screen.blit(ground, (32*i, 480-32))
        self.player.draw(self.screen)

    def update(self):
        self.player.move()
        self.player.animate()


game = ShovelKnight('Shovel Knight', (640, 480), fps=60)
game.run()
