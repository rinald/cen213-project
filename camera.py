from engine import *


class Camera:
    def __init__(self, pos=None):
        self.pos = pos
        self.vx = 0

    # def on_event(self, event):
    #     if event.type == KEYDOWN:
    #         if event.key == K_a:
    #             if self.pos[0] > 0:
    #                 self.vx = -15
    #         if event.key == K_d:
    #             if self.pos[0] < 50 * 16:
    #                 self.vx = 15
    #     if event.type == KEYUP:
    #         self.vx = 0

    def move(self, player):
        self.pos[0] += self.vx*dt

        if player.pos[0] > 200-16 and player.pos[0] < 600-16:
            self.vx = player.vx

        if self.pos[0] < 0:
            self.pos[0] = 0
            self.vx = 0
        elif self.pos[0] > 400:
            self.pos[0] = 400
            self.vx = 0
