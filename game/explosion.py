from pgzero.actor import Actor

class Explosion:
    def __init__(self, x, y):
        self.images = ["effects/explosion_1", "effects/explosion_2", "effects/explosion_3"]
        self.current_frame = 0
        self.actor = Actor(self.images[0], (x, y))
        self.timer = 0
        self.finished = False

    def update(self):
        self.timer += 1
        if self.timer % 5 == 0:
            self.current_frame += 1
            if self.current_frame < len(self.images):
                self.actor.image = self.images[self.current_frame]
            else:
                self.finished = True

    def draw(self):
        if not self.finished:
            self.actor.draw()
