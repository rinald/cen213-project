from abc import ABC, abstractmethod
import sys

import pygame
import pygame.display as pg_display
import pygame.time as pg_time
import pygame.event as pg_event

from pygame.locals import *


class Game(ABC):
    def __init__(self, title, window_size, fps=60):
        self.title = title
        self.window_size = window_size
        self.fps = fps

        pygame.init()
        pg_display.set_caption(title)

        self.screen = pg_display.set_mode(window_size)
        self.clock = pg_time.Clock()
        self.event_listeners = []

    def add_listener(self, listener):
        self.event_listeners.append(listener)

    def run(self):
        self.init()

        while True:
            for event in pg_event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                for listener in self.event_listeners:
                    listener.update(event)

            self.draw()
            self.update()

            pg_display.update()
            self.clock.tick(self.fps)

    @abstractmethod
    def init(self):
        ...

    @abstractmethod
    def draw(self):
        ...

    @abstractmethod
    def update(self):
        ...
