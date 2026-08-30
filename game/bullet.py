from pgzero.actor import Actor
from config import WIDTH

class Bullet:
    def __init__(self, x, y, speed=12, image="bullets/laser_player"):
        pass

    def move(self):
        pass

    def is_off_screen(self):
        pass

    def draw(self):
        pass

class EnemyBullet(Bullet):
    def __init__(self, x, y, speed=8, image="bullets/laser_enemy"):
        super().__init__(x, y, speed, image)

    def move(self):
        self.actor.x -= self.speed

    def is_off_screen(self):
        return self.actor.x < -20
