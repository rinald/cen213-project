FPS = 60


class Animation:
    def __init__(self, frames, duration, repeat=False):
        self.i = 0  # animation frame index
        self.j = 0  # game frame index
        self.nframes = len(frames)  # number of animation frames
        # update animation frame every k frames
        self.k = int(FPS / self.nframes * duration)

        self.frames = frames  # animation frames
        self.repeat = repeat  # repeat animation

    def tick(self):
        if self.j == 0:
            self.i += 1

        self.j += 1

        self.i %= self.nframes
        self.j %= self.k

    def reset(self):
        self.i = 0
        self.j = 0

    def frame(self):
        return self.frames[self.i]
