import pygame
from pgzero.actor import Actor
from pgzero.loaders import images
from game.bullet import EnemyBullet
from config import WIDTH, HEIGHT

class Boss:
    def __init__(self, x=None, y=None, image_name="enemies/boss", width=160, height=140):
        if x is None: x = WIDTH - 100
        if y is None: y = HEIGHT // 2
        self.image_name = image_name
        self.actor = Actor(image_name, (x, y))

        try:
            surf = images.load(image_name)
            if width and height:
                surf = pygame.transform.scale(surf, (width, height))
            elif width:
                ratio = width / surf.get_width()
                height = int(surf.get_height() * ratio)
                surf = pygame.transform.scale(surf, (width, height))
            
            self.width = surf.get_width()
            self.height = surf.get_height()
            self.actor._surf = surf
            self.actor._orig_surf = surf
            self.actor._update_pos()
        except Exception:
            self.width = width or 160
            self.height = height or 140

        self.speed_y = 3
        self.direction_y = 1
        self.health = 15
        self.max_health = 15
        self.shoot_timer = 0

    def move(self):
        self.actor.y += self.speed_y * self.direction_y
        if self.actor.y < 80:
            self.actor.y = 80
            self.direction_y = 1
        elif self.actor.y > HEIGHT - 80:
            self.actor.y = HEIGHT - 80
            self.direction_y = -1

    def update_shoot(self):
        self.shoot_timer += 1
        if self.shoot_timer >= 35:
            self.shoot_timer = 0
            bullet_x = self.actor.x - (self.width // 2)
            return EnemyBullet(bullet_x, self.actor.y)
        return None

    def take_damage(self, amount=1):
        self.health -= amount
        return self.health <= 0

    def draw(self):
        self.actor.draw()
