import random
from game.enemy import Enemy
from config import WIDTH, HEIGHT

class WaveManager:
    def __init__(self):
        self.spawn_timer = 0

    def update(self, enemies, player_score, boss_spawned):
        if player_score >= 1000 or boss_spawned:
            return

        self.spawn_timer += 1
        if self.spawn_timer % 45 == 0:
            y_pos = random.randint(50, max(60, HEIGHT - 50))
            enemies.append(Enemy(WIDTH + 40, y_pos, "Enemy"))
